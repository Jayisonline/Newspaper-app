# from django.views.generic import ListView
# from .models import Article



# class ArticleListView(ListView):
#     model = Article
#     template_name = 'article_list.html'


from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from .models import Artical

from django.core.exceptions import PermissionDenied




class ArticleListView(ListView):
    model = Artical
    template_name = 'article_list.html'
    login_url  = 'login'    



class ArticleUpdateView(UpdateView): # new
    model = Artical
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url  = 'login'    

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            return render(request, "error.html")
            # raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)




class ArticleDetailView(DetailView): # new
    model = Artical
    template_name = 'article_detail.html'
    login_url  = 'login'    



class ArticleDeleteView(DeleteView): # new
    model = Artical
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url  = 'login'  


    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            return render(request, "error.html")
        return super().dispatch(request, *args, **kwargs)  



class ArticleCreateView(LoginRequiredMixin, CreateView):
    # class ArticleCreateView(CreateView):
    model = Artical
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    login_url  = 'login'    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    

