"""Blub"""
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Wish(models.Model):
    """Blip"""
    title_text = models.CharField(max_length=200)
    description_text = models.TextField()
    importance = models.IntegerField(
        default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    bought = models.BooleanField(default=False)
    unbuy_string = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title_text
