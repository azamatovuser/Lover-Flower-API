from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=221)
    number = models.CharField(max_length=25)
    commentary = models.TextField()

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=221)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()


class Feedback(models.Model):
    RATE = (
        (0, '⭐️'),
        (1, '⭐️⭐️'),
        (2, '⭐️⭐️⭐️'),
        (3, '⭐️⭐️⭐️⭐️'),
        (4, '⭐️⭐️⭐️⭐️⭐️'),
    )
    name = models.CharField(max_length=221)
    email = models.EmailField(unique=True)
    rate = models.IntegerField(choices=RATE, default=0)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name