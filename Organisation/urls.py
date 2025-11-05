from django.urls import path

from Organisation.views import OrganisationAPI

urlpatterns = [
     path('all-org/', OrganisationAPI.as_view({'get': 'list'})),
     path('orgdetails/<int:pk>/', OrganisationAPI.as_view({'get': 'retrieve'})),
     path('add-org/', OrganisationAPI.as_view({'post': 'create'})),
     path('update-org/<int:pk>/', OrganisationAPI.as_view({'put': 'update'})),
     path('partialupdate-org/<int:pk>/', OrganisationAPI.as_view({'patch': 'partial_update'})),
     path('delete-org/<int:pk>/', OrganisationAPI.as_view({'delete': 'destroy'})),

]