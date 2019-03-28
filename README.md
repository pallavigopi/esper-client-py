# esper
This is a read only Esper SDK.  You can find out more about Esper at [https://shoonya.io](https://shoonya.io).

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 0.0.1
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import esper 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import esper
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import esper
from esper.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic_security
configuration = esper.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esper.CommandsApi(esper.ApiClient(configuration))
body = esper.DeviceCommandRequest() # DeviceCommandRequest | command name to fire
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
device_id = 'device_id_example' # str | ID of the device

try:
    # Run commands on device
    api_response = api_instance.run_command(body, enterprise_id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->run_command: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://127.0.0.1:8000/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CommandsApi* | [**run_command**](docs/CommandsApi.md#run_command) | **POST** /enterprise/{enterprise_id}/device/{device_id}/command/ | Run commands on device
*DeviceApi* | [**get_all_devices**](docs/DeviceApi.md#get_all_devices) | **GET** /enterprise/{enterprise_id}/device/ | Fetch all devices in an enterprise
*DeviceApi* | [**get_device_by_id**](docs/DeviceApi.md#get_device_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/ | Fetch device details by ID

## Documentation For Models

 - [Device](docs/Device.md)
 - [DeviceCommandRequest](docs/DeviceCommandRequest.md)
 - [DeviceCommandResponse](docs/DeviceCommandResponse.md)
 - [DeviceListResponse](docs/DeviceListResponse.md)
 - [EmmDevice](docs/EmmDevice.md)

## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## basic_security

- **Type**: HTTP basic authentication


## Author

developer@shoonya.io
