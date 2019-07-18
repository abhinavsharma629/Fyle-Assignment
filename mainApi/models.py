from django.db import models

class BankDetails(models.Model):
    ifsc=models.CharField(max_length=11, null=False, blank=False)
    branch_id=models.BigIntegerField()
    branch=models.CharField(max_length=74)
    address=models.CharField(max_length=195)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=26)
    bank_name=models.CharField(max_length=49)

    def __str__(self):
        return self.ifsc
