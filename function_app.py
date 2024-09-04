import azure.functions as func
import logging
import base64
import random
import os

from azure.storage.blob import BlobServiceClient
from werkzeug.datastructures import MultiDict, FileStorage
from time import time

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


def get_blob_name(file: FileStorage) -> str:
    # get file extension
    file_ext = str(file.filename).split('/')[-1]

    # generate a unique identifier
    identifier = ''.join([str(random.randint(1, 10)) for _ in range(5)])

    # generate a unique name for the blob
    filename_bytes = base64.b64encode(
        str(file.filename).encode('utf-8')).decode('utf-8')

    # generate a unique name for the blob
    unique_identifier = f'{identifier}{int(time())}{filename_bytes}.{file_ext}'

    return unique_identifier


def upload_pdf(file: FileStorage):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            os.environ["AZURE_STORAGE_CONNECTION_STRING"])
        container_name = "pdf"
        container_client = blob_service_client.get_container_client(
            container_name)
        blob_client = container_client.get_blob_client(get_blob_name(file))
        blob_client.upload_blob(file.stream)
        return True
    except Exception as e:
        logging.error(str(e))
        return False


def upload_excel(file: FileStorage):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            os.environ["AZURE_STORAGE_CONNECTION_STRING"])
        container_name = "excel"
        container_client = blob_service_client.get_container_client(
            container_name)
        blob_client = container_client.get_blob_client(get_blob_name(file))
        blob_client.upload_blob(file.stream)
        return True
    except Exception as e:
        logging.error(str(e))
        return False


@app.route(route="uploader")
def uploader(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == 'POST':
        files: MultiDict[str, FileStorage] = req.files  # type: ignore

        if not len(files):
            return func.HttpResponse("No file uploaded", status_code=400)

        # validate only pdf and excel files
        available_extensions = ['pdf', 'xlsx', 'xls']

        # check if all files are allowed
        for file in files.values():
            file_ext = str(file.filename).split('.')[-1]

            if file_ext not in available_extensions:
                return func.HttpResponse(f"File {file.filename} is not allowed", status_code=400)

        # upload files to blob storage
        for file in files.values():
            file_ext = str(file.filename).split('.')[-1]

            if file_ext == 'pdf':
                upload_pdf(file)
            elif file_ext in ['xlsx', 'xls']:
                upload_excel(file)

        return func.HttpResponse("Files uploaded successfully", status_code=200)
    else:
        return func.HttpResponse("Method not allowed", status_code=405)
