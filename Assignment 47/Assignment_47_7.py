"""7. Write a Python program using LinearRegression to train a regression model using the dataset below.

Study Hours   Marks
    1          50
    2          55
    3          60
    4          65
    5          70

Your program should:
• Train the regression model
• Print the coefficient
• Print the intercept
"""

from sklearn.linear_model import LinearRegression

def main():
    # Dataset
    X=[[1],[2],[3],[4],[5]]
    Y=[50,55,60,65,70]

    # Create Model
    model=LinearRegression()

    # Train Model
    model.fit(X,Y)

    # Display Coefficient
    print("Coefficient is :",model.coef_)

    # Display Intercept
    print("Intercept is :",model.intercept_)
        
if __name__=="__main__":
    main()