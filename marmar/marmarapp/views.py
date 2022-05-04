from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
# Create your views here.


def home_page(request):
    project = Project.objects.all()[:4]
    return render(request,'home_page.html', {'project':project})


def contacts(request):
    return render(request,'contacts.html')


def projects(request):
    projects = Project.objects.all()
    return render(request,'projects.html', {'project': projects})


def reviews(request):
    reviews = Review.objects.all()
    paginator = Paginator(
        reviews,
        2,
        orphans=0,
        allow_empty_first_page=False,
    )
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return render(request,'reviews.html',
                  {
                      'reviews':reviews,
                      'page':page,
                      'paginator':paginator
                  })


def about(request):
    staffs = Staff.objects.all()
    paginator = Paginator(
        staffs,
        8,
        orphans=0,
        allow_empty_first_page=False,
    )
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return render(request,'about.html',
                  {
                      'staffs': staffs,
                      'paginator': paginator,
                      'page': page
                  })

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(
        request,
        'project_deail.html',
        {'project':project}
    )


def get_reviews(request):
    name = request.GET.get('name')
    text = request.GET.get('text')
    Review.objects.create(
        name=name,
        text=text
    )
    return redirect('reviews_url')

def get_contact(request):
    name = request.GET.get('name')
    number = request.GET.get('number')
    text = request.GET.get('text')
    Contact.objects.create(
        name=name,
        number=number,
        text=text
    )
    return redirect('contacts_url')