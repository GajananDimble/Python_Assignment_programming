import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

border="_"*40
######################
# Step 1 : Load Dataset
######################

print(border)
print("Step 1 : Load Dataset")
print(border)

df =pd.read_csv("Customer_Loan_Approval.csv")

print("First 5 records:")
print(df.head())
print("\nDataset Shape:")
print(df.shape)

######################
# Step 2 : Check Missing Values
######################
print(border)
print("Step 2 : Check Missing Values")
print(border)

print("Missing Values")
print(df.isnull().sum())

######################
# Step 3 : Separate Input and Output
######################

print(border)
print("Step 3 : Separate Input and Output")
print(border)

X = df.drop("LoanApproved",axis=1)
Y = df["LoanApproved"]

print("Input Variable:")
print(X.head())
print("Output Variable:")
print(Y.head())

######################
# Step 4 : Split Dataset into training and testing data
######################

print(border)
print("Step 4 : Split Dataset into training and testing data")
print(border)

X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
)

print("Training Data:",X_train.shape)
print("Testing Data:",X_test.shape)

######################
# Step 5 : Train the Data using Logistic Regression
######################
print(border)
print("Step 5 : Train Logistic Regression")
print(border)

LR_model = LogisticRegression(random_state=42,max_iter=1000)

LR_model.fit(X_train,Y_train)
print("Data training (Logistic Regression) is successfully completed")
Y_pred= LR_model.predict(X_test)
LR_accuracy = accuracy_score(Y_test,Y_pred)

print("Logistic Regression Accuracy :", LR_accuracy * 100,"%")

######################
# Step 6 : Train Decision Tree
######################

print(border)
print(" Step 6 : Train Decision Tree")
print(border)

DT_model =DecisionTreeClassifier(random_state=42)

DT_model.fit(X_train,Y_train)
print("Data training (Decision Tree) is successfully completed")

Y_pred=DT_model.predict(X_test)

DT_accuracy= accuracy_score(Y_test,Y_pred)
print("Decision Tree Accuracy :", DT_accuracy * 100,"%")

######################
# Step 7 : Train K-Nearest Neighbors
######################

print(border)
print("Step 7 : Train K-Nearest Neighbors")
print(border)

KNN_model = KNeighborsClassifier(n_neighbors=5)

KNN_model.fit(X_train,Y_train)
print("Data training of (K-Nearest Kneigbours) is successfully completed")

Y_pred = KNN_model.predict(X_test)
KNN_accuracy = accuracy_score(Y_test,Y_pred)
print("K-Nearest Neighbours Accuracy :", KNN_accuracy * 100, "%")

######################
# Step 8 : Individual Model Accuracy
######################

print(border)
print("Step 8 : INDIVIDUAL MODEL ACCURACY")
print(border)

print("Logistic Regression Accuracy :",
      LR_accuracy * 100, "%")

print("Decision Tree Accuracy       :",
      DT_accuracy * 100, "%")

print("KNN Accuracy                 :",
      KNN_accuracy * 100, "%")

######################
# Step 9: Create Hard Voting Classifier
######################

print(border)
print("Step 9: Create Hard Voting Classifier")
print(border)

HardVoting = VotingClassifier(
    estimators=[
        ("lr", LR_model),
        ("dt", DT_model),
        ("knn", KNN_model)
    ],
    voting="hard"
)
HardVoting.fit(X_train,Y_train)

Y_pred_Hard = HardVoting.predict(X_test)
Hard_accuracy = accuracy_score(Y_test,Y_pred_Hard)
print("Hard Voting Accuracy is :", Hard_accuracy * 100,"%")


######################
# Step 10 : Create Soft Voting Classifier
######################

print(border)
print("Step 10 : Create Soft Voting Classifier")
print(border)

SoftVoting = VotingClassifier(
    estimators=[
        ("lr",LR_model),
        ("dt", DT_model),
        ("knn", KNN_model)
    ],
    voting="soft"
)
SoftVoting.fit(X_train,Y_train)
Y_pred_Soft =SoftVoting.predict(X_test)

Soft_accuracy = accuracy_score(Y_test,Y_pred_Soft)
print("Soft Voting Accuracy :",Soft_accuracy * 100,"%")

######################
# Step 11 : Compare All Models
######################

print(border)
print("Step 11 : Compare All Models")
print(border)

print("Logistic Regression :", round(LR_accuracy * 100, 2), "%")
print("Decision Tree       :", round(DT_accuracy * 100, 2), "%")
print("KNN                 :", round(KNN_accuracy * 100, 2), "%")
print("Hard Voting         :", round(Hard_accuracy * 100, 2), "%")
print("Soft Voting         :", round(Soft_accuracy * 100, 2), "%")
