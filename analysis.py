import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def analyze(n,p,k,temperature,humidity,ph,rainfall):
    # load the dataset
    data = pd.read_csv("crop.csv")

    # split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop("label", axis=1), data["label"], test_size=0.2)

    # train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # train the SVM model
    svm_model = SVC()
    svm_model.fit(X_train, y_train)

    # test the SVM model
    svm_accuracy = svm_model.score(X_test, y_test)
    print("SVM Accuracy:", svm_accuracy)
    # test the model
    accuracy = model.score(X_test, y_test)
    print("Accuracy:", accuracy)

    # chatbot guiding system
    # while True:
    #     n = float(input("Enter Nitrogen (N) content: "))
    #     p = float(input("Enter Phosphorus (P) content: "))
    #     k = float(input("Enter Potassium (K) content: "))
    #     temperature = float(input("Enter temperature: "))
    #     humidity = float(input("Enter humidity: "))
    #     ph = float(input("Enter pH level: "))
    #     rainfall = float(input("Enter rainfall: "))
    #     # make a prediction

    crop = model.predict([[n,p,k,temperature,humidity,ph,rainfall]])
    return crop