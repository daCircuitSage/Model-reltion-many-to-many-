from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=55)

    def __str__(self):
        return self.name

class books(models.Model):
    book = models.CharField(max_length=20)
    publish_date = models.DateField()
    author = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name= 'books')

    def __str__(self):
        return self.book
        
    
