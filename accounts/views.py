from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DetailView

from accounts.forms import LoginForm, MyUserCreationForm


# Create your views here.

class LoginView(TemplateView):
    template_name = "login.html"
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {"form": form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect("login")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect("login")
        login(request, user)
        return redirect("index")


def logout_view(request):
    logout(request)
    return redirect("index")


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = MyUserCreationForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        context = {}
        context["form"] = form
        return self.render_to_response(context)


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "user_detail.html"
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        reviews = self.object.reviews.all()
        kwargs["reviews"] = reviews
        return super().get_context_data(**kwargs)





