""" 8. Using the regression model created in the previous question, write a Python program to predict marks for 6
study hours and display the predicted value.
Study Hours   Marks
    1          50
    2          55
    3          60
    4          65
    5          70
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

    study_hours=[[6]]

    prediction=model.predict(study_hours)
    print("Predicted Marks:",prediction[0])
        
if __name__=="__main__":
    main()