from curses import flash
from pickle import FALSE
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User, Deck, FlashCard
from .forms import DeckForm, FlashCardForm
from django.contrib.auth.decorators import login_required, user_passes_test


def homepage(request):
    if request.user.is_authenticated:
        return redirect("deck_list")

    return render(request, "home.html")


@login_required(login_url="auth_login")
def deck_list(request):
    decks = Deck.objects.all()
    for deck in decks:
        flashcards = FlashCard.objects.all()
    return render(
        request, "deck_list.html", {
            "decks": decks, "flashcards": flashcards, "deck": deck}
    )


@ login_required
def show_flashcards(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    flashcards = FlashCard.objects.all().filter(flashcard_deck_id=deck.id)

    return render(request, "show_flashcards.html", {"deck": deck, "flashcards": flashcards})


@ login_required
def add_deck(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'GET':
        form = DeckForm()
    else:
        form = DeckForm(data=request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = user
            deck.save()
            return redirect(to="deck_list")

    return render(request, "add_deck.html", {"form": form, "user": user})


@ login_required
def edit_deck(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = DeckForm(request.POST, instance=deck)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = user
            deck.save()
            return redirect(to="deck_list")
    else:
        form = DeckForm(instance=deck)
    return render(request, "edit_deck.html", {'form': form, "deck": deck, "user": user})


@ login_required
def delete_deck(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == 'POST':
        deck.delete()
        return redirect(to='deck_list.html')

    return render(request, "delete_deck.html",
                  {"deck": deck})


@ login_required
def add_flashcard(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == 'GET':
        form = FlashCardForm()
    else:
        form = FlashCardForm(data=request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.flashcard_deck_id = deck.id
            flashcard.save()
            return redirect(to="show_flashcards", slug=deck.slug)

    return render(request, "add_flashcard.html", {"form": form, "deck": deck})


@ login_required
def edit_flashcard(request, pk, slug):
    deck = get_object_or_404(Deck, slug=slug)
    flashcard = get_object_or_404(FlashCard, pk=pk)

    if request.method == "POST":
        form = FlashCardForm(request.POST, instance=flashcard)
        if form.is_valid():

            flashcard.deck_id = deck.id
            flashcard.save()
            return redirect(to="show_flashcards", slug=deck.slug)
    else:
        form = FlashCardForm(instance=flashcard)
    return render(request, "edit_flashcard.html", {'form': form, "deck": deck, "flashcard": flashcard})


@ login_required
def delete_flashcard(request, pk, slug):
    deck = get_object_or_404(Deck, slug=slug)
    flashcard = get_object_or_404(FlashCard, pk=pk)
    if request.method == 'POST':
        flashcard.delete()
        return redirect(to='show_flashcards', slug=deck.slug)

    return render(request, "delete_flashcard.html",
                  {"deck": deck, "flashcard": flashcard})


@ login_required
def show_prompt(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    flashcards = FlashCard.objects.filter(flashcard_deck_id=deck.id).get(pk=pk)
    return render(request, "show_prompt.html", {"deck": deck, "flashcards": flashcards})


@ login_required
def show_answer(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    flashcards = FlashCard.objects.get(pk=pk)
    return render(request, "show_answer.html", {"flashcards": flashcards, "deck": deck})


@ login_required
def add_correct(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    flashcard = get_object_or_404(FlashCard, pk=pk)
    if request.method == "GET":
        correct = FlashCard
    else:
        correct = FlashCard(request.method == "POST")

        FlashCard.objects.filter(pk=flashcard.pk).update(
            correct=True
        ),
        return redirect(to="show_prompt", slug=deck.slug, pk=flashcard.pk)

    return render(request, "correct.html", {"deck": deck, "flashcard": flashcard, "correct": correct},)


@ login_required
def add_incorrect(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    flashcard = get_object_or_404(FlashCard, pk=pk)
    if request.method == "GET":
        incorrect = FlashCard
    else:
        missed = flashcard.missed
        missed += 1
        incorrect = FlashCard(request.method == "POST")

        FlashCard.objects.filter(pk=flashcard.pk).update(
            correct=False, missed=missed
        ),
        return redirect(to="show_prompt", slug=deck.slug, pk=flashcard.pk)

    return render(request, "incorrect.html", {"deck": deck, "flashcard": flashcard, "incorrect": incorrect},)


@ login_required
def show_incorrect(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    flashcards = FlashCard.objects.all().filter(flashcard_deck_id=deck.id)

    return render(request, "show_incorrect.html", {"deck": deck, "flashcards": flashcards})


# class FlaschCardListView(LoginRequiredMixin, ListView):
#     model = FlashCard
#     context_object_name = 'flashcards'
#     template_name = 'flashcards.html'
#     login_url = '/login'

#     def get_queryset(self):
#         return self.request.user.deck.flashcard.all()
