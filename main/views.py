from django.shortcuts import render, redirect
from recipes.models  import Blog, Category, Review, Vote, RecipeBook
from blog.models import Blog as Blg
from django.db.models import Q
from django.db.models import Count
from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.conf import settings

from django.contrib import messages
# Create your views here.


def index(request):
    blogs=Blog.objects.filter(Q(isActive=True)).annotate(num=Count("recipebook")).order_by("-num")[0:15]
    wrts=Blg.objects.filter(Q(inSlide=True) & Q(isActive=True)).order_by("-created")[0:15]
    video=Blog.objects.filter(youtube_link__isnull=False)[0:15]
    diet=Blog.objects.filter(category__title='Diet')[0:15]
    time=Blog.objects.filter(Q(cook_time__lte=15) & Q(time="dəqiqə"))[0:15]
    categories= Category.objects.all().order_by('title').order_by("title")
    context = {
        "blog": blogs,
        "category":categories,
        "like":video,
        "diet":diet,
        "wrts":wrts,
        "time":time,
    }
    return render(request, "index.html", context)



def aboutus(request):
    return render(request, 'about-us.html')


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())
			try:
				send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER]) 
				messages.success(request, "Mesajınız Göndərildi")
			except BadHeaderError:
				messages.error(request, "Xəta!")
				return HttpResponse('Invalid header found.')
            
			return redirect ("index")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})