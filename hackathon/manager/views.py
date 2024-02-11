from django.http import HttpResponse
from rest_framework import generics
# from .models import Manager
# from .serializers import ManagerSerializer


def index(request):
    return HttpResponse("Hello, world.")




# # Create your views here.
class ManagerList(generics.ListCreateAPIView):
    pass
    # queryset = Manager.objects.all()
    # serializer_class = ManagerSerializer