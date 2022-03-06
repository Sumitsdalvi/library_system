from django.db import models


class Active_books(models.Manager):
    def get_queryset(self):
        return super(Active_books, self).get_queryset().filter(is_active=1)

class InActive_books(models.Manager):
    def get_queryset(self):
        return super(InActive_books, self).get_queryset().filter(is_active=0)

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_active = models.BooleanField(default=True)
    objects =  models.Manager()   # Default manager
    act_books = Active_books()  # Custom manager 1 :- To fetch all active books
    inactive_books = InActive_books() # Custom manager 2 :- To fetch all inactive books
    class meta:
        db_table = "Book"

    def __str__(self):
        return f"{self.name}"