from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


challenges = {
    "january": "read a new book",
    "february": "run 5 kilometers",
    "march": "learn a new recipe",
    "april": "start a meditation practice",
    "may": "learn basic yoga",
    "june": "volunteer at a local charity",
    "july": "take a photography course",
    "august": "learn a new language",
    "september": "complete a puzzle",
    "october": "attend a workshop",
    "november": "write in a journal daily",
    "december": None,
}

# Function to handle month by name (e.g., "january")


def monthly_challenge(request, month):
    try:
        content = challenges[month.lower()]
        return render(request, "challenges/challenge.html", {
            "content": content,
            "month": month,
        })
    except :
        raise Http404()


# Function to handle month by index (e.g., 1 for "january")
def monthly_challenge_by_index(request, month):
    months = list(challenges.keys())

    if month < 1 or month > len(months):
        return HttpResponseNotFound("Invalid month number")

    selected_month = months[month - 1]
    content = challenges[selected_month]
    redirect_path = reverse("monthly_challenge", args=[selected_month])

    return HttpResponseRedirect(redirect_path)


def index(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
