from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    urlname = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
    # Funcion para borrar archivos media al borrar el post (gracias chat bing)
    def delete(self, *args, **kwargs):
        self.image.delete()
        for element in self.galleries.all():
            element.image_comment.delete()
        super().delete(*args, **kwargs)

class Gallery(models.Model):
    # Recordatorio: el parametro related_name permite usar la variable en la template con los Proyectos
    article = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='galleries'
    )
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    urlname = models.CharField(max_length=10)

    def __str__(self):
        return self.title
