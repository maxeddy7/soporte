from django.db import models

# Create your models here.


class Author(models.Model):

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    cat_name = models.CharField('category name', max_length=50)
    cat_description = models.CharField('category description', max_length=255)

    def __str__(self):
        return self.cat_name


class Tag(models.Model):

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    tag_name = models.CharField(max_length=50)
    tag_descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Post(models.Model):

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(Author)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
