"""Using the same dataset from above question, calculate model performance.
Tasks
1. Predict all Y values using regression equation.
2. Calculate:
• Mean Squared Error (MSE)
• R2 Score
Show all intermediate calculations.

"""
def main():
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    mean_x = sum(X) / len(X)
    mean_y = sum(Y) / len(Y)

    # Calculate slope
    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator += (X[i] - mean_x) * (Y[i] - mean_y)
        denominator += (X[i] - mean_x) ** 2

    m = numerator / denominator

    # Calculate intercept
    c = mean_y - (m * mean_x)

    # Predict Y
    predictions = []

    for x in X:
        y_pred = (m * x) + c
        predictions.append(y_pred)

    print("Predicted Y values:", predictions)

    # Calculate MSE
    squared_error = 0

    for i in range(len(Y)):
        squared_error += (Y[i] - predictions[i]) ** 2

    mse = squared_error / len(Y)

    # Calculate R2
    total_error = 0

    for y in Y:
        total_error += (y - mean_y) ** 2

    r2 = 1 - (squared_error / total_error)

    print("MSE =", mse)
    print("R2 Score =", r2)


if __name__ == "__main__":
   main()