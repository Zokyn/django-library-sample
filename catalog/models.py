import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField('Birthday', null=True, blank=True, 
                                     help_text='Enter date of birth of the Author')
    date_of_death = models.DateField('Died', null=True, blank=True, 
                                     help_text='Enter date of death of the Author')
    class Meta:
        ordering = [-'date_of_birth']
    
    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])
    

    def __str__(self) -> str:
        return f'{self.last_name.upper()}, {self.first_name.capitalize()}'

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a book genre(e.g. Sci-fi)')
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    ISBN = models.CharField('ISBN', max_length=13, unique=True, help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>') # ex: 978-3-16-148140-0
    author : Author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT,
                                        null=True, default='Unknown')
    summary = models.TextField(max_length=1000, 
                               help_text='Write a brief description of the book')
    genre : Genre = models.ManyToManyField(Genre, help_text='Select a genre for this book') # ManyToMany
    def __str__(self) -> str:
        return f'{self.title};{self.author.last_name};{self.ISBN}'
    def get_absolute_url(self):
        return reverse("book_details", args=[str(self.id)])

class BookInstance(models.Model):
    LOAN_STATUS = [
        ("A", "Available"),
        ("B", "Borrowed"),
        ("D", "Delayed"),
        ("R", "Reserved"),
        ("M", "Maintenance")
    ]
    bid = models.UUIDField(primary_key=True, default=uuid.uuid4, 
                           help_text='Unique ID for this particular book in library')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    status = models.CharField(max_length=10,choices=LOAN_STATUS, blank=True, 
                              default='A', help_text='Set book availability')
    imprint = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True, help_text='date to book be returned')
    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f'{self.bid}: {self.book.title}'