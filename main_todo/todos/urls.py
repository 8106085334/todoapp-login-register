from django.urls import path
from .import views
urlpatterns = [
    #adding tasks 
    path('addTask/',views.addTask,name="addTask"),
    # Mark as Read
    path('mark_as_read/<int:pk>/',views.mark_as_read,name='mark_as_read'),
    # Mark as UnDone
    path('mark_as_undone/<int:pk>',views.mark_as_undone,name='mark_as_undone'),

    #Edit Feature
    path('editTask/<int:pk>/',views.edit_Task,name='editTask'),

    # Delete Feature 
      path('DeleteTask/<int:pk>/',views.Delete_Task,name='DeleteTask'),
]
