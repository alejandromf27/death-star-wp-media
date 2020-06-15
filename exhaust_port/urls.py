from django.urls import path
from exhaust_port.wing_views import XWingList
from exhaust_port.tower_views import DefenceTowerView

urlpatterns = [
    path('x_wings/', XWingList.as_view()),
    path('towers/', DefenceTowerView.as_view()),
]
