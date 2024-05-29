from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import models, forms


class RegisterView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'employees/register.html'
    success_url = reverse_lazy('employees:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        experience = form.cleaned_data['experience']
        if isinstance(experience, str):
            experience = int(experience)

        if experience <= 2:
            self.object.job = 'Junior'
        elif 2 <= experience < 4:
            self.object.job = 'Strong Junior'
        elif 4 <= experience <= 8:
            self.object.job = "Middle"
        elif 8 <= experience <= 12:
            self.object.job = "Strong Middle"
        elif 12 <= experience <= 18:
            self.object.job = "Senior"
        elif 18 <= experience <= 30:
            self.object.job = "Strong Senior"
        else:
            self.object.job = "Category is not Defined"
        self.object.save()
        return response


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'employees/login.html'

    def get_success_url(self):
        return reverse('employee:employee_list')


class AuthLogOutView(LogoutView):
    next_page = reverse_lazy('employee:login')


class EmployeeListView(ListView):
    template_name = 'employees/employee_list.html'
    model = models.CustomEmployee

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = getattr(self.request, 'job', 'Category is not Defined')
        return context
