from django.conf import settings
import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from electionadmin.models import Electionadmin
from electionadmin.serializers import ElectionAdminSerializer, AdminLoginSerializer

# Create your views here.

class AdminAPI(ModelViewSet):
          queryset = Electionadmin.objects.all()
          serializer_class = ElectionAdminSerializer

          def list(self, request, *args, **kwargs):
                    try:
                              admin = Electionadmin.objects.all()
                              serializer = self.get_serializer(admin, many=True)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All admins',
                                        'all_admins': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred while fetching records: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def retrieve(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              serializer = self.get_serializer(instance)
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Admin details',
                                        'admin_details': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def create(self, request, *args, **kwargs):
                    try:
                              serializer = self.get_serializer(data=request.data)
                              serializer.is_valid(raise_exception=True)
                              serializer.save()

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_201_CREATED,
                                        'message': 'Admin added successfully',
                                        'new_admin': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
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
                                        'message': 'Admin updated successfully',
                                        'updated_admin': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
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
                                        'message': 'Admin updated successfully',
                                        'updated_admin': serializer.data,
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
                              }
                              return Response(error_response)

          def perform_update(self, serializer):
                    instance = serializer.instance
                    image_file = self.request.data.get('a_image', None)
                    if image_file:
                              user_id = instance.a_id
                              extension = image_file.name.split('.')[-1]
                              image_name = f'image{user_id}.{extension}'  # Use user_id to form image name
                              instance.a_image.delete(save=False)
                              instance.a_image = image_name
                    instance.save()

          def perform_create(self, serializer):
                    image_file = self.request.data.get('a_image', None)
                    if image_file:
                              user_id = serializer.a_id
                              extension = image_file.name.split('.')[-1]
                              image_name = f'image{user_id}.{extension}'  # Use user_id to form image name
                              serializer.a_image = image_name
                    serializer.save()

          def destroy(self, request, *args, **kwargs):
                    try:
                              instance = self.get_object()
                              instance.delete()
                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Admin deleted successfully',
                              }
                              return Response(api_response)
                    except Exception as e:
                              error_msg = 'An error occurred: {}'.format(str(e))
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_msg,
                              }
                              return Response(error_response)

class AdminLoginAPI(APIView):
          serializer_class = AdminLoginSerializer

          def post(self, request, *args, **kwargs):
                    serializer = self.serializer_class(data=request.data)

                    if serializer.is_valid():
                              username = serializer.validated_data.get('a_username')
                              password = serializer.validated_data.get('a_password')
                              type_admin = serializer.validated_data.get('a_typeadmin')
                              type_superadmin = serializer.validated_data.get('a_typesuperadmin')

                              try:
                                        admin = Electionadmin.objects.get(a_username=username)

                                        if admin.a_password == password:
                                                  admin_type = None

                                                  if admin.a_typeadmin == type_admin:
                                                            if admin.a_typesuperadmin == type_superadmin:
                                                                      if admin.a_typeadmin:
                                                                                admin_type = 'Admin'
                                                                      elif admin.a_typesuperadmin:
                                                                                admin_type = 'Superadmin'

                                                                      return Response({'message': 'Valid User',
                                                                                       'admin_type': admin_type,
                                                                                       'admin_ID': admin.a_id},
                                                                                      status=status.HTTP_200_OK)
                                                            else:
                                                                      return Response(
                                                                                {'message': 'Invalid superadmintype'},
                                                                                status=status.HTTP_401_UNAUTHORIZED)
                                                  else:
                                                            return Response({'message': 'Invalid admintype'},
                                                                            status=status.HTTP_401_UNAUTHORIZED)
                                        else:
                                                  return Response({'message': 'Invalid Password'},
                                                                  status=status.HTTP_401_UNAUTHORIZED)
                              except Electionadmin.DoesNotExist:
                                        return Response({'message': 'Invalid Credentials'},
                                                        status=status.HTTP_401_UNAUTHORIZED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetMessagebyCode(APIView):
          def get(self, request, *args, **kwargs):
                    code = self.kwargs.get('a_contactno', None)
                    if code is None:
                              return Response({'error': 'Contact number is required'},
                                              status=status.HTTP_400_BAD_REQUEST)

                    try:
                              admin = Electionadmin.objects.get(a_contactno=code)
                              serializer = ElectionAdminSerializer(admin)
                              data = serializer.data

                              # Add full path to a_image field without hardcoding the URL
                              if data['a_image']:
                                        data['a_image'] = request.build_absolute_uri(data['a_image'])

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': f'Message for {code}',
                                        'data': [data]
                              }
                              return Response(api_response)
                    except Electionadmin.DoesNotExist:
                              api_response = {
                                        'status': 'error',
                                        'code': status.HTTP_404_NOT_FOUND,
                                        'message': f'Message not found for {code}',
                              }
                              return Response(api_response)

class GetImage(APIView):
          def get(self, request, a_id):
                    try:
                              admin = Electionadmin.objects.get(a_id=a_id)
                              image_path = str(admin.a_image)  # Convert the ImageFieldFile to a string

                              # Construct the full URL
                              image_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, image_path))

                              # Assuming the image is stored in a media directory, get the full file path
                              full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)

                              # Check if the image file exists
                              if not os.path.isfile(full_image_path):
                                        error_response = {
                                                  'status': 'error',
                                                  'code': status.HTTP_404_NOT_FOUND,
                                                  'message': f'Image file not found at path: {full_image_path}',
                                        }
                                        return Response(error_response)

                              api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'Image path retrieved successfully',
                                        'image_path': image_url,  # Return the full URL
                              }
                              return Response(api_response)
                    except Electionadmin.DoesNotExist:
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_404_NOT_FOUND,
                                        'message': 'Admin with given ID does not exist',
                              }
                              return Response(error_response)
                    except Exception as e:
                              error_msg = f'An error occurred: {str(e)}'
                              error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_msg,
                              }
                              return Response(error_response)
