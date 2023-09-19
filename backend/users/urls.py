from django.urls import path 
from users import views 

##### 

urlpatterns = [
    path("objectives/", views.ObjectivesListCreateAPIView.as_view(), name="objectives-list-create"),
    path("objectives/<int:pk>/", views.ObjectiveRetrieveAPIView.as_view(), name="objective-details"),  
    path("user-objectives/<str:username>/", views.UserObjectives.as_view(), name="user-objectives"), 
]