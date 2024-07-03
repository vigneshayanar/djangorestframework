from django.db import models

# Create your models here.    content=models.TextField(blank=True,null=True)
class post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
