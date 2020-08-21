from django import forms
from .models import Post, Comment
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget



""" class CKEditorWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False """


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
    partida = forms.CharField(
        widget=CKEditorWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'partida', 'thumbnail', 
        'categories', 'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )