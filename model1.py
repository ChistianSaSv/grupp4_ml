import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sqlite3


regressor = LinearRegression()

def train_model():
    con = sqlite3.connect("dataset.db")
    dataset = pd.read_sql_query("SELECT * FROM Dataset", con)
    X = dataset.iloc[:,:-1].values  # Independent value
    y = dataset.iloc[:, 0].values  # Dependent value, ska predicta
    
    # Splitting dataset into train and test sets.
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

    #Training the model uses the object method .fit
    regressor.fit(X_train, y_train)

    print("Training OK!")
    con.close()


def predict(Critic_Scores):
    y_pred = regressor.predict(Critic_Scores)
    y_pred = int(y_pred)
    
    result = {"predict": y_pred}
    return result
