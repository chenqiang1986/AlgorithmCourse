# Lesson 1: USAAIO Trained-Model Rules and the Cheat Sheet
*AIO / A01-TrainingQuestionFormat*

USAAIO open-ended problems ask you to **train a model and submit it**, not just write a function. This lesson summarizes the official submission rules and the cheat sheet you are given during the contest.

Official documents:

- Rules: [Guideline: Submitting Trained Models for Open-Ended Problems](https://drive.google.com/file/d/1-N5WHW_VmcR2t14nOEGEP-TnqyyHib0m/view) (version October 4, 2026)
- Cheat sheet: [AI Save & Load Cheat Sheet](https://drive.google.com/file/d/1L2P3-7s5kpsgizrZ5L9tpYTe1-djOoJT/view) (version June 20, 2026)

## 1. The Most Important Rule: No Google, No AI

> **During the competition you may NOT use Google search, ChatGPT, Claude, Copilot, or any other AI or web help.**
>
> The only two things you can rely on are:
> 1. **The official cheat sheet** (Section 4 below)
> 2. **Colab's built-in IntelliSense**: autocomplete after typing `.`, and the pop-up showing a function's parameters and docstring

What this means for practice:

- Anything that is **not** on the cheat sheet must be in your head: pandas column operations, `train_test_split`, `StandardScaler`, `OneHotEncoder`, `LinearRegression`, and how to compute an error metric.
- IntelliSense can remind you of a **name** you half remember (`scaler.get_fe...` → `get_feature_names_out`). It cannot teach you a workflow you have never written.
- Practice the way you will compete: write the whole sample problem with only the cheat sheet open. If you get stuck, note what you looked up and drill that until you can write it from memory.

## 2. The Provided Files

A trained-model problem gives you a folder like this:

```text
Provided materials/
├── Starter code/
│   ├── Starter code - Training.ipynb
│   ├── Starter code - Inference.ipynb
│   └── Starter code - Write md.ipynb
├── Self-check.ipynb
```

| Notebook | What you do in it |
|---|---|
| `Training.ipynb` | Load training data, train (and validate) the model, **save** every file inference will need (preprocessor parameters, model, weights). |
| `Inference.ipynb` | Write `submission.py` (with a `predict(test_path)` function), then ZIP `submission.py` + all files saved by training. |
| `Write md.ipynb` | Write the required Markdown explanation of your approach (only if the problem asks). |
| `Self-check.ipynb` | Run the official check on your ZIP. **Never edit this file.** |

## 3. Student Roadmap (5 Steps)

1. **Training.ipynb**: build and train the model; save and **download** all files needed for inference (preprocessing parameters, trained model, learned weights).
2. **Inference.ipynb**: complete `submission.py`, which the grader will call. It may load any file produced in step 1. Then build and download the ZIP containing `submission.py` and those files.
3. **Self-check.ipynb**: upload your ZIP and run it. This checks whether your submission will work on the grader's side.
4. **Write md.ipynb** (if required): document your approach and thinking process.
5. **Submit** on the contest upload page: `Training.ipynb`, `Inference.ipynb`, the ZIP, and the `.md` file (if required).

## 4. How the Grader Scores You

- The grader's script is **almost the same as `Self-check.ipynb`**: it unzips your package, does `from submission import predict`, calls `predict(...)`, and scores the output.
- The grader passes the path of a **hidden test dataset**. You cannot see it or guess its location, so `predict` must work on **any** file with the same format as the training input.
- The grader may also run anti-cheating checks.

Consequences:

- If Self-check fails, the grader fails too. Run it every time you change anything.
- `predict` runs in a **fresh Python process**. Variables from your Training notebook do not exist there. Anything you learned during training (the model, the scaler mean/std, the one-hot categories) must be **saved to a file, zipped, and loaded inside `submission.py`**.
- A file you forgot to put in the ZIP causes `FileNotFoundError` on the grader, which means zero score.

## 5. What the Cheat Sheet Gives You

The cheat sheet only covers **saving and loading**. Its quick guide:

| What you have | Format | Save | Load |
|---|---|---|---|
| Table / DataFrame | `.csv` | `df.to_csv()` | `pd.read_csv()` |
| Python dict / list | `.json` | `json.dump()` | `json.load()` |
| NumPy array | `.npy` | `np.save()` | `np.load()` |
| Multiple NumPy arrays | `.npz` | `np.savez()` | `np.load()` |
| scikit-learn object | `.joblib` | `joblib.dump()` | `joblib.load()` |
| PyTorch checkpoint | `.pt` / `.pth` | `torch.save()` | `torch.load()` |

The useful code patterns inside it:

- **JSON load**: `with open(path, "r", encoding="utf-8") as f: data = json.load(f)`
- **Split**: `train_test_split(X, y, test_size=0.2, random_state=42)` (shown inside the scikit-learn example)
- **Fitted scaler**: `scaler = StandardScaler(); scaler.fit(X_train); joblib.dump(scaler, "...joblib")`, then `joblib.load(...)` and `.transform(X_test)`
- **Fitted model**: `model.fit(...)`, `joblib.dump(model, ...)`, `joblib.load(...)`, `.predict(...)` (shown with `LogisticRegression`)
- **PyTorch**: architecture in a `%%writefile` `.py` file; checkpoint dict with `model_config`, `model_state_dict`, `optimizer_state_dict`, hyperparameters; reload with `Model(**cfg)` + `load_state_dict` + `model.eval()` + `torch.no_grad()`

Reminders printed at the end of the cheat sheet:

- CSV for tables, JSON for settings, labels, metrics and logs, NumPy formats for arrays.
- `joblib` for scikit-learn objects (only load files you trust).
- PyTorch: architecture in code (preferably a separate `.py` file), values in the checkpoint. `state_dict()` includes learnable parameters **and** buffers. Save hyperparameters (dropout, image size, number of classes) in the checkpoint too.

### What the cheat sheet does NOT give you (memorize these)

| Need | You must remember |
|---|---|
| JSON → DataFrame | `df = pd.DataFrame(data)` |
| Select columns | `df[["x"]]` (2-D, a DataFrame) vs. `df["y"]` (1-D, a Series) |
| Add / drop a column | `df["new"] = ...`, `df = df.drop(columns=[...])` |
| DataFrame → NumPy | `df.to_numpy()` |
| `OneHotEncoder` | Not shown at all. See [Lesson 3](./03-feature-engineering-scaler-and-onehot.md) |
| Encoder output | sparse matrix → `.toarray()`; column names → `get_feature_names_out()` |
| `LinearRegression` | `from sklearn.linear_model import LinearRegression` |
| Metrics | `np.abs(a - p).mean()`, or `from sklearn.metrics import mean_squared_error` |

## 6. Common Mistakes

### 6.1 Treating the Training notebook as the submission
The grader never runs your Training notebook. It only runs `submission.py` from the ZIP.

### 6.2 Forgetting a file in the ZIP
If `submission.py` calls `joblib.load("scaler.joblib")`, then `scaler.joblib` must be in the ZIP. Self-check catches this. Run it.

### 6.3 Hard-coding the data path
Inside `predict`, read from the `test_path` argument, never from `"train.json"` or `"val_input.json"`.

### 6.4 Editing Self-check.ipynb
It mirrors the grader. If you have to edit it to make it pass, your submission is broken.

## Key Takeaways

- **No Google, no AI.** Only the cheat sheet and Colab IntelliSense.
- Four notebooks: Training → Inference (`submission.py` + ZIP) → Self-check → Write md.
- The grader imports `submission.py` and calls `predict(test_path)` on hidden data in a fresh process.
- Everything learned in training must be **saved, zipped, and loaded**.
- The cheat sheet covers save and load only. Pandas, encoders, models and metrics must be memorized.

Next lesson: the standard operating procedure (SOP) for training and inference, and a minimum end-to-end run of the sample problem.
