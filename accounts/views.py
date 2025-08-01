from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms import MyUserCreationForm

User = get_user_model()

class RegisterView(CreateView):
    template_name = "user_create.html"
    model = User
    form_class = MyUserCreationForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:index")