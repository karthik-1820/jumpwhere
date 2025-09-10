from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShortURLForm
from .models import ShortURL

def home(request):
    form = ShortURLForm(request.POST or None)
    short_url = None
    if request.method == 'POST' and form.is_valid():
        new_url = form.save()
        short_url = request.build_absolute_uri(f"/{new_url.short_code}")
    return render(request, 'shortner/home.html', {'form': form, 'short_url': short_url})

def redirect_url(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(url.original_url)
