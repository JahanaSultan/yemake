from django.shortcuts import render, redirect
from recipes.models  import Blog, Category
from blog.models import Blog as Blg
from django.db.models import Q
from django.db.models import Count
from .forms import ContactForm, NewsletterForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.conf import settings

from django.contrib import messages


from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers

from users.models import Profile

from django.contrib.auth.decorators import user_passes_test

from django.core.mail import EmailMessage

from .models import SubscribedUsers
from notification.models import Notification
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


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "Abunə olmaq üçün e-poçt yazmalısınız")
            return redirect("/")

        if Profile.objects.filter(email=email).first():
            messages.error(request, f"{email} emaili ilə qeydiyyatdan keçmiş istifadəçi tapıldı. İzləmək və ya izləmədən çıxmaq üçün giriş edin.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        if SubscribedUsers.objects.filter(email=email).first():
            messages.error(request, f"{email} email addresi artıq var.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email uğurla əlavə edildi!')
        return redirect(request.META.get("HTTP_REFERER", "/"))


@user_passes_test(lambda u: u.is_superuser)
def newsletter(request):
        if request.method == 'POST':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data.get('subject')
                receivers = form.cleaned_data.get('receivers').split(',')
                email_message = form.cleaned_data.get('message')
               
                mail = EmailMessage(subject, email_message, settings.EMAIL_HOST_USER, bcc=receivers)
                mail.content_subtype = 'html'

                if mail.send():
                    messages.success(request, "Email Göndərildi")
                else:
                    messages.error(request, "Xəta Baş Verdi")

            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

            return redirect('index')

        form = NewsletterForm()
        form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
        return render(request, template_name='newsletter.html', context={'form': form})



def error_404_view(request, exception):
    return render(request, '404.html')