#
# Model serializers
# - define exposed model fields
# - define validation
# - provide access controls
#
# See http://www.django-rest-framework.org/api-guide/serializers
#
from rest_framework import serializers
from ..models import Stock


class StockSerializer(serializers.ModelSerializer):
    """
    Serialize and Validate

    TODO: create a BaseMeta to handle common audit fields
    """

    class Meta:
        model = Stock
        fields = (
            "pk",
            "created",
            "created_by",
            "modified",
            "modified_by",
            "name",
            "symbol",
            "dividend_type",
        )
        # prevent users from modifying the following - celery task owns these fields
        read_only_fields = ("pk", "created", "created_by", "modified", "modified_by")
