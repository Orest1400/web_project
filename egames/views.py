from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home/home.html', {})
def contact(request):
	return render(request, 'contact/contact.html', {})
def game_review(request):
	return render(request, 'game_review/game_review.html', {})
def single_game_review(request):
	return render(request, 'game_review/single_game_review.html', {})
def post(request):
	return render(request, 'post/post.html', {})
def single_post(request):
	return render(request, 'post/single_post.html', {})