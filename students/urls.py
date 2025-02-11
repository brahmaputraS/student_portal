from django.urls import path
from .views import student_signup, signup_success

urlpatterns = [
    path('signup/', student_signup, name='student_signup'),
    path('signup-success/', signup_success, name='signup_success'),
]
