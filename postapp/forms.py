from django import forms 
from postapp.models import Ticket, Comment, UserFollows, profilemodel


class Ticketform(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=("title", "description", "image")
        widgets={'description':forms.Textarea(attrs={'id':'text_id'}),
                 'title':forms.TextInput(attrs={'id':'title_id'}),
                 'image': forms.FileInput(attrs={'required': False})}
        

class Reviewform(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)
        
        widgets={'body':forms.Textarea(
            attrs={
                'placeholder': 'Votre commentaire...'}
        )}
    
    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body.strip()) == 0:  # Vérifie si le texte est vide après suppression des espaces
            raise forms.ValidationError("Le commentaire ne peut pas être vide")
        return body
           
                 


class Userfollowsform(forms.ModelForm):
    class Meta:
        model=UserFollows
        fields=["followed_user"]

class profilform(forms.ModelForm):
    class Meta:
        model=profilemodel
        fields=("image","description","gender")      