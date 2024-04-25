from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from course.models import Carusele

# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    carusele = Carusele.objects.all().order_by('-id')[:2]
    if form.is_valid():
        form.save()
    context = {'form': form, 'caruseles': carusele}
    return render(request, 'contact.html', context)
