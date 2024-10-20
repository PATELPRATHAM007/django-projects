from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="your name",max_length=100,error_messages={
#         "required"  : "your name must be required",
#         "max_length" : "please eneter shorter name !"
#     })
#     review_text = forms.CharField(label="Your review",widget=forms.Textarea , max_length=200)
#     rating = forms.IntegerField(label="your rating" ,min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ["field names","field names"]
        fields = "__all__"
        # exclude = ["field name"]
        labels = {
                "user_name" : "Your Name",
                "review_text" : "Your Feedback",
                "rating" : "Your Rating",
        }
        error_messages = {
            "user_name" : {
                "required"  : "your name must be required",
                "max_length" : "please eneter shorter name !"
            }
        }
