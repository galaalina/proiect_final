from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, ProfileForm
from .models import Profile

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'schimba_parola.html'
    success_url = reverse_lazy('acasa')


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('acasa')

    def form_valid(self, form):
        # Salvează utilizatorul fără a-l confirma imediat
        user = form.save(commit=False)
        user.save()  # Salvează utilizatorul efectiv în baza de date


        clienti_group, created = Group.objects.get_or_create(name="clienti")
        user.groups.add(clienti_group)

        return super().form_valid(form)



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
