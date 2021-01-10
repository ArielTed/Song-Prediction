from django.urls import path
import Prediction.views as views

urlpatterns = [
  path('predict/', views.Song_Model_Predict.as_view(), name = 'predict'),
]
