from django.db import models, IntegrityError

# Create your models here.

class Commodity(models.Model):
    name = models.CharField(max_length=100)
    interval = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)

    def __str__ (self):
        return self.name

class CommodityData(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, related_name='data')
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=6)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('commodity', 'date', 'value')

    def __str__(self):
        return f'{self.commodity.name} - {self.date}: {self.value}'