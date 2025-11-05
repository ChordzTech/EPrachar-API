from rest_framework import serializers
from Organisation.models import Organisation

class OrganisationSerializer(serializers.ModelSerializer):
     class Meta:
          model = Organisation
          fields = "__all__"
