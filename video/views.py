from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, VideoForm
from .models import Video
from django.core.paginator import Paginator

def UploadVideo(request):
    if request.method == 'POST':
        form = VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video-list')
    else:
        form = VideoForm()
    return render(request, 'video/upload_video.html', {'form': form})

def VideoList(request):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 1)  # Show 1 video per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'videos': page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'video/video_list.html', context)

def SignUp(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {
        'form': form,
    }
    return render(request, 'video/sign_up.html', context)
