from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from .models import Post
from .models import Comments
from .forms import PostForm,Comments


# Create your views here.

#def homepage(request):
    #return render(request, 'homepage.html')

class Homepage(ListView):
    model = Post 
    template_name = 'homepage.html'

class Post_details(DetailView):
    model = Post
    template_name = 'post_details.html'

class Submit_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = "submit_post.html"
    #fields = '__all__'

class Post_comments(CreateView):
    model = Comments
    form_class = Comments
    template_name = "post_comments.html"


    def form_valid(self, form):
       form.instance.post_id = self.kwargs['pk']
       return super().form_valid(form)


  

class About(ListView):
    model = Post
    template_name = "about.html"
    fields = "__all__"


