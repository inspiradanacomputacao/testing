from django.db import models
from django.core.urlresolvers import reverse

from django.utils import timezone
from django.contrib.auth.models import User



class PublishedManager(models.Manager):
       def get_queryset(self):
           return super(PublishedManager,
                        self).get_queryset()\
                             .filter(status='published')

class Filme(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250,
                            verbose_name='Título')
    slug = models.SlugField(max_length=250,
                           unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts',
                                verbose_name='Autor(a)')
    synopsis = models.TextField(verbose_name='Sinopse')
    publish = models.DateTimeField(default=timezone.now, 
                                    verbose_name='Publicação')
    created = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Criação')
    updated = models.DateTimeField(auto_now=True,
                                    verbose_name='Atualização')
    status = models.CharField(max_length=10,
                             choices=STATUS_CHOICES,
                             default='draft', verbose_name='Status')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def get_absolute_url(self):
           return reverse('cinema:filme_detail',
                          args=[self.publish.year,
                                self.publish.strftime('%m'),
                                self.publish.strftime('%d'),
                                self.slug])        

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)


