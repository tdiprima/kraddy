"""
Build a PyTorch model that learns the pattern of a straight line and matches it.
"""
import torch

from my_models import LinearRegressionModel
from plotting import plot_predictions

print("Torch version:", torch.__version__)

# CREATE AND MASSAGE DATA
weight = 0.7  # b (slope)
bias = 0.3  # a (y intercept)

start = 0
end = 1
step = 0.02

# X <class 'torch.Tensor'> len 50
X = torch.arange(start, end, step).unsqueeze(dim=1)

# y <class 'torch.Tensor'> len 50
y = weight * X + bias  # y = a + bX

split_position = int(0.8 * len(X))  # <class 'int'> 40

"""
X[:split_position] means: Get all examples up until the train split.
X[split_position:] means: Get everything from the train split, onwards.
"""
X_train, y_train = X[:split_position], y[:split_position]
X_test, y_test = X[split_position:], y[split_position:]

print("\nlengths:", len(X_train), len(y_train), len(X_test), len(y_test))

# Set manual seed since nn.Parameter are randomly initialized
torch.manual_seed(42)

# MODEL.
model_0 = LinearRegressionModel()

# Define the path to save the model
PATH = "my_model.pth"

# Save the model state dictionary
torch.save(model_0.state_dict(), PATH)

# Check the nn.Parameter(s) within the nn.Module subclass we created
print("\nmodel parameters:", list(model_0.parameters()))

# List named parameters
print("\nmodel dict:", model_0.state_dict())

"""
MAKE PREDICTIONS
inference_mode is torch.no_grad ++
"""
with torch.inference_mode():
    y_preds = model_0(X_test)

# Check the predictions
print(f"\nNumber of testing samples: {len(X_test)}")
print(f"Number of predictions made: {len(y_preds)}")
print(f"\nPredicted values:\n{y_preds}")

print("\nHow close were we?", y_test - y_preds)

plot_predictions(X_train, y_train, X_test, y_test, predictions=y_preds)
