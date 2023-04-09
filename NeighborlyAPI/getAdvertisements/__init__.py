import os

import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

from variables import MongoDBConnString, MongoDBName


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        url = MongoDBConnString
        client = pymongo.MongoClient(url)
        database = client[MongoDBName]
        collection = database['advertisements']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)
