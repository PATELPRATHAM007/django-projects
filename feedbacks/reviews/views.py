from django.shortcuts import render
from django.http import HttpResponseRedirect
def reviews(request):
    if request.method == "POST":
        entered_username = request.POST["username"]
        print(entered_username)
        return HttpResponseRedirect("/thank-you")
    return render(request,"reviews/review.html")


def thankYou(request):
    return render(request,"reviews/thank_you.html")