from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm


class RegisterView(View):
    template_name = 'users/register.html'
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Congratulations, {username}. Your account has been successfully created.")
            return redirect(to="users:login")
        return render(request, self.template_name, {"form": form})
