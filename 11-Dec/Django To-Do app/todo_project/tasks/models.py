from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
    ('Pending','Pending'),
    ('Completed','Completed'),
    )

    title=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=20,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"
