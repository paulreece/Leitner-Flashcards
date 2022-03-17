# ShadowClan's Flashcards

“ShadowClan’s Flashcards” is a web application that allows you to create and study flashcards. Users can create multiple decks and flashcards for each deck. Once created, users will have the opportunity to study their flashcards using the Leitner System.

## How to use it.

Once you’ve registered an account, you will be directed to a homepage with the option to create a deck. Click the “Add a New Deck” link to create your first deck. Once you create a deck, you will be given an option to “Add Flashcards”. Click “Add Flashcards” to begin adding flashcards to your deck. If you would like to view your added flashcards, click “show flashcards”. By default, flashcards will be put into box 1 as part of the Leitner system. However, you are able to manually choose which box a card goes into. If you select the wrong box or make an error o a flashcard, you can simply click “Edit Flashcard” to fix it. If you no longer need a flashcard, click “Delete Flashcard”.

Once you have created a deck and its corresponding flashcards, you can click “Study Flashcards” to begin studying. Our site uses the famous Leitner System to study flashcards, so you’ll want to select “Box 1” to begin studying. If you get a card right, you’ll select the green button that reads “Answer = Correct! Add to (next box)”. If you miss a card, skip to the next card and keep studying until you get all of the cards in that box correct. Once you’ve gotten them all correct, box 1 will disappear and you will be redirected back to the box list where you can select box 2 to continue studying. Repeat this process until you finish box 4.

## More about the Leitner System.

According to Wikipedia, The Leitner system is a widely used method of efficiently using flashcards that was proposed by the German science journalist Sebastian Leitner in the 1970s. It is a simple implementation of the principle of spaced repetition, where cards are reviewed at increasing intervals. In this method, flashcards are sorted into groups according to how well the learner knows each one in Leitner's learning box. The learners try to recall the solution written on a flashcard. If they succeed, they send the card to the next group. If they fail, they send it back to the first group. Each succeeding group has a longer period before the learner is required to revisit the cards.

## How to get this web application functioning for you.

Unfortunately this web application has yet to be deployed. That means it is not available for public use. This web application was created as part of a class project to practice writing code in Django and Python. If you would like to try this for yourself, simply clone the repo and do a pipenv install of django, django-registration-redux, and environ. Once this is done, start your shell in pipenv and run python manage.py runserver.

## Project Planning

In planning this project we first created our models and their relationships in lucid charts. We then split up the work into a todo list on a trello board. Here are links to each:
[Our Trello Board](https://trello.com/b/dIgPBgnn/flashcard-shadowclan)
[Our Lucid Chart Models](https://lucid.app/lucidchart/3d502964-3799-4d63-93d0-5fc516f9695e/edit?invitationId=inv_bf5b73a4-6fba-47a7-9bd2-815d56a499ce)
