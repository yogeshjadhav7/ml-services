from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.core.cache import cache
from intellecto import Intellecto
import threading
import keras
import numpy as np
import requests
import json

# Create your views here.

host_url = "http://localhost:9000/intellecto/robot"
notify_api_uri = "/notify/train/completion"

def default(o):
    if isinstance(o, np.int64): return int(o)
    raise TypeError

def train_model(behaviourList, userId):
    print("Training model for user " + str(userId))
    I = Intellecto()
    model = I.train(behaviourList=behaviourList, one_hot=True, verbose=1)
    model_saved_path = I.save_model(model=model, userId=userId)
    print("Completed training model for user " + str(userId))

    url = host_url + notify_api_uri
    params = json.dumps({'userId': userId})
    requests.post(url, params, headers={'Content-Type': 'application/json'})


@csrf_exempt
def predict(request):
    I = Intellecto()
    data = json.loads(request.body)
    behaviour = json.loads(data['behaviour'])
    userId = data['userId']
    behaviourMap = behaviour['behaviourMap']

    saved_model = I.get_saved_model(userId=userId)
    I.predict(behaviourMap=behaviourMap, saved_model=saved_model)

    behaviour['behaviourMap'] = behaviourMap

    keras.backend.clear_session()
    return JsonResponse(json.dumps(behaviour, default=default), safe=False)

@csrf_exempt
def train(request):
    I = Intellecto()
    data = json.loads(request.body)
    behaviourList = json.loads(data['behaviour'])
    userId = data['userId']

    trainingThread = threading.Thread(target=train_model, args=(behaviourList, userId,))
    trainingThread.start()

    return JsonResponse(json.dumps(True, default=default), safe=False)