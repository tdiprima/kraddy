## Linear Regression

Linear regression is the most basic and commonly used predictive analysis.

Regression estimates are used to describe data and to explain the relationship.

Linear Regression is a type of machine learning model.

It's called "linear" because it assumes that the relationship between the variables is a straight line.

tensorflow 2.11

Lol &mdash; All I wanted was a simple fluffin linear regression example to go with my "steps".

## Example 1

[Answers: tape is required when a Tensor loss is passed](https://stackoverflow.com/questions/68879963/valueerror-tape-is-required-when-a-tensor-loss-is-passed#70193400)


You can use this as different data:

```python
x_train = [3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
           7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1]

y_train = [1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221,
           2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3]
```

## Example 2

SEE: <a href="linear_refreshin.py">linear_refreshin.py</a>

We generated some random data for `x_data` and `y_data`, and then defined the model with variables W and b, representing the weights and biases, respectively.

The predicted y values are computed as `W * x_data + b`.

The loss function used is mean squared error, which measures the difference between the predicted y values and the actual `y_data` values.

The optimizer used is stochastic gradient descent (SGD), which is a commonly used optimization algorithm for training machine learning models.

Finally, we run the training loop for 201 iterations.

After each 20 iterations, we print the current values of W and b.

## Display the results of linear regression with matplotlib

After running the training loop, we use plt.plot to plot the original data as red circles ('ro') and the fitted line as a blue line (generated by `model(x_data)`).

Finally, we call plt.legend() to display a legend, and plt.show() to display the plot.

<br>