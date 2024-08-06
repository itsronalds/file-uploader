# file-uploader

Proof of concept using Python with Azure Function and Azure Storage for uploading multiple PDF and Excel files.

## Requirements

- [Python v3.8, v.3.9, v3.10 or v3.11](https://www.python.org/downloads/)
- [Azure Functions Core Tools v4](https://www.npmjs.com/package/azure-functions-core-tools)
- [Microsoft Azure account](https://azure.microsoft.com/en-us/get-started/azure-portal/) is required to create an Azure Storage and Azure Function resource

## Clone Repository

```$
git clone https://github.com/itsronalds/file-uploader
```

## Create Virtual Environment

```$
# First, Let's get to the root of the project
cd file-uploader

# Create virtual environment in Windows
py -3 -m venv .venv 
```

## Activate/Deactivate Virtual Environment

```$
# Activate
.venv\Scripts\Activate

# Deactivate (use it when leaving the project)
.venv\Scripts\Deactivate
```

## Download dependencies
```$
pip install -r requirements.txt
```

## Run Project
```$
func start
```

## Thanks for Reading
