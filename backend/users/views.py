from django.shortcuts import render
from rest_framework import generics 

from users.models import Objective, CustomUser 
from users.serializers import ObjectiveSerializer
# Create your views here.

class ObjectivesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer 

    def perform_create(self, serializer):
        user = self.request.user; 
        serializer.save(
            user = user 
        )

class ObjectiveRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer 


class UserObjectives(generics.ListAPIView):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer 

    def get_queryset(self):
        username = self.kwargs.get('username')

        return Objective.objects.filter(user__username=username)
