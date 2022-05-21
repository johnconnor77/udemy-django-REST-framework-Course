from django.contrib import admin
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchListDetailAV,
                                     StreamPlatformAV, StreamPlatformDetailAV,
                                     ReviewList, ReviewDetail, ReviewCreate)


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='watch_list_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream_plaforms'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_platform_details'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]
