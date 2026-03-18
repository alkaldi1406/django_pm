from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
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
        queryset = super().get_queryset().filter(user=self.request.user)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'


    def test_func(self):
        return self.get_object().user_id == self.request.user.id



    def get_success_url(self):
        return reverse('project_update', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')


    def test_func(self):
        return self.get_object().user_id == self.request.user.id



class TaskCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = models.Task
    fields = ['description','project']
    http_method_names = ['post']


    def test_func(self):
        project_id = self.request.POST.get('project','')
        return models.Project.objects.get(pk=project_id).user_id == self.request.user.id


    def get_success_url(self):
        return reverse('project_update', kwargs={'pk': self.object.project.pk})



class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']


    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id


    def get_success_url(self):
        return reverse('project_update', kwargs={'pk': self.object.project.pk})



class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.Task

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('project_update', kwargs={'pk': self.object.project.pk})