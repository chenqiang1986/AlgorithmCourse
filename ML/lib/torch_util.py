import torch
import pandas as pd

def convert_to_torch(X_train, y_train, X_val, y_val, X_test, y_test):

    if isinstance(y_train, pd.DataFrame) or isinstance(y_train, pd.Series):
        y_train = y_train.to_numpy()

    if (len(y_train.shape) == 1):
        y_train = y_train.reshape(-1, 1)
    
    if isinstance(y_test, pd.DataFrame) or isinstance(y_test, pd.Series):
        y_test = y_test.to_numpy()
    
    if (len(y_test.shape) == 1):
        y_test = y_test.reshape(-1, 1)

    if isinstance(y_val, pd.DataFrame) or isinstance(y_val, pd.Series):
            y_val = y_val.to_numpy()
        
    if (len(y_val.shape) == 1):
        y_val = y_val.reshape(-1, 1)

    return (
        torch.from_numpy(X_train).to(torch.float32),
        torch.from_numpy(y_train).to(torch.float32),
        torch.from_numpy(X_val).to(torch.float32),
        torch.from_numpy(y_val).to(torch.float32),
        torch.from_numpy(X_test).to(torch.float32),
        torch.from_numpy(y_test).to(torch.float32),
    )