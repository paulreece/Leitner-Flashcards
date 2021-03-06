"""flashcard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from flashcardsapp import views as flash_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path("", flash_views.homepage, name="homepage"),
    path("decks", flash_views.deck_list, name="deck_list"),
    path("decks/leitner", flash_views.leitner, name="leitner"),
    path("<int:pk>/add/", flash_views.add_deck, name="add_deck"),
    path("decks/<slug:slug>", flash_views.show_flashcards, name="show_flashcards"),
    path("decks/<slug:slug>/choose", flash_views.choose_box, name="choose_box"),
    path("decks/<slug:slug>/boxone/<int:pk>",
         flash_views.box_one, name="box_one"),
    path("decks/<slug:slug>/boxtwo/<int:pk>",
         flash_views.box_two, name="box_two"),
    path("decks/<slug:slug>/boxthree/<int:pk>",
         flash_views.box_three, name="box_three"),
    path("decks/<slug:slug>/boxfour/<int:pk>",
         flash_views.box_four, name="box_four"),
    path("decks/<slug:slug>/<int:pk>/add_to_box_two",
         flash_views.add_to_box_two, name="add_to_box_two"),
    path("decks/<slug:slug>/<int:pk>/add_to_box_three",
         flash_views.add_to_box_three, name="add_to_box_three"),
    path("decks/<slug:slug>/<int:pk>/add_to_box_four",
         flash_views.add_to_box_four, name="add_to_box_four"),
    path("<int:pk>/decks/<slug:slug>/edit/",
         flash_views.edit_deck, name="edit_deck"),
    path("decks/<slug:slug>/delete",
         flash_views.delete_deck, name="delete_deck"),

    path("decks/<slug:slug>/incorrect",
         flash_views.show_incorrect, name="show_incorrect"),
    path("decks/<slug:slug>/<int:pk>/correct/",
         flash_views.add_correct, name="add_correct"),
    path("decks/<slug:slug>/<int:pk>/incorrect/",
         flash_views.add_incorrect, name="add_incorrect"),
    path("decks/<slug:slug>/add/",
         flash_views.add_flashcard, name="add_flashcard"),
    path("decks/<slug:slug>/<int:pk>/edit/",
         flash_views.edit_flashcard, name="edit_flashcard"),
    path("decks/<slug:slug>/<int:pk>/delete/",
         flash_views.delete_flashcard, name="delete_flashcard"),
    path("decks/<slug:slug>/<int:pk>/prompt",
         flash_views.show_prompt, name="show_prompt"),
    path("decks/<slug:slug>/<int:pk>/answer",
         flash_views.show_answer, name="show_answer"),
]
