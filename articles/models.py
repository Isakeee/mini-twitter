from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField("Название заголовка", max_length=150)
    slug = models.SlugField("Слаг", unique=True, editable=True)
    description = models.TextField("Описание")
    images = models.ImageField("Превью", upload_to="article_image")
    # author = models.OneToOneField(
    #     settings.AUTH_USER_MODEL,  
    #     on_delete=models.CASCADE, 
    #     default=None, 
    #     null=True,
    #     )

    category = models.ForeignKey(
        "Category", 
        on_delete=models.CASCADE, 
        verbose_name="Категории"
        )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Статья"
        verbose_name_plural="Статьи"



class Category(models.Model):
    title = models.CharField("Название категории", max_length=150)
    slug = models.SlugField("Слаг", unique=True, editable=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"


