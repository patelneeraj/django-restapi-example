from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class DeafultView(APIView):

    def post(self, request):
        return Response({"message": f"Hello {request.data['name']}"}, status=200)
