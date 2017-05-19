from django.shortcuts import render, get_object_or_404

from .models import Filme
from .serializer import FilmeSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

def filme_list(request):
       filmes = Filme.published.all()
       return render(request,
                     'cinema/filme/list.html',
                     {'filmes': filmes})

def filme_detail(request, year, month, day, filme):
       filme = get_object_or_404(Filme, slug=filme,
                                      status='published',
                                      publish__year=year,
                                      publish__month=month,
                                      publish__day=day)
       return render(request,
                     'cinema/filme/detail.html',
                     {'filme': filme})

class FilmeListView(APIView):
    serializer_class = FilmeSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Filme.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class FilmeView(APIView):

    def get(self, request, status, format=None):
        user = Filme.objects.get(status=status)
        serializer = FilmeSerializer(user)
        return Response(serializer.data)
