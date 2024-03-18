from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb

# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator
# from .forms import AuthorForm, QuoteForm
from .models import Quote, Author


def main(request, page=1):
    quotes = Quote.objects.all().order_by('-created_at')  # Отримуємо всі цитати з бази даних SQLite
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    # return render(request, 'quotes/index.html', context={'title': 'Home', 'quotes': quotes_on_page})
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})

#
#
# def authors(request, page=1):
#     autors = Author.objects.all()  # Отримуємо всіх Автори з бази даних SQLite
#     per_page = 24
#     paginator = Paginator(autors, per_page)
#     authors_on_page = paginator.page(page)
#     return render(request, 'quotes/authors.html',
#                   context={'title': 'Autors', 'page': 'autors', 'authors': authors_on_page})
#
#
# def add_author(request):
#     form = AuthorForm(instance=Author())
#     if request.method == 'POST':
#         form = AuthorForm(request.POST, request.FILES, instance=Author())
#         if form.is_valid():
#             form.save()
#             return redirect(to='quotes:home')
#     return render(request, 'quotes/add_author.html',
#                   context={'title': 'Add Author', 'page': 'add_author', "form": form})
#
#
