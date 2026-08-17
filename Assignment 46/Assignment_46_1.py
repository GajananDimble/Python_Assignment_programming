import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def main():
    Border ="_"*40

    # Step 1 : Load The  data
    print(Border)
    print("Step 1 : Load The  data")
    print(Border)

    df=pd.read_csv("Advertising.csv")
    print("Dataset loaded suceesfully")

    print(df.head())
    print(Border)
    print("Datset shape:",df.shape)

    # Step 2 : Clean,prepare and manipulate data
    
    print(Border)
    print("Step 2 : Clean,prepare and manipulate data")
    print(Border)

    print("Missing Value:")
    print(df.isnull().sum())

    X=df[["TV","radio","newspaper"]]
    Y=df["sales"]

    print("\nInput Features:")
    print(X.head())

    print("\nTarget Values:")
    print(Y.head())

    # Step 3 : Train Data

    print(Border)
    print("Step 3: Train Data")
    print(Border)

    X_train,X_test,Y_train,Y_test= train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )
    print("Training Data:",X_train.shape)
    print("Testing Data:",X_test.shape)

    Model=LinearRegression()

    Model.fit(X_train,Y_train)

    print("Linear Regression suceessfully")

    # Step 4: Test Data
    print(Border)
    print("Step 4: Test Data")
    print(Border)

    Y_pred=Model.predict(X_test)

    print("Testing completed suceessfully")

    # Step 5: Display Expected and predicted Values

    print(Border)
    print("Step 5: Display Expected and predicted Values")
    print(Border)

    result=pd.DataFrame({
        "Expected Sales":Y_test.values,
        "Predicted Sales":Y_pred
    })
    print(result.head(10))

    print(Border)
    print("Model Performance")

    MSE= mean_squared_error(Y_test,Y_pred)
    r2=r2_score(Y_test,Y_pred)

    print("Mean Squared Error:",MSE)
    print("R2 Score:",r2)

    
if __name__=="__main__":
    main()