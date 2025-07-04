from django.db import models

# Create your models here.
SUBJECT_CHOICES = [
    ("eng", "English"),
    ("math", "Maths"),
    ("sci", "Science"),
    ("sst", "Social Studies"),
    ("re", "Religionous Education"),
]

SUBJECT_TYPE_CHOICES = [
    ('bot', "Beginning of Term"),
    ('mot', "Mid Term"),
    ('eot', "End of Term"),
    ('mock', "Mock examination"),
    ('test', "Test")
]

class Student(models.Model):
    """Consists of the parameters and methods performed on a student"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    term = models.PositiveSmallIntegerField(default=1)
    age = models.PositiveIntegerField()
    class_name = models.CharField(max_length=50)
    entry_class = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.id}-{self.first_name}-{self.last_name}"



class Subject(models.Model):
    """The base template for all subjets"""
    score = models.PositiveBigIntegerField()
    type = models.CharField(max_length=10, choices=SUBJECT_TYPE_CHOICES)