import logging

import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

def main(req: func.HttpRequest, inputDocument: func.DocumentList, outputDoc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    counter = inputDocument[0]['usersCounter'] + 1
    inputDocument[0]['usersCounter'] = counter
    test = inputDocument[0].to_json()
    outputDoc.set(func.Document.from_json(inputDocument[0].to_json()))
    if counter:
        return func.HttpResponse(f"{counter}", status_code=200)
    else:
        return func.HttpResponse(
             "Error",
             status_code=500
        )
