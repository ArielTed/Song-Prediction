from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .apps import PredictionConfig
import pandas as pd

class Song_Model_Predict(APIView):
    def post(self, request, format=None):
        data = request.data
        keys = []
        values = []
        for key in data:
            keys.append(key)
            values.append(data[key])
        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_dim_reduction = PredictionConfig.dim_reduction
        X_reduc = loaded_dim_reduction.transform(X)
        loaded_classifier = PredictionConfig.classifier
        y_pred = loaded_classifier.predict(X_reduc)
        y_pred = pd.Series(y_pred)
        response_dict = {"Predicted year": y_pred[0]}
        return Response(response_dict, status=200)
