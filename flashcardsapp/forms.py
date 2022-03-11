from django import forms
from .models import User, Deck, FlashCard


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ["name", "description"]


class FlashCardForm(forms.ModelForm):
    class Meta:
        model = FlashCard
        fields = ["prompt", "answer"]
