from django.db import models
from django.contrib.auth.models import User

class Carwash(models.Model):
    carwash_purchased = models.CharField(max_length=50, default=0)
    free_code = models.CharField(max_length=50, blank=True, default=0)
    main_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.main_user.first_name

class LoyaltyCode(models.Model):
    loyalty_code = models.CharField(max_length=50, default=0)

    def __str__(self):
        return self.loyalty_code