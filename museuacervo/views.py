# coding: utf-8

from django.shortcuts import render

from .models import DadosPessoais
from .serializer import DadosPessoaisSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


def museuacervo_exibir(request):

    pessoa = DadosPessoais.objects.all()
    context = {'pessoa': pessoa}
    return render(request, 'museuacervo/museuacervo_exibir.html', context)


class DadosPessoaisViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all()
    serializer_class = DadosPessoaisSerializer

'''
class PortfolioListView(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class PortfolioView(APIView):

    def get(self, request, pk, format=None):
        user = DadosPessoais.objects.get(pk=pk)
        serializer = DadosPessoaisSerializer(user)
        return Response(serializer.data)
'''