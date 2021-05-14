import string
import random
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


def code_generate(prefix):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=14))
    return prefix+code


class Layer(models.Model):
    code = models.CharField(_('Code'), unique=True, max_length=16, default=code_generate("LY"))
    title = models.CharField(_('Title'), max_length=128)
    description = models.TextField(_('Description'), blank=True, null=True)
    tags = models.TextField(_('Tags'), blank=True, null=True)
    public = models.BooleanField(_('Public'), default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        verbose_name = _('Layer')
        verbose_name_plural = _('Layer')

    def __str__(self):
        return f"{self.code}: {self.title}"

    def tag_list(self):
        return self.tags.split(",")

    def number_of_features(self):
        return Feature.objects.filter(layer=self).count()


class Feature(models.Model):
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE)
    code = models.CharField(_('Code'), unique=True, max_length=16, default=code_generate("FT"))
    title = models.CharField(_('Title'), max_length=128)
    attendant = models.CharField(_('Attendant'), max_length=128)
    phone = models.CharField(_('Phone'), max_length=128)
    description = models.TextField(_('Description'), blank=True, null=True)
    collection = models.GeometryCollectionField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Feature')

    def __str__(self):
        return f"{self.code}: {self.title}"


class FloodPlain(models.Model):
    area = models.PolygonField()
    happened_at = models.DateTimeField(_('Happened_at'), blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        verbose_name = _('Flood Plain')
        verbose_name_plural = _('Flood Plain')

    def __str__(self):
        return f"{self.happened_at}"
