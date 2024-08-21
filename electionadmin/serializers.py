from rest_framework import serializers
from electionadmin.models import Electionadmin

class ElectionAdminSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Electionadmin
                    fields = '__all__'

class AdminLoginSerializer(serializers.Serializer):
          a_username = serializers.CharField(required=True)
          a_password = serializers.CharField(required=True)
          a_typeadmin = serializers.IntegerField(required=True)
          a_typesuperadmin = serializers.IntegerField(required=True)