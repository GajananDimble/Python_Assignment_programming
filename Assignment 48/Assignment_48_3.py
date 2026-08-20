"""Q.3. Consider below task
1. Train linear regression model.
2. Predict salary for 6 years of experience.
3. Plot regression line using matplotlib.

    Experience  Salary
        1       20000
        2       25000
        3       30000
        4       35000
        5       40000

"""
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def main():
    # DataSet
    X=[[1],[2],[3],[4],[5]]
    Y=[20000,25000,30000,35000,40000]

    model=LinearRegression()

    model.fit(X,Y)

    prediction=model.predict([[6]])

    print("Prediction Salary for 6 years Experience :",int(prediction[0]))

    y_pred=model.predict(X)

    plt.scatter(X,Y)

    plt.plot(y_pred)

    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")

    plt.grid(True)
    plt.show()
    
if __name__=="__main__":
    main()

"""
Expected Output
Predicted Salary for 6 Years Experience: ₹45000
Graph should display:
• Data points
• Regression line
"""