from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    GENRE_BOOK = (
        ('Romantic', 'Romantic'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Fantasy', 'Fantasy'),
        ('Old Literature', 'Old Literature'),
        ('Autobiography', 'Autobiography')
    )

    title = models.CharField(max_length=100, verbose_name='Write the name of the book')
    created_at = models.DateTimeField(verbose_name='Write the time of loading this book', max_length=100)
    author = models.CharField(max_length=100, verbose_name='Write the author')
    image = models.ImageField(upload_to='images/', verbose_name='Download the image', blank=True)
    description = models.TextField(verbose_name='Write the description')
    music = models.FileField(upload_to='audio/', verbose_name='Download the music', blank=True)
    video = models.URLField(verbose_name='Download the link of the video', blank=True)
    category_book = models.CharField(max_length=100,
                                     choices=GENRE_BOOK, verbose_name='What is the category of the book')
    opinion_book = models.CharField(max_length=100, verbose_name='Write your opinion about this book', blank=True)
    recommendation = models.CharField(verbose_name='Would you recommend that book?', blank=True, max_length=100)

    def __str__(self):
        return f'{self.title} - {self.created_at}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Review(models.Model):
    review_book = models.ForeignKey(Book, on_delete=models.CASCADE,
                                    related_name='reviews_book')
    stars = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
