from django import forms
from sportsnews.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Leave a comment…'
            }),
        }

