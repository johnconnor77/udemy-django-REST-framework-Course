from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.seriallizers import MovieSerializers


@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)


@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)