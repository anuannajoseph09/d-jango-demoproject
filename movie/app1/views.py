from django.shortcuts import render,redirect
from app1.models import Movie
from app1.forms import MovieForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView


# Create your views here.
#function based
# def home(request):
#
#     k=Movie.objects.all()
#     return render(request, 'home.html',{'movie':k})
# class based
class Home(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movie"

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     queryset = qs.filter(name__startswith="a")
    #     return queryset


     # def get_context_data(self):
     #     context=super().get_context_data()
     #     context['name']="arun"
     #     context['age']="34"
     #     return context
    # extra_context = {'name':'arun','age':21}
class Addmovie(CreateView):
    model=Movie
    fields=['title','description','year','image','language']
    template_name='add1.html'
    success_url=reverse_lazy('app1:home')
# def addmovie1(request):
#     if(request.method=="POST"):
#         form=MovieForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#     form=MovieForm()
#     context={'form':form}
#     return render(request,'add1.html',context)
# def addmovie(request):
#     if(request.method=="POST"):
#         t=request.POST['t']
#         d=request.POST['d']
#         y=request.POST['y']
#         l=request.POST['l']
#         i=request.FILES['i']
#
#         m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
#         m.save()
#         return home(request)
#
#
#
#     return render(request, 'add.html')
# def detail(request,i):
#     k=Movie.objects.get(id=i)
#     return render(request,'detail.html',{'movie':k})

class Detail(DetailView):
    model=Movie
    template_name="detail.html"
    context_object_name="movie"

# def edit(request,a):
#     k=Movie.objects.get(id=a)
#     if(request.method=="POST"):
#         k.title=request.POST['t']
#         k.description=request.POST['d']
#         k.year=request.POST['y']
#         k.language=request.POST['l']
#         if(request.FILES.get('i')==None):
#             k.save()
#         else:
#             k.image=request.FILES['i']
#
#         k.save()
#         return home(request)
#
#     return render(request,'edit.html',{'movie':k})
class Edit(UpdateView):
    model = Movie
    fields = ['title', 'description', 'year', 'image', 'language']
    template_name = 'edit.html'
    success_url = reverse_lazy('app1:home')


# def delete(request,p):
#     k = Movie.objects.get(id=p)
#     k.delete()
#     return home(request)

class Delete(DeleteView):
    template_name="delete.html"
    model=Movie
    success_url=reverse_lazy('app1:home')


