from django.shortcuts import render
from .models import *
from django.core.mail import send_mail

def index(request):
    posts = Post.objects.all()
    facilities = Facilitie.objects.all()
    return render(request, 'index.html', {'posts' : posts, 'facilities' : facilities})


def posts(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'posts.html', {})

def viewposts(request, id):
    posts = Post.objects.filter(id=id);
    post = None;
    if posts:
        post = posts[0]
    return render(request, 'viewpost.html', {'post': post})

def contacts(request):
    posts = Post.objects.all()
    print(posts)
    # if request.method == 'POST':
    #     send_mail(
    #         request.POST['name'],
    #         request.POST['description'],
    #         request.POST['email'],
    #         ['mdamirten@gmail.com'],
    #         fail_silently=False,
    #     )
    return render(request, 'contacts.html', {})







#landing,
#contact,
#about,
#gallery,
#posts,
#facilities,