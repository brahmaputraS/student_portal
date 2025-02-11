from django.shortcuts import render, redirect
from .forms import StudentSignupForm

def student_signup(request):
    if request.method == "POST":
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')
    else:
        form = StudentSignupForm()

    return render(request, 'students/signup.html', {'form': form})

def signup_success(request):
    return render(request, 'students/signup_success.html')
