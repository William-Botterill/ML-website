from django.shortcuts import render
from django.http import HttpResponse
from ML_models.ml_scripts.polynomial_regression import runPolyRegression
from ML_models.ml_scripts.linear_regression import runLinearRegression
import traceback
import os

# Create your views here.
def polynomial_regression_view(request):
    #Delete previous graph if it exists
    this_folder = os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(this_folder, "..", "static", "images",
                            "graphs", "polynomial_regression_graph.png")
    try:
        os.remove(file_path)
    except:
        pass
    context = {
        'meanAbsoluteError'    : "",
        'residualSumOfSquares' : "",
        'R2score'              : ""
    }
    if request.method == "POST":
        try:
            # Load data from form
            degree = int(request.POST.get('degree'))
            test_size = float(request.POST.get('test_size'))
            interaction_only = bool(request.POST.get('interaction_only'))
            include_bias = bool(request.POST.get('include_bias'))
            normalize = bool(request.POST.get('normalize'))

            #Run ML model and get metrics
            results = runPolyRegression(test_size,degree,include_bias,normalize)
            context = {
            'meanAbsoluteError'    : results[0],
            'residualSumOfSquares' : results[1],
            'R2score'              : results[2]
            }
            
        except:
            print("AN ERROR OCCURRED")
            traceback.print_exc()
            pass
    return render(request, "polynomialRegressionForm.html", context)

def linear_regression_view(request):
    #Delete previous graph if it exists
    this_folder = os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(this_folder, "..", "static", "images",
                            "graphs", "linear_regression_graph.png")
    try:
        os.remove(file_path)
    except:
        pass
    context = {
    'meanAbsoluteError'    : "",
    'residualSumOfSquares' : "",
    'R2score'              : ""
    }
    if request.method == "POST":
        try:
            # Load data from form
            loss = request.POST.get('loss')
            test_size = float(request.POST.get('test_size'))
            penalty = request.POST.get('penalty')
            alpha = float(request.POST.get('alpha'))
            fit_intercept = bool(request.POST.get('fit_intercept'))
            max_iter = int(request.POST.get('max_iter'))
            shuffle = bool(request.POST.get('shuffle'))
            learning_rate = request.POST.get('learning_rate')
            eta0 = float(request.POST.get('eta0'))

            #Run ML model and get metrics
            results = runLinearRegression(loss=loss,test_size=test_size,penalty=penalty,
                                          alpha=alpha, fit_intercept=fit_intercept, max_iter=max_iter,
                                          shuffle=shuffle, learning_rate=learning_rate, eta0=eta0)  
            context = {
            'meanAbsoluteError'    : results[0],
            'residualSumOfSquares' : results[1],
            'R2score'              : results[2],
            }
        except Exception as e:
            print("AN ERROR OCCURRED: ", e)
            pass
    return render(request, "linearRegressionForm.html", context)