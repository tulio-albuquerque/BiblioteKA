from rest_framework import serializers
from .models import Loan


class LoanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "copy",
            "loaner",
            "return_date",
            "returned"
        ]
        read_only_fields = [   
            "copy",
            "loaner",
            "return_date",
            "returned"
        ]
