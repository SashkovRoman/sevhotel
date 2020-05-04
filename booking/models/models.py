from django.db import models


class Guest(models.Model):
    last_name = models.CharField(max_length=256, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=256, blank=True, null=True, default=None)
    email = models.EmailField(max_length=256, blank=True, null=True, default=None)
    room = models.CharField(max_length=256, blank=True, null=True, default=None)
    arrival = models.DateField(blank=True, null=True)
    departure = models.DateField(blank=True, null=True)
    adults = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    children = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    comment = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'
