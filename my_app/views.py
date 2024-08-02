from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import CategoryForm, MovieForm
from django.urls import reverse_lazy
from .models import Category, Movies

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class CategoryDetailView(DetailView):
    model = Category
    template_name = "category_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context["videos"] = Movies.objects.filter(category=category)
        return context

class MovieListView(ListView):
    model = Movies
    template_name = 'movie_list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

class MovieCreateView(CreateView):
    model = Movies
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieUpdateView(UpdateView):
    model = Movies
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieDeleteView(DeleteView):
    model = Movies
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

class VideoSearchView(ListView):
    model = Movies
    template_name = 'video_search_results.html'
    context_object_name = 'videos'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Movies.objects.filter(title__icontains=query)
        return Movies.objects.all()
