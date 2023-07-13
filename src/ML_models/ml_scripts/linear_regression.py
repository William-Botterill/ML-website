import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score
from django.conf import settings
from django.conf.urls.static import static

import os

# VARIABLES
filename = 'FuelConsumption.csv'
features = ['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']
variable_to_predict = 'CO2EMISSIONS'


def runLinearRegression(loss, test_size, penalty, alpha, fit_intercept, max_iter, shuffle, learning_rate, eta0):
    test_size = 0.2
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
    clf = linear_model.SGDRegressor(loss=loss, alpha=alpha, penalty=penalty, fit_intercept=fit_intercept,
                                    max_iter=max_iter, shuffle=shuffle, learning_rate=learning_rate, eta0=eta0)
    clf.fit(X_train, y_train)
    """
    # The coefficients
    print ('Coefficients: ', clf.coef_)
    print ('Intercept: ',clf.intercept_)"""

    # MAKE PREDICTIONS
    y_hat = clf.predict(X_test)

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
    XX = np.arange(0,len(X_train)/80,0.1)
    print(XX)
    print(clf.coef_[0]*XX + clf.intercept_[0])
    print(clf.coef_)
    plt.plot(XX, clf.coef_[0]*XX + clf.intercept_[0], '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    graph_folder = os.path.join(this_folder,"..", "..", "static", "images", "graphs")
    graph_path = os.path.join(graph_folder, "linear_regression_graph.png") 
    plt.savefig(graph_path, dpi=300)
    plt.close()
    results.append(graph_path)

    print("Mean absolute error: %.2f" % np.mean(np.absolute(y_hat - y_test)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((y_hat - y_test) ** 2))
    print("R2-score: %.2f" % r2_score(y_hat , y_test) )
    return results