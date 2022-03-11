from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Deck(model.models):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    user = models.ManyToManyField("User", blank=True)
    flashcard = models.ForeignKey(
        "Flashcard", on_delete=models.CASCADE, null=True, related_name="comments"
    )
    slug = models.SlugField(
        max_length=200,
        null=True,
        blank=True,
        unique=True,
    )
    date = models.DateTimeField(auto_now_add=datetime.now)


class FlashCard(model.models):
    prompt = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)
    deck = models.ManyToManyField("Deck", blank=True)
    user = models.ManyToManyField("User", blank=True)
    correct = models.BooleanField(default=True)
    missed = models.IntegerField(max_length=100, default=0)
    date = models.DateTimeField(auto_now_add=datetime.now)
