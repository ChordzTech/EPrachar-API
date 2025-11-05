from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Organisation.models import Organisation
from Organisation.serializers import OrganisationSerializer

# Create your views here.
class OrganisationAPI(ModelViewSet):
     queryset = Organisation.objects.all()
     serializer_class = OrganisationSerializer

     def list(self, request, *args, **kwargs):
          try:
               org = Organisation.objects.all()
               serializer = self.get_serializer(org, many=True)
               api_response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'All organisations',
                    'all_organisations': serializer.data,
               }
               return Response(api_response)
          except Exception as e:
               error_message = 'An error occurred while fetching organisation: {}'.format(str(e))
          error_response = {
               'status': 'error',
               'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
               'message': error_message
          }
          return Response(error_response)

     def retrieve(self, request, *args, **kwargs):
          try:
               instance = self.get_object()
               serializer = self.get_serializer(instance)
               api_response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Organisation fetched successfully',
                    'organisation_details': serializer.data,
               }
               return Response(api_response)
          except Exception as e:
               error_message = 'An error occurred while fetching organisation: {}'.format(str(e))
               error_response = {
                    'status': 'error',
                    'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': error_message
               }
          return Response(error_response)

     def create(self, request, *args, **kwargs):
          try:
               serializer = self.serializer_class(data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()

               api_response = {
                    'status': 'success',
                    'code': status.HTTP_201_CREATED,
                    'message': 'Organisation added successfully',
                    'new_organisation': serializer.data,
               }
               return Response(api_response)
          except Exception as e:
               error_message = 'Failed to add organisation: {}'.format(str(e))
               error_response = {
                    'status': 'error',
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': error_message
               }
               return Response(error_response)

     def update(self, request, *args, **kwargs):
          try:
               instance = self.get_object()
               serializer = self.get_serializer(instance, data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()

               api_response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Organisation updated successfully',
                    'updated_organisation': serializer.data,
               }
               return Response(api_response)
          except Exception as e:
               error_message = 'Failed to update organisation:{}'.format(str(e))
               error_response = {
                    'status': 'error',
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': error_message
               }
               return Response(error_response)

     def partial_update(self, request, *args, **kwargs):
          try:
               instance = self.get_object()
               serializer = self.get_serializer(instance, data=request.data, partial=True)
               serializer.is_valid(raise_exception=True)
               serializer.save()

               api_response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Organisation updated successfully',
                    'updated_organisation': serializer.data,
               }
               return Response(api_response)
          except Exception as e:
               error_message = 'Failed to partially update organisation:{}'.format(str(e))
               error_response = {
                    'status': 'error',
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': error_message
               }
               return Response(error_response)

     def destroy(self, request, *args, **kwargs):
          try:
               instance = self.get_object()
               instance.delete()

               api_response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Organisation deleted successfully',
               }
               return Response(api_response)
          except Exception as e:
               error_message = 'Failed to delete organisation:{}'.format(str(e))
               error_response = {
                    'status': 'error',
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': error_message
               }
          return Response(error_response)
