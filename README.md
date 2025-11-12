# File Uploader

A proof-of-concept project built with Python, Azure Functions, and Azure Blob Storage. This application allows users to upload multiple PDF and Excel files securely to Azure Storage via a serverless HTTP endpoint.

## Features

- Upload multiple files in a single request
- Supports PDF (`.pdf`) and Excel (`.xlsx`, `.xls`) file formats
- Each file is validated and stored in separate containers by type
- Generates a unique name for each file to avoid conflicts
- Built with Azure Functions for scalable, serverless operation

## Requirements

- [Python 3.8, 3.9, 3.10, or 3.11](https://www.python.org/downloads/)
- [Azure Functions Core Tools v4](https://www.npmjs.com/package/azure-functions-core-tools)
- [Microsoft Azure account](https://azure.microsoft.com/en-us/get-started/azure-portal/) (required to create Azure Storage and deploy Azure Functions)

## Project Structure

```
file-uploader/
├── function_app.py     # Main Azure Function entry point and logic
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/itsronalds/file-uploader
cd file-uploader
```

### Create Virtual Environment

#### Windows

```bash
py -3 -m venv .venv
```

#### macOS/Linux

```bash
python3 -m venv .venv
```

### Activate/Deactivate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
# To deactivate
deactivate
```

#### macOS/Linux

```bash
source .venv/bin/activate
# To deactivate
deactivate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project Locally

1. Set the `AZURE_STORAGE_CONNECTION_STRING` environment variable with your Azure Storage account connection string.
2. Start the Azure Functions host:

```bash
func start
```

The HTTP endpoint (default: `http://localhost:7071/api/uploader`) will be available for file uploads.

## Usage

Send a `POST` request to the `/uploader` endpoint with files attached as form data. Only PDF and Excel files are accepted. Unsupported file types will be rejected.

Example with `curl`:

```bash
curl -X POST http://localhost:7071/api/uploader \
  -F "file1=@example.pdf" \
  -F "file2=@example.xlsx"
```

## Deployment

To deploy to Azure:

1. Create an Azure Storage account and an Azure Function App.
2. Configure the Function App's application settings with `AZURE_STORAGE_CONNECTION_STRING`.
3. Publish the code to Azure using Azure Functions Core Tools:

```bash
func azure functionapp publish <YOUR_FUNCTION_APP_NAME>
```
