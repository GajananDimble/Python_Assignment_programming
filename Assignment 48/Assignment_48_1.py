"""1. Implement Simple Linear Regression manually without using any ML library.
Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

Tasks
Calculate:
1. Mean of X (X̄ )
2. Mean of Y (Ȳ)
3. Slope (m)
4. Intercept (c)

"""
def main():
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    # Calculate Mean
    mean_x=sum(X)/len(X)
    mean_y=sum(Y)/len(Y)

    print("Mean of X:",mean_x)
    print("Mean of Y:",mean_y)

    # Calculator slope
    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator
    
    c= mean_y - (m * mean_x)

    print("Slope (m)=",m)
    print("Intercept (c)=",c)

    print("Regression Equation:")
    print("Y =", m,"X +",c)

    x=6 
    predicted_y = (m * x) + c

    print("Predicted Y for X 6:",predicted_y)


if __name__=="__main__":
    main()

"""
Expected Output Example
Mean of X = 3
Mean of Y = 3.6
Slope (m) = 0.4
Intercept (c) = 2.4
Regression Equation:
Y = 0.4X + 2.4
Predicted Y for X = 6 : 4.8
"""