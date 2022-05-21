from django.contrib import admin
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='watch_list_details'),
    path('stream/', StreamPlatformAV.as_view() , name='stream_plaforms'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_platform_details'),
]
