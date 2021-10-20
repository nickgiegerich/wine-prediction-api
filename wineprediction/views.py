from .apps import WinepredictionConfig
from django.http import JsonResponse

import pandas as pd
import numpy as np

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from wineprediction.serializers import WineSerializer


# Create your views here.

class WinePredictionView(APIView):
    """
        for posting data to our machine learning algorithm(s)

        takes in data in the form of a JSON request. 

        EX:

        {
            "fixed_acidity": 7.4,
            "volatile_acidity": 0.700,
            "citric_acid": 0.00,
            "residual_sugar": 1.9,
            "chlorides": 0.076,
            "free_sulfur_dioxide": 11.0,
            "total_sulfur_dioxide": 34.0,
            "density": 0.99780,
            "ph": 3.51,
            "sulphates": 0.56,
            "alcohol": 9.4
        }

        this will give a response of quality after being run through the prediction algorithm

        EX: 

        {"quality": [0]}

        """
    def post(self, request):
    
        serializer = WineSerializer(data=request.data)
        
        if serializer.is_valid():
            df = pd.DataFrame([serializer.data])
            if serializer.data['model_to_run']:
                prediction = WinepredictionConfig.rf.predict(np.array(df.drop('model_to_run', axis=1))).tolist()
                prediction_prob = WinepredictionConfig.rf.predict_proba(np.array(df.drop('model_to_run', axis=1)))[0,:].tolist()
            else:
                prediction = WinepredictionConfig.knn.predict(np.array(df.drop('model_to_run', axis=1))).tolist()
                prediction_prob = WinepredictionConfig.knn.predict_proba(np.array(df.drop('model_to_run', axis=1)))[0,:].tolist()
            response = {'quality': prediction, 'confidence': prediction_prob}
            return JsonResponse(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)