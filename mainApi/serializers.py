from rest_framework import serializers
from .models import BankDetails

class BankDetailsSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=BankDetails  # what module you are going to serialize
		fields= '__all__'