from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.
def signup(request):
    if request.POST == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()

    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "signup.html", context)
