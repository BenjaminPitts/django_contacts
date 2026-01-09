from django.shortcuts import render, redirect

from .models import Contact
from .forms import ContactForm
from django.http import JsonResponse
from .hg_statsd import counter


# import statsd
# c = statsd.StatsClient("statsd.hostedgraphite.com", 8125, prefix="8770573a-2e24-4ad5-9d1f-f69afca83321")

# Create your views here.

## index
def contact_list(request):
    # c.incr("benjaminpitts-musician.contact_list.request", 1)
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', { 'contacts': contacts})

## show
def contact_detail(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

##profile
def profile(request):
    return render(request, 'contacts/profile.html')

##about
def about(request):
    return render(request, 'contacts/about.html')

##contact
def contact(request):
    return render(request, 'contacts/contact.html')
    
##portfolio
def portfolio(request):
    return render(request, 'contacts/portfolio.html')

## new
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

## edit
def contact_edit(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

## delete
def contact_delete(request, pk):
    Contact.objects.get(id=pk).delete()
    return redirect('contact_list')

# statsd counter metric
def demo_click(request):
    counter("app.events.button_clicks", 1)
    return JsonResponse({"ok": True, "clicked": True})

def force_error(request):
    raise Exception("Intentional test error")
