from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import UserRegistrationForm, ProfileForm


# Create your views here.

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    # success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_success_url(self):
        login(self.request, self.object)
        return reverse_lazy('project_list')



class EditProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('profile') # الرابط الذي يوجه إليه بعد الحفظ

    def get_object(self):
        # لضمان أن المستخدم يعدل ملفه الشخصي فقط وليس ملفات الآخرين
        return self.request.user