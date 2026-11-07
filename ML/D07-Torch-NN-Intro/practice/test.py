from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

csv_path = Path(
    "student_scores.csv"
)
df = pd.read_csv(csv_path)

print(df.head())
print(df.shape)
print(df.dtypes)

numeric_features = [
    "hours_studied",
    "attendance_rate",
    "prior_score",
]
categorical_features = ["study_method"]
target_column = "exam_score"

required_columns = numeric_features + categorical_features + [target_column]

missing_columns = set(required_columns) - set(df.columns)
if missing_columns:
    raise ValueError(f"Missing columns: {sorted(missing_columns)}")

if df[required_columns].isna().any().any():
    raise ValueError("Clean or impute missing values before conversion.")

X = df[numeric_features + categorical_features]
y = df[target_column]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.2, random_state=25)

preprocessor = ColumnTransformer(
    [
        ("num", StandardScaler(), numeric_features),
    ]
).set_output(transform="pandas")

preprocessor.fit(X_train)
X_train = preprocessor.transform(X_train)
X_val = preprocessor.transform(X_val)

print(X_train)
print(X_val)

print(torch.from_numpy(X_train.to_numpy(dtype="float32")))
print(torch.from_numpy(X_val.to_numpy(dtype="float32")))
exit(0)

feature_frame = pd.get_dummies(
    df[numeric_features + categorical_features],
    columns=categorical_features,
    dtype="float32",
)

target_frame = df[[target_column]]

print(feature_frame.head())
print(feature_frame.columns.tolist())

X_array = feature_frame.to_numpy(dtype="float32")
y_array = target_frame.to_numpy(dtype="float32")

X_train = torch.from_numpy(X_array)
y_train = torch.from_numpy(y_array)

print(X_train.shape, X_train.dtype)  # torch.Size([16, 5]) torch.float32
print(y_train.shape, y_train.dtype)  # torch.Size([16, 1]) torch.float32

assert X_train.ndim == 2
assert y_train.ndim == 2
assert X_train.shape[0] == y_train.shape[0]
assert torch.isfinite(X_train).all()
assert torch.isfinite(y_train).all()

n_examples, n_features = X_train.shape

print(n_examples)  # 16
print(n_features)  # 5

X_all = X_train
y_all = y_train

g = torch.Generator().manual_seed(42)
permutation = torch.randperm(len(X_all), generator=g)

n_train = int(0.8 * len(X_all))
train_indices = permutation[:n_train]
val_indices = permutation[n_train:]

X_train = X_all[train_indices]
y_train = y_all[train_indices]
X_val = X_all[val_indices]
y_val = y_all[val_indices]

assert len(X_train) + len(X_val) == len(X_all)

train_dataset = TensorDataset(X_train, y_train)
val_dataset = TensorDataset(X_val, y_val)

X_first, y_first = train_dataset[0]
print(X_first.shape)  # torch.Size([5])
print(y_first.shape)  # torch.Size([1])

train_loader = DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True,
)

val_loader = DataLoader(
    val_dataset,
    batch_size=8,
    shuffle=False,
)

def choose_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


device = choose_device()

torch.manual_seed(42)
model = nn.Linear(X_all.shape[1], 1).to(device)

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.2)

def train_one_epoch(model, loader, loss_fn, optimizer, device):
    model.train()
    total_loss = 0.0
    total_examples = 0

    for X_batch, y_batch in loader:
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        optimizer.zero_grad()
        output = model(X_batch)
        loss = loss_fn(output, y_batch)
        loss.backward()
        optimizer.step()

        batch_size = X_batch.shape[0]
        total_loss += loss.item() * batch_size
        total_examples += batch_size

    return total_loss / total_examples

def evaluate(model, loader, loss_fn, device):
    model.eval()
    total_loss = 0.0
    total_examples = 0

    with torch.inference_mode():
        for X_batch, y_batch in loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)

            output = model(X_batch)
            loss = loss_fn(output, y_batch)

            batch_size = X_batch.shape[0]
            total_loss += loss.item() * batch_size
            total_examples += batch_size

    return total_loss / total_examples

n_epochs = 50

for epoch in range(1, n_epochs + 1):
    train_loss = train_one_epoch(
        model, train_loader, loss_fn, optimizer, device
    )
    val_loss = evaluate(model, val_loader, loss_fn, device)

    if epoch == 1 or epoch % 10 == 0:
        print(
            f"epoch={epoch:3d} "
            f"train_loss={train_loss:.4f} "
            f"val_loss={val_loss:.4f}"
        )

