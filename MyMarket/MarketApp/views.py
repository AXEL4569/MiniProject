import os
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from . import models
from django.contrib.staticfiles.storage import staticfiles_storage
from django.db.models.base import ObjectDoesNotExist



# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def search(request):
    query = request.GET['q']
    gigs = models.Gigs.objects.filter(title__contains = query, status=True)
    return render(request, 'search.html', {'gigs': gigs})

def account(request):
    if request.user.is_authenticated:
        profiles = models.Profile.objects.filter(user = request.user)
        gigs = models.Gigs.objects.filter(user = request.user)
        return render(request, 'account.html', {'profiles':profiles, 'gigs':gigs, })
    else:
        return redirect('sign-in')

def profile(request):
    if request.method == 'POST':
        try:
            profile = models.Profile.objects.get(user = request.user)
            if len(request.FILES) != 0:
                if len(profile.avatar) > 0:
                    os.remove(profile.avatar.path)
                profile.avatar = request.FILES['avatar']
            profile.about = request.POST['about']
            profile.save()
        except ObjectDoesNotExist:
            avatar = None
            if len(request.FILES) != 0:
                avatar = request.FILES['avatar']
            about = request.POST['about']           
            profile = models.Profile.objects.create(user = request.user, avatar = avatar, about = about)
            profile.save()
        return redirect('my-account')
    else:
        if request.user.is_authenticated:
            userProfile = models.Profile.objects.filter(user = request.user)
            return render(request, 'profile.html', {'userProfile':userProfile,})
        else:
            return redirect('sign-in')

def addGig(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            newGig = models.Gigs.objects.create(
                title=request.POST["title"],
                category=request.POST["category"],
                description = request.POST["description"],
                picture = request.FILES['gigPic'],
                user=request.user,
                email=request.POST["email"],
                phoneNumber=request.POST["phno"],
                address=request.POST["address"],
            )
            newGig.save()
            return redirect('my-account')
        else:
            return render(request, 'add_gig.html', {})
    else:
        return redirect('sign-in')

def editGig(request, gigId):
    if request.user.is_authenticated:
        gig = models.Gigs.objects.get(id = gigId)
        if request.method=='POST':
            if len(request.FILES) != 0:
                if len(gig.picture) > 0:
                    os.remove(gig.picture.path)
            gig.picture = request.FILES['gigPic']
            gig.title = request.POST['title']
            gig.category = request.POST["category"]
            gig.description = request.POST.get("description")
            gig.status = request.POST["status"]
            gig.email = request.POST["email"]
            gig.phoneNumber = request.POST["phno"]
            gig.address = request.POST["address"]
            gig.save()
            return redirect('my-account')
        else:
            return render(request, 'edit_gig.html', {'gig':gig})
    else:
        return redirect('sign-in')

def gigDetail(request, gigId):
    gigs = models.Gigs.objects.filter(id=gigId)
    creator = None
    for gig in gigs:
        creator = gig.user
    profile = models.Profile.objects.get(user=creator)
    return render(request, 'gig_detail.html', {'gig':gigs, 'profile': creator})