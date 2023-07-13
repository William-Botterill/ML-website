import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.metrics import r2_score

import os

# VARIABLES
filename = 'FuelConsumption.csv'
features = ['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']
variable_to_predict = 'CO2EMISSIONS'
#test_size = 0.2
#degree = 2
#interaction_only = False  # Products that have not only one feature
#include_bias = True
#normalize = False

def runPolyRegression(test_size, degree, include_bias, normalize):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    myfile=os.path.join(this_folder, "FuelConsumption.csv")
    filename = 'FuelConsumption.csv'
    features = ['ENGINESIZE']#,'CYLINDERS','FUELCONSUMPTION_COMB']
    variable_to_predict = 'CO2EMISSIONS'

    # READ FILE
    df = pd.read_csv(myfile)

    # LOAD FEATURES
    feature_df = df[features]
    X = np.asarray(feature_df)

    # LOAD FEATURE TO BE PREDICTED
    y = np.asarray(df[variable_to_predict])

    # TRAIN TEST SPLIT
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=4)

    # LOAD MODEL
    print("Degree = ", degree)
    poly = PolynomialFeatures(degree=degree)
    train_x_poly = poly.fit_transform(X_train)
    print(train_x_poly)
    clf = linear_model.LinearRegression(normalize=normalize)
    clf.fit(train_x_poly, y_train)
    """
    # The coefficients
    print ('Coefficients: ', clf.coef_)
    print ('Intercept: ',clf.intercept_)"""

    # MAKE PREDICTIONS
    test_x_poly = poly.fit_transform(X_test)
    y_hat = clf.predict(test_x_poly)

    # GET METRICS
    results = []
    meanAbsoluteError = np.mean(np.absolute(y_hat - y_test))
    results.append(meanAbsoluteError)
    residualSumOfSquares = np.mean((y_hat - y_test) ** 2)
    results.append(residualSumOfSquares)
    R2score = r2_score(y_hat , y_test)
    results.append(R2score)

    # CREATE A GRAPH
    msk = np.random.rand(len(df)) < 0.8
    plt.scatter(df[msk].ENGINESIZE, df[msk].CO2EMISSIONS,  color='blue')
    graph = 0
    XX = np.arange(0,len(X_train)/80,0.1)
    print(clf.intercept_)
    print(clf.coef_)
    tempList = [clf.intercept_]
    
    for i in range(1,degree+1):
        tempList.append(clf.coef_[i]*np.power(XX,i))
    yy = 0
    for item in tempList:
        yy += item
    plt.scatter(df.ENGINESIZE, df.CO2EMISSIONS,  color='blue')
    plt.plot(XX, yy, '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    graph_folder = os.path.join(this_folder,"..", "..", "static", "images", "graphs")
    graph_path = os.path.join(graph_folder, "polynomial_regression_graph.png") 
    plt.savefig(graph_path, dpi=300)
    plt.close()

    print("Mean absolute error: %.2f" % np.mean(np.absolute(y_hat - y_test)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((y_hat - y_test) ** 2))
    print("R2-score: %.2f" % r2_score(y_hat , y_test) )
    return results