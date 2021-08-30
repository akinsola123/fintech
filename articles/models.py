from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Blog(models.Model):

    """
    db for blog post
    """    

    title = models.CharField(
        verbose_name = _('Blog Title'),
        max_length=200, null=True,
        unique=True,
        help_text = _('Enter your blog title here.')
        )

    img = models.ImageField(
       verbose_name = _('Blog Image'),
       null=True,
       upload_to = "blog_post/",
       help_text = _('Blog Image'),
    )

    # amount = models.FloatField()


    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blog')

    def __str__(self):
        return str(self.title)

