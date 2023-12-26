# import re 

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import ContactUs
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request, "index.html")


def team_member(request):
    return render(request, "team.html")


def about_us(request):
    return render(request, "about_us.html")


def contact_us(request):
    return render(request, "contact_us.html")


def contact(request):
    if request.method == "POST":
        # import ipdb;ipdb.set_trace();
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "phone_number": form.cleaned_data["phone_number"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            print("body", body)
            
            email_record = ContactUs(
                first_name=body.get("first_name"),
                last_name=body.get("last_name"),
                email=body.get("email"),
                phone_number=body.get("phone_number"),
                subject=subject,
                message=body.get("message"),
            )
            email_record.save()            

            try:
                send_mail(
                    subject, message, "jaikishan.shiv@gmail.com", ["jai@navgurukul.org"]
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("home")

    else:
        form = ContactUsForm()
    return render(request, "contact_us.html", {"form": form})


def blogs(request):
    return render(request, "blog.html")


def donate_us(request):
    return render(request, "donate_us.html")
