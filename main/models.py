from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technology = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    view_live_link = models.CharField(max_length=150, blank=True)
    github_link = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-id']
