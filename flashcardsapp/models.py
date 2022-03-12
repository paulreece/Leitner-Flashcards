from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Deck(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    # deck_user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, null=True, related_name="deck_user", db_column='deck_user',
    # )
    flashcard = models.ForeignKey(
        "Flashcard", on_delete=models.CASCADE, null=True, blank=True, related_name="flashcard",
    )
    slug = models.SlugField(
        max_length=200,
        null=True,
        blank=True,
        unique=True,
    )
    date = models.DateTimeField(auto_now_add=datetime.now)


class FlashCard(models.Model):
    prompt = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)
    flashcard_deck = models.ForeignKey(
        Deck, on_delete=models.CASCADE, null=True, blank=True, related_name="flashcard_deck"
    )
    correct = models.BooleanField(default=True)
    missed = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=datetime.now)
