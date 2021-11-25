from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=5000, null=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
