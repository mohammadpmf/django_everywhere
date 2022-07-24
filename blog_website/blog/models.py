from django.db import models

class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    authors = models.ForeignKey("auth.User", on_delete=models.CASCADE) # Yani age ye roozi ye nafar author ro az oon var paak kard man che khaki too saram berizam? ma ham goftim in ja ham pakesh kon author ro az tooye in field az in table.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title
