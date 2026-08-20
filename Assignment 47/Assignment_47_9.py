""" 9. Consider the dataset below:
StudyHours SleepHours  Marks
    1             7        50
    2             6        55
    3             7        60
    4             6        65
    5             8        70

    Write a Python program to:
• Train a regression model using this dataset
• Print the coefficients for both features
• Print the intercept
"""

from sklearn.linear_model import LinearRegression

def main():
    # Dataset
    X=[[1,7],[2,6],[3,7],[4,6],[5,8]]
    Y=[50,55,60,65,70]

    # Create Model
    model=LinearRegression()

    # Train Model
    model.fit(X,Y)

    # Display Coefficient
    print("Coefficient of StudyHours :",model.coef_[0])
    print("Coefficient of SleepHours :",model.coef_[1])

    # Display Intercept
    print("Intercept is :",model.intercept_)    
    
if __name__=="__main__":
    main()