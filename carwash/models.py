from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Carwash(models.Model):
    carwash_purchased = models.CharField(max_length=50, default=0)
    free_code = models.CharField(max_length=50, blank=True, default=0)
    used_codes = ArrayField(models.TextField(), blank=True, null=True, default=list)
    main_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.main_user.first_name

class LoyaltyCode(models.Model):
    loyalty_code = ArrayField(models.TextField(), blank=True, null=True, default=list)

    # def __str__(self):
    #     return list(self.loyalty_code)

class FreeCode(models.Model):
    name = models.CharField(max_length=50, default=0)
    active_free_code = ArrayField(models.TextField(), blank=True, null=True, default=list)
    used_free_code = ArrayField(models.TextField(), blank=True, null=True, default=list)

    def __str__(self):
        return self.name