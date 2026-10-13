# D07 — Neural Networks with PyTorch
*ML / D07-Torch-NN-Intro*

This module introduces the PyTorch API for constructing and training small
feedforward neural networks. It starts with one linear layer, then builds toward
a reusable mini-batch training workflow for regression and classification.

The focus is not memorizing one finished script. The focus is understanding the
contract between data shapes, a model's output, the loss function, automatic
differentiation, and the optimizer.

## Prerequisites

Students should already be comfortable with:

- tensor shapes and basic tensor operations from
  [Tensor Operations](../M01-Tensor/01-tensor-operations.md);
- gradients from
  [Tensor Gradients](../M01-Tensor/02-tensor-gradient.md); and
- generating and splitting data from
  [D06-Numpy-Torch-Random-Gen](../D06-Numpy-Torch-Random-Gen/README.md).

## Course Goals

By the end of this module, students should be able to:

1. explain how `nn.Linear` transforms a batch and inspect its parameters;
2. build a multilayer network with `nn.Sequential` or a custom `nn.Module`;
3. match regression, binary-classification, and multiclass outputs to the
   correct loss and target format;
4. explain and execute the five operations in a PyTorch training step;
5. load CSV data with pandas, convert prepared columns to tensors, and use
   `TensorDataset` and `DataLoader` to train with mini-batches;
6. write separate training and evaluation loops using `train()`, `eval()`, and
   `torch.inference_mode()`;
7. train and evaluate complete regression and classification models; and
8. diagnose common shape, dtype, device, gradient, and overfitting problems.

## Lessons

1. [A neuron is a linear layer](./01-a-neuron-is-a-linear-layer.md)  
   Connect $xW^T+b$ to `nn.Linear`, batch shapes, and trainable parameters.
2. [Build a network with modules and activations](./02-modules-sequential-and-activations.md)  
   Stack layers with `nn.Sequential` and define reusable models with `nn.Module`.
3. [Choose outputs and loss functions](./03-output-loss-and-target-contracts.md)  
   Match model outputs, target shapes, and target dtypes for three common tasks.
4. [Perform one training step](./04-autograd-and-one-training-step.md)  
   Follow forward, loss, zero-gradient, backward, and optimizer-step operations.
5. [Load CSV data, train with mini-batches, and evaluate](./05-dataloaders-training-and-evaluation.md)  
   Convert a pandas DataFrame to tensors, then use data loaders, epoch loops,
   evaluation mode, and correctly aggregated metrics.
6. [Complete regression project](./06-complete-regression-project.md)  
   Fit a nonlinear curve, then compare a PyTorch network with the earlier
   Walmart sales linear-regression baseline.
7. [Complete classification project and debugging guide](./07-complete-classification-project.md)  
   Learn a nonlinear decision boundary, then compare a PyTorch network with
   the earlier Telecom churn classifier.

The complete script used in Lesson 7 is available at
[`practice_ws/train_xor_classifier.py`](./practice_ws/train_xor_classifier.py).

## The Training Workflow at a Glance

```text
batch (X, y)
    │
    ▼
model(X) ──► prediction/logits ──► loss_fn(output, y) ──► scalar loss
    ▲                                                       │
    │                                                       ▼
parameters ◄── optimizer.step() ◄── parameter gradients ◄── loss.backward()
```

At the start of each new batch, clear the old gradients with
`optimizer.zero_grad()`. During validation or testing, do not call `backward()`
or `step()`.

## API Map

| Job | Main PyTorch API |
|---|---|
| Define a layer | `torch.nn.Linear` |
| Stack simple layers | `torch.nn.Sequential` |
| Define a custom model | subclass `torch.nn.Module` |
| List trainable tensors | `model.parameters()` or `model.named_parameters()` |
| Compute a regression loss | `torch.nn.MSELoss` |
| Compute a binary-classification loss | `torch.nn.BCEWithLogitsLoss` |
| Compute a multiclass loss | `torch.nn.CrossEntropyLoss` |
| Update parameters | `torch.optim.SGD` or `torch.optim.Adam` |
| Store paired tensors | `torch.utils.data.TensorDataset` |
| Create mini-batches | `torch.utils.data.DataLoader` |
| Switch training behavior on | `model.train()` |
| Switch evaluation behavior on | `model.eval()` |
| Disable gradient recording for evaluation | `torch.inference_mode()` |
| Save learned parameter values | `torch.save(model.state_dict(), path)` |

## Official References

- [Build the neural network](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html)
- [Automatic differentiation](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [Optimizing model parameters](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- [Datasets and data loaders](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html)
- [Save and load a model](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html)
- [pandas `read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [pandas `DataFrame.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html)

