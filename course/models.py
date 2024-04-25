from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Teacher(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='teachers')
    surname = models.CharField(max_length=212)
    email = models.EmailField(null=True, blank=True)
    experience = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Course(TimeStampedModel):
    name = models.CharField(max_length=212)
    tags = models.ManyToManyField(Tag)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    course_image = models.ImageField(upload_to='course')

    def __str__(self):
        return self.name


class Carusele(TimeStampedModel):
    image = models.ImageField(upload_to='carusele')
    title = models.CharField(max_length=212)
    content = models.TextField()

    def __str__(self):
        return self.title