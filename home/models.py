from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import  RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailsearch import index

class HomePage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class BlogPage(Page):
    date= models.DateField("Post date")
    intro = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    blogElement = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.TextBlock()),
        ('picture', ImageChooserBlock()),
    ], default=[])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        StreamFieldPanel('blogElement'),
    ]