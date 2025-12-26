from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    publish_date = models.DateField(auto_created=True)
    edit_date = models.DateField(auto_now=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    