from django.db import models
from django.utils import timezone

class Vocabulary(models.Model):
    word_hira = models.CharField(max_length=100)
    word_kanji = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=10)  # N5, N4, ...
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word_kanji or self.word_hira


class Exercise(models.Model):
    DISPLAY_MODES = (
        ('kanji', 'Kanji'),
        ('no_kanji', 'No Kanji'),
    )

    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE, related_name='exercises')
    display_mode = models.CharField(max_length=10, choices=DISPLAY_MODES)
    sentence = models.TextField()
    options = models.JSONField()
    answer = models.CharField(max_length=100)
    explanation = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vocabulary} [{self.display_mode}]"
