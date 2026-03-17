from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from . import models
from . import forms


# Create your views here.

class ProjectListView(LoginRequiredMixin,ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 6


    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:

            queryset = queryset.filter(title__icontains=q)
        return queryset


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')



class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'


    def get_success_url(self):
        return reverse('project_update', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')





class TaskCreateView(LoginRequiredMixin,CreateView):
    model = models.Task
    fields = ['description','project']
    http_method_names = ['post']


    def get_success_url(self):
        return reverse('project_update', kwargs={'pk': self.object.project.pk})


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']


    def get_success_url(self):
        return reverse('project_update', kwargs={'pk': self.object.project.pk})



class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Task


    def get_success_url(self):
        return reverse('project_update', kwargs={'pk': self.object.project.pk})