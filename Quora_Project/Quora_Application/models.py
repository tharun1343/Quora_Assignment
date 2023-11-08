from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    question = models.CharField(max_length = 100, blank = False)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.question

class Answers(models.Model):
    question_id = models.ForeignKey(Question, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    answer = models.CharField(max_length = 500, blank = False)
    likes = models.ManyToManyField(User, related_name="blog_post")
    created_at = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.answer

