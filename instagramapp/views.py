from .emails import send_welcome_email
from django.shortcuts import render, redirect
from .models import User
from .forms2 import Registration
from .forms import PostingForm
from django.views.generic import (
    ListView,
    CreateView,
)


class postList(ListView):
    template_name = "insta/post_list.html"
    queryset = User.objects.all()
    context_object_name = 'Users'


class PostCreatedView(CreateView):
    template_name = 'insta/post_created.html'
    form_class = PostingForm
    queryset = User.objects.all()
    success_url = '/'

    def form_invalid(self, form):
        print(form.cleaned_data)
        form.insta.author = self.request.user
        return super().form_valid(form)

def profile(response):
    return render(response, 'insta/profile.html')

def register(response):
    if response.method == "POST":
        form = Registration(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
        
    else:

        form = Registration()
    return render(response, "registration/register.html", {"form":form})