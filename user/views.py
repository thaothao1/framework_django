# from django.shortcuts import render
# from . import serializers
# from rest_framework.response import Response
# from django.http import JsonResponse
# from rest_framework.views import APIView

# # Create your views here.
# class UserRegister(APIView):
#     def post (self , request):
#         serializer = serializers.UserSerializer(data= request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response(serializer.data)


