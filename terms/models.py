from django.db import models
from markdownx.models import MarkdownxField
from moxutils.models import WithDateAndOwner
import reversion

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@reversion.register()
class Topic(WithDateAndOwner):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

@reversion.register()
class Term(WithDateAndOwner):
    name = models.CharField(max_length=200)
    short_version = MarkdownxField(max_length=250)
    long_version = MarkdownxField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('name', 'topic')

    def __str__(self):
        return f"{self.name} ({self.topic})"

