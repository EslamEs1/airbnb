from django.urls import path
from .views import Property_list, PropertyDetail, AddListing, property_review
from .api_views import PropertyListApi, PropertyDetailApi


app_name = 'property'

urlpatterns = [ 
    path('', Property_list.as_view(), name='property_list'),
    path('details/<slug:slug>', PropertyDetail.as_view(), name='property_detail'),
    path('AddList/', AddListing.as_view(), name='addListing'),
    path('<slug:slug>/', property_review, name='property_review'),

    # Api
    path('api_List/', PropertyListApi.as_view(), name='PropertyList_api'),
    path('api_Detail/<int:pk>', PropertyDetailApi.as_view(),name='PropertyDetail_api'),


]