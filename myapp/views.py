from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HomeSerializer, StatusSerializer, NoticeSerializer
from .models import Home, Status, Notice
from rest_framework.views import APIView
from rest_framework import status
import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder


class noticeList(APIView):
    # 게시물 생성 post
    def post(self, request, format = None):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    # 게시물 조회 get
    def get(self, request, format = None):
        queryset = Notice.objects.all()
        serializer = NoticeSerializer(queryset, many = True)
        return Response(serializer.data)

class homeList(APIView):
    def post(self, request):
        serializer = HomeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        queryset = Home.objects.all()
        serializer = HomeSerializer(queryset, many = True)
        return Response(serializer.data)
"""

class homeDetail(APIView):
    def get_object(self, addr):
        return Home.objects.filter(address=addr)

    def get(self, request, addr):
        home = self.get_object(addr)
        res = []
        for info in vmInfoes.values():
            tmp = info
            res.append(tmp)
        result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")

"""
