"""LearnML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from Pages.views import home_view, learnPR_view, signIn_view, signUp_view, signOut_view, faq_view, user_data_view, choosing_view, user_create_view, quiz_view, register, learnPRadv_view, learnLR_view, learnLRadv_view, learnLRquiz_view, learnLogR_view, learnLogRadv_view
from ML_models.views import polynomial_regression_view, linear_regression_view


urlpatterns = [
    path('admin/', admin.site.urls),

#    path('register/', register, name='register'),
    path('',home_view, name='home'),
    path('test/',user_data_view, name='test'),
    path('testcreate/',user_create_view, name='create'),

    path('learnLR/', learnLR_view, name='LR learn page'),
    path('learnLRadv/', learnLRadv_view, name='LR advanced page'),
    path('learnLRquiz/', learnLRquiz_view, name='LR quiz page'),

    path('learnPR/',learnPR_view, name='PR learn page'),
    path('learnPRadv/', learnPRadv_view, name='PR advanced page'),
    path('PRQuiz/', quiz_view, name="quiz page"),

    path('learnLogR/', learnLogR_view, name="LogR learn page"),
    path('learnLogRadv/', learnLogRadv_view, name="LogR advanced page"),

    path('choosing/polynomialRegression/',polynomial_regression_view, name='polynomial regression'),
    path('choosing/linearRegression/',linear_regression_view, name='linear regression'),
    path('faq/',faq_view, name='faq page'),
    path('choosing/',choosing_view, name='choosing page'),

    path('signup/',register, name='sign up page'),


    path('signin/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='sign in page'),
    path('signout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='sign out page'),

]
