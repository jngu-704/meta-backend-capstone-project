from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


# class MenuView(APIView):
#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = MenuSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
