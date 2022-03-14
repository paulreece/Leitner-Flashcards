from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.template.defaultfilters import slugify


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Deck(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    deck_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="deck_user", db_column='deck_user',
    )
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

    def save(self):
        self.slug = slugify(self.name)
        super().save()


class FlashCard(models.Model):
    prompt = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)
    flashcard_deck = models.ForeignKey(
        Deck, on_delete=models.CASCADE, null=True, blank=True, related_name="flashcard_deck"
    )
    correct = models.BooleanField(default=True)
    missed = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=datetime.now)
    objects = models.Manager()
    box = models.ForeignKey(
        "Box", on_delete=models.CASCADE, null=True, blank=True, related_name="box",
    )

    def __str__(self):
        return self.prompt

    def get_next(self):
        next = FlashCard.objects.filter(id__gt=self.id).order_by('?').first()
        if next:
            return next
        # If the current card is the last one, return the first card in the deck
        else:
            return FlashCard.objects.all().order_by('id').first()


class Box(models.Model):
    name = models.CharField(max_length=200)
