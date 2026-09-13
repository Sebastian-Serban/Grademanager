from django.db import models


# Create your models here.
class Grade(models.Model):
    subject = models.ForeignKey("subjects", on_delete=models.CASCADE, related_name="grades")
    grade = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grade
