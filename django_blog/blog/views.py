from django.shortcuts import render, redirect
from django.views.generic import FormView, View
from blog.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class RegisterView(FormView):
    template_name = 'blog/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your Account has been created successfully")
        return super().form_valid(form)
    


class ProfileView(LoginRequiredMixin, View):
    template_name = 'blog/profile.html'

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated successfully")
            return redirect('profile')
        
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }

        return render(request, self.template_name, context)