# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.template import RequestContext
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from models import Verse, Author
from forms import AuthorForm
from django.core.urlresolvers import reverse

def index(request):
    verses = Verse.objects.all()
    if request.method == "POST":
        verse_data = request.POST['new_verse']
        if request.user.is_authenticated() and request.user.author_profile.count() != 0:
            author = request.user.get_profile()
            verse = Verse()
            verse.author = author
            verse.verse_text = verse_data.replace(u' ',' ') # Replacing non-breaking space with space
            verse.save()
            return HttpResponseRedirect(reverse("verse_detail", args=[verse.id]))
        else:
            return HttpResponseNotAllowed(['GET'])
    return render_to_response('index.html', {'verses': verses}, context_instance = RequestContext(request))

def verse_index(request):
    verses = Verse.objects.all()
    return render_to_response('verse_index.html', {'verses':verses}, context_instance = RequestContext(request))

def verse_detail(request, id):
    verse = get_object_or_404(Verse, pk=id)
    return render_to_response('verse_detail.html', {'verse': verse}, context_instance = RequestContext(request))

@login_required
def verse_edit(request, id):
    verse = get_object_or_404(Verse, pk=id)
    if request.user != verse.author.user:
        resp = render_to_response('403.html', context_instance=RequestContext(request))
        resp.status_code = 403
        return resp
    if request.method == 'POST':
        verse_data = request.POST['edit_verse']
        verse.verse_text = verse_data.replace(u' ',' ') # Replacing non-breaking space with space
        verse.save()
        return HttpResponseRedirect(reverse("verse_detail", args=[verse.id]))
    return render_to_response('verse_edit.html', {'verse': verse}, context_instance = RequestContext(request))

def author_index(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        found_authors = Author.objects.filter(name__icontains=q).order_by('-user__date_joined')
        return render_to_response('author_index.html', { 'q':q, 'found_authors': found_authors}, context_instance = RequestContext(request))
    else:
       authors = Author.objects.annotate(number_of_verses = Count('verses'))
       authors = authors.order_by('-number_of_verses')
    return render_to_response('author_index.html', {'authors':authors}, context_instance = RequestContext(request))

def author_detail(request, id):
    author = get_object_or_404(Author, pk=id)
    return render_to_response('author_detail.html', {'author': author}, context_instance = RequestContext(request))
    
@login_required
def author_edit(request, id):
    author = get_object_or_404(Author, pk=id)
    if request.user != author.user:
        resp = render_to_response('403.html', context_instance=RequestContext(request))
        resp.status_code = 403
        return resp
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('author_detail', args=[author.id]))
        else:
           form = AuthorForm(request.POST, instance=author)
    else:
        form = AuthorForm(instance=author)
    return render_to_response('author_edit.html', {'form': form, 'author': author}, context_instance = RequestContext(request))

@login_required
def author_create(request):
    if request.user.author_profile.count() != 0:
        return HttpResponseRedirect(reverse('author_detail', args=[request.user.get_profile().id]))
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.user = request.user
            new_author.save()
            return HttpResponseRedirect(reverse('author_detail', args=[new_author.id]))
        else:
           form = AuthorForm(request.POST)
    else:
        form = AuthorForm()
    return render_to_response('author_create.html', {'form': form}, context_instance = RequestContext(request))
    
def about_us(request):
    return render_to_response('about_us.html', context_instance = RequestContext(request))

def contact_us(request):
    return render_to_response('contact_us.html', context_instance = RequestContext(request))

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        found_verses = Verse.objects.filter(verse_text__icontains=q).order_by('-publishing_date')
        return render_to_response('search.html', { 'q':q, 'found_verses': found_verses}, context_instance = RequestContext(request))
    else:
        return HttpResponse("Under construction")
