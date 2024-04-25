from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher, Carusele
from contact.forms import ContactForm

# Create your views here.


def home_view(request):
    courses = Course.objects.all().order_by('-id')[:3]
    teachers = Teacher.objects.all().order_by('id')[:3]
    carusel = Carusele.objects.all().order_by('id')[:3]
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'courses': courses, 'teachers': teachers, 'form': form, 'caruseles': carusel}
    return render(request, 'index.html', context)


def courselist_view(request):
    courses = Course.objects.all()
    tag = request.GET.get('tag')
    search = request.GET.get('q')
    carusel = Carusele.objects.all().order_by('id')[:3]
    print(search)
    if search:
        courses = courses.filter(name__icontains=search)
    if tag:
        courses = courses.filter(tag__contains=tag)
    context = {'courses': courses, 'caruseles': carusel}
    return render(request, 'kurslar.html', context)


def course_detail_view(request, pk):
    course = get_object_or_404(Course, id=pk)
    carusel = Carusele.objects.all().order_by('id')[:3]
    context = {'course': course, 'caruseles': carusel}
    return render(request, 'course_detail.html', context)


def teachers_list_view(request):
    teachers = Teacher.objects.all()
    carusel = Carusele.objects.all().order_by('id')[:3]
    context = {'teachers': teachers, 'caruseles': carusel}
    return render(request, 'teachers.html', context)


def teachers_detail_view(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    carusel = Carusele.objects.all().order_by('id')[:3]
    context = {'teacher': teacher, 'caruseles': carusel}
    return render(request, 'teacher_detail.html', context)

