from django.db.models.functions import Now

from content.models.items import *


class Rate(ModelBaze):

    def begin_date(self):
        periods = Period.objects.filter(rate_id=self.id).order_by('begin_date') or None
        if periods: return periods[0].begin_date
        return periods

    def end_date(self):
        periods = Period.objects.filter(rate_id=self.id).order_by('-end_date') or None
        if periods: return periods[0].end_date
        return periods

    def min_price(self):
        periods = Period.objects.filter(rate_id=self.id).order_by('price') or None
        if periods: return periods[0].price
        return periods

    def max_price(self):
        periods = Period.objects.filter(rate_id=self.id).order_by('-price') or None
        if periods: return periods[0].price
        return periods

    def now_price(self):
        periods = Period.objects.filter(rate_id=self.id, begin_date__lte=Now(), end_date__gt=Now()) or None
        if periods: return periods[0].price
        return periods

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


class Period(ModelBaze):
    rate = models.ForeignKey(Rate, blank=True, null=True, default=None, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Период и цена'
        verbose_name_plural = 'Периоды и цены'
