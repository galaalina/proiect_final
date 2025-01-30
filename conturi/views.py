from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, ProfileForm
from .models import Profile

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('acasa')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response

class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('acasa')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('acasa')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('acasa')

    def get_object(self):
        return self.request.user.profile
