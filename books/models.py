from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    last_accessed = models.DateTimeField()

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class AuthorBookManager(models.Manager):
    def get_queryset(self):
        return super(AuthorBookManager, self).get_queryset().filter(authors=1)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(null=True, blank=True)
    num_pages = models.IntegerField(blank=True, null=True)
    objects = models.Manager() # The default manager.
    author_objects = AuthorBookManager() # Author-specific manager.

    def __str__(self):
        return self.title

