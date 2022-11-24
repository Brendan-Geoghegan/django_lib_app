from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # put the new user in the model/db
            username = form.cleaned_data.get("username")
            messages.success(request, f"User {username} created successfully.")
            return redirect("books-home")
    else:
        form = UserRegistrationForm()
    return render(request, "registration.html", { "form": form })
