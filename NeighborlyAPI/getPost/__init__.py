import os

import azure.functions as func
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId

from variables import MongoDBConnString, MongoDBName


def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.params.get('id')

    if id:
        try:
            url = MongoDBConnString
            client = pymongo.MongoClient(url)
            database = client[MongoDBName]
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
