import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def main():
    Border="-"*40

    # 1. Load Dataset
    print(Border)
    print("1.Load Dataset")
    df = pd.read_csv("breast-cancer-wisconsin.csv")

    print("First 5 Records:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nDataset Information:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print(Border)

    print("2: Data Preprocessing")
    # 2. Data Preprocessing

    # Replace '?' with NaN
    df = df.replace("?", pd.NA)

    # Convert BareNuclei into numeric
    df["BareNuclei"] = pd.to_numeric(df["BareNuclei"])

    # Handle missing values
    df["BareNuclei"] = df["BareNuclei"].fillna(df["BareNuclei"].median())

    # Remove unnecessary CodeNumber column
    df = df.drop("CodeNumber", axis=1)
    print(Border)

    print("3. Separate Input and Output")
    # 3. Separate Input and Output
    X = df.drop("CancerType", axis=1)
    Y = df["CancerType"]

    # Convert target:
    # 2 = Benign
    # 4 = Malignant

    Y = Y.map({
        2: 0,
        4: 1
    })

    print("\nInput Data:")
    print(X.head())

    print("\nTarget Data:")
    print(Y.head())

    print(Border)

    print("4: Summary Statistics")
    # 4. Summary Statistics
    print("\nSummary Statistics:")
    print(X.describe())
    print(Border)
    print("5. Feature Correlation")

    # 5. Feature Correlation
    plt.figure(figsize=(12, 8))

    sns.heatmap(
        X.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Feature Correlation")
    plt.show()

    print(Border)

    print("6. Train Test Split")
    # 6. Train Test Split
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("\nTraining Data:", X_train.shape)
    print("Testing Data:", X_test.shape)

    print(Border)

    print("7. Feature Scaling")
    # 7. Feature Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print(Border)

    print("8. Build Machine Learning Model")
    # 8. Build Machine Learning Model
    model = LogisticRegression()

    model.fit(X_train, Y_train)

    print(Border)

    print("9:Prediction")
    # 9. Prediction
    Y_pred = model.predict(X_test)

    print("\nPredicted Values:")
    print(Y_pred)
    print(Border)

    print("10: Accuracy")
    # 10. Accuracy
    accuracy = accuracy_score(Y_test, Y_pred)

    print("\nAccuracy:", accuracy)

    print(Border)
    print("11. Confusion Matrix")

    # 11. Confusion Matrix
    cm = confusion_matrix(Y_test, Y_pred)

    print("\nConfusion Matrix:")
    print(cm)

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()

    print(Border)
    print("12. Precision, Recall and F1-Score")

    # 12. Precision, Recall and F1-Score
    print("\nClassification Report:")

    print(classification_report(Y_test,Y_pred,target_names=["Benign","Malignant"]))

    print(Border)

if __name__ == "__main__":
    main()