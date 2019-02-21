from django.shortcuts import render

posts = [
	{
		'author': 'Alex Hamlin',
		'title': 'New site who dis?',
		'content': 'First post content',
		'date_posted': 'Feb 2019'
	},
	{
		'author': 'Not Alex Hamlin',
		'title': 'Drake still hurting over Pusha-T beef?',
		'content': 'Second post content',
		'date_posted': 'March 2019'
	},
	{
		'author': ' Definitely Not Alex Hamlin',
		'title': 'Upcomming Artists of 2019',
		'content': 'Second post content',
		'date_posted': 'April 2019'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

