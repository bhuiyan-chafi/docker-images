from django.db import models

class User(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive')
    ]

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)  # Use Django's built-in password hashing for security
    status = models.BooleanField(choices=STATUS_CHOICES, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username