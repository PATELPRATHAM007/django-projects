from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView , CreateView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views import View


from .forms import ReviewForm
from .models import Review



class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html", {
#             "form": form
#         })


# def reviews(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # review = Review(
#             #     user_name=form.cleaned_data["user_name"], review_text=form.cleaned_data["review_text"], rating=form.cleaned_data["rating"])
#             # review.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })


class thankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        content =  super().get_context_data(**kwargs)
        content["message"] = "its work"
        return content
# class thankYouView(View):
#     def get(self,request):
#         return render(request, "reviews/thank_you.html")

# def thankYou(request):
#     return 


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt = 4)
    #     return data


# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
    

class SingleReviewView(DetailView):
    template_name = "reviews/reviewDetails.html"
    model = Review
    context_object_name = "review"

# class SingleReviewView(TemplateView):
#     template_name = "reviews/reviewDetails.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviewId = kwargs["id"]
#         selectedReview =  Review.objects.get(pk=reviewId)
#         context["review"] = selectedReview
#         return context