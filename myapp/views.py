from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import HomeSerializer, StatusSerializer, NoticeSerializer
from .models import Home, Status, Notice
from rest_framework.views import APIView
from rest_framework import status
import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import datetime
import pytz



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


    #@csrf_exempt
    #def post(self, request):
    #    serializer = HomeSerializer(data = request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        queryset = Home.objects.all()
        serializer = HomeSerializer(queryset, many = True)
        return Response(serializer.data)


class statusList(APIView):

    def post(self, request):
        serializer = StatusSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        queryset = Status.objects.all()
        serializer = StatusSerializer(queryset, many = True)
        return Response(serializer.data)



class homeDetail(APIView):
    def get(self, request, addr):
        print("connect complete!")
        home = Home.objects.filter(address=addr)
        res = []
        for info in home.values():
            tmp = info
            res.append(tmp)
        result = json.dumps(res, cls=DjangoJSONEncoder)
        return HttpResponse(result, content_type="text/json-comment-filtered")

@api_view(['POST'])
def homeinfo_by_id(request):
    _address = Home.objects.filter(id = request.data['id']).values()[0]['address']
    res = []
    for info in Home.objects.filter(address = _address).values():
        tmp = info
        res.append(tmp)
    result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")



@api_view(['PATCH'])
def update_sensor_time(request):
    _id = request.data['id']
    _start = request.data['sensor_starttime']
    _end = request.data['sensor_endtime']
    Home.objects.filter(id=_id).update(sensor_starttime=_start, sensor_endtime=_end)
    res = []
    for info in Home.objects.filter(id=_id).values():
        tmp = info
        res.append(tmp)
    result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")

@api_view(['POST'])
def sensorData(request):
    Status.objects.create(noise=request.data['sound'], vibration=request.data['vib'], home_id_id=request.data['address'])
    res = []
    tmp = {}
    tmp['success'] = 1
    res.append(tmp)
    result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")


@api_view(['POST'])
def homeinfo_id(request):
    _address = Home.objects.filter(id = request.data['id']).values()[0]['address']
    res = []
    for info in Home.objects.filter(address = _address).values():
        tmp = info
        res.append(tmp)
    result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")

@api_view(['POST'])
def my_meta_id(request):
    res = []
    for info in Home.objects.filter(id = request.data['id']).values():
        tmp = info
        res.append(tmp)
    result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")


@api_view(['POST'])
def above_meta_id(request):
    _above = Home.objects.filter(id=request.data['id']).values()[0]['home_No'] + 100
    res = []
    for info in Home.objects.filter(home_No = _above).values():
        tmp = info
        res.append(tmp)
    result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")



@api_view(['POST'])
def my_sensor_data(request):
    res = []
    for info in Status.objects.filter(home_id_id=request.data['id']).values():
        tmp = info
        res.append(tmp)
    result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")



@api_view(['POST'])
def above_sensor_data(request):
    _above = Home.objects.filter(id=request.data['id']).values()[0]['home_No'] + 100
    _above_id = Home.objects.filter(home_No = _above).values()[0]['id']
    res = []
    for info in Status.objects.filter(home_id_id=_above_id).values():
        tmp = info
        res.append(tmp)
    result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")

@api_view(['POST'])
def message(request):
    _home = Home.objects.filter(id=request.data['id']).update(message = request.data['message'],
                                                              message_starttime = request.data['message_starttime'],
                                                              message_endtime = request.data['message_endtime'])
    res = []
    tmp = {}
    tmp['success'] = 1
    res.append(tmp)
    result = json.dumps(res, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="text/json-comment-filtered")