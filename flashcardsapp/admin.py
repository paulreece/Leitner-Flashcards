from django.contrib import admin
from .models import User, Deck, FlashCard, Box

admin.site.register(User)
admin.site.register(Deck)
admin.site.register(FlashCard)
admin.site.register(Box)
