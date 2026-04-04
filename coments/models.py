from django.db import models
from elements.models import Element

class Comment(models.Model):
    text = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    #element = models.ForeignKey(Element, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Comment{self.text} - {self.date_posted}"