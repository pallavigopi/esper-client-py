# coding: utf-8

"""
    Esper Manage API

    # Introduction Esper Manage APIs for Cloud are a set of REST-based APIs that help you programmatically control and monitor your enterprise's dedicated Esper endpoint. Using these APIs, one can orchestrate & manage devices that have been provisioned against your endpoint. Furthermore, this API allows you to manage android applications that get installed on such devices. To read more about the various capabilities of Esper endpoints and Esper managed devices, please visit [esper.io](https://esper.io). This guide describes all the available APIs in detail, along with code samples for you to quickly ramp up to using them.  You can find out more about Esper at [https://esper.io](https://esper.io)  We've done our best to keep this document up to date, but if you find any issues, please reach out to us at developer@esper.io.  # SDK    You are welcome to use your favorite HTTP/REST library for your programming language in order to use these APIs, or you can use our official SDK (currently available in [python](https://github.com/esper-io/esper-client-py)) to do so.   # Authentication Client needs to send authentication details to access APIs. Following authentication schemes are supported:  #### Basic Authentication Client can use username and password to authenticate. These are your developer account credentials. For example, the client sends HTTP requests with the Authorization header that contains the word `Basic` followed by a space and a base64-encoded string `username:password`. ##### Base64 encoding Bash  ``` echo 'username:password' | base64 ```  Powershell  ``` [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes(\"username:password\")) ```  **Example request** ```bash curl -X GET \\   https://DOMAIN.shoonyacloud.com/api/enterprise/<enterprise_id>/device/ \\   -H 'Authorization: Basic cl0ZWFkbWluOnNpdG1pbjEyMyQ=' \\   -H 'Content-Type: application/json' \\ ``` You can read more about basic authentication scheme  [here](https://swagger.io/docs/specification/authentication/basic-authentication/)  # Errors The API uses standard HTTP status codes to indicate success or failure. All error responses will have a JSON body in the following format  ``` {   \"errors\": [],   \"message\": \"error message\",   \"status\": 400 } ``` * `errors` -  List of error details * `message` - Error description * `status` - HTTP status code   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@esper.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from esperclient.api_client import ApiClient


class ApplicationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete(self, application_id, enterprise_id, **kwargs):  # noqa: E501
        """Delete an application  # noqa: E501

        Empty response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_with_http_info(application_id, enterprise_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_with_http_info(application_id, enterprise_id, **kwargs)  # noqa: E501
            return data

    def delete_with_http_info(self, application_id, enterprise_id, **kwargs):  # noqa: E501
        """Delete an application  # noqa: E501

        Empty response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_with_http_info(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'enterprise_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `delete`")  # noqa: E501
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']  # noqa: E501
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_security']  # noqa: E501

        return self.api_client.call_api(
            '/enterprise/{enterprise_id}/application/{application_id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_app_version(self, version_id, application_id, enterprise_id, **kwargs):  # noqa: E501
        """Delete app version  # noqa: E501

        Empty response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_app_version(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_app_version_with_http_info(version_id, application_id, enterprise_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_app_version_with_http_info(version_id, application_id, enterprise_id, **kwargs)  # noqa: E501
            return data

    def delete_app_version_with_http_info(self, version_id, application_id, enterprise_id, **kwargs):  # noqa: E501
        """Delete app version  # noqa: E501

        Empty response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_app_version_with_http_info(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version_id', 'application_id', 'enterprise_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_app_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `delete_app_version`")  # noqa: E501
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `delete_app_version`")  # noqa: E501
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `delete_app_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']  # noqa: E501
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get(self, application_id, enterprise_id, **kwargs):  # noqa: E501
        """Get application information  # noqa: E501

        Returns Application instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_with_http_info(application_id, enterprise_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_with_http_info(application_id, enterprise_id, **kwargs)  # noqa: E501
            return data

    def get_with_http_info(self, application_id, enterprise_id, **kwargs):  # noqa: E501
        """Get application information  # noqa: E501

        Returns Application instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_with_http_info(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'enterprise_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `get`")  # noqa: E501
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']  # noqa: E501
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_security']  # noqa: E501

        return self.api_client.call_api(
            '/enterprise/{enterprise_id}/application/{application_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Application',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_app_version(self, version_id, application_id, enterprise_id, **kwargs):  # noqa: E501
        """Get app version information  # noqa: E501

        Returns AppVersion instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_app_version(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: AppVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_app_version_with_http_info(version_id, application_id, enterprise_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_app_version_with_http_info(version_id, application_id, enterprise_id, **kwargs)  # noqa: E501
            return data

    def get_app_version_with_http_info(self, version_id, application_id, enterprise_id, **kwargs):  # noqa: E501
        """Get app version information  # noqa: E501

        Returns AppVersion instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_app_version_with_http_info(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: AppVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version_id', 'application_id', 'enterprise_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `get_app_version`")  # noqa: E501
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `get_app_version`")  # noqa: E501
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_app_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']  # noqa: E501
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']  # noqa: E501
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_security']  # noqa: E501

        return self.api_client.call_api(
            '/enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_app_versions(self, application_id, enterprise_id, **kwargs):  # noqa: E501
        """List App versions  # noqa: E501

        Returns AppVersion list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_app_versions(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str version_code: filter by version code
        :param str build_number: filter by build number
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_app_versions_with_http_info(application_id, enterprise_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_app_versions_with_http_info(application_id, enterprise_id, **kwargs)  # noqa: E501
            return data

    def get_app_versions_with_http_info(self, application_id, enterprise_id, **kwargs):  # noqa: E501
        """List App versions  # noqa: E501

        Returns AppVersion list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_app_versions_with_http_info(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str version_code: filter by version code
        :param str build_number: filter by build number
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'enterprise_id', 'version_code', 'build_number', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_versions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `get_app_versions`")  # noqa: E501
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_app_versions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']  # noqa: E501
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']  # noqa: E501

        query_params = []
        if 'version_code' in params:
            query_params.append(('version_code', params['version_code']))  # noqa: E501
        if 'build_number' in params:
            query_params.append(('build_number', params['build_number']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_security']  # noqa: E501

        return self.api_client.call_api(
            '/enterprise/{enterprise_id}/application/{application_id}/version/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, enterprise_id, **kwargs):  # noqa: E501
        """List apps in enterprise  # noqa: E501

        Returns Application list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str application_name: filter by application name
        :param str package_name: filter by package name
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_with_http_info(enterprise_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(enterprise_id, **kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, enterprise_id, **kwargs):  # noqa: E501
        """List apps in enterprise  # noqa: E501

        Returns Application list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str application_name: filter by application name
        :param str package_name: filter by package name
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'application_name', 'package_name', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']  # noqa: E501

        query_params = []
        if 'application_name' in params:
            query_params.append(('application_name', params['application_name']))  # noqa: E501
        if 'package_name' in params:
            query_params.append(('package_name', params['package_name']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_security']  # noqa: E501

        return self.api_client.call_api(
            '/enterprise/{enterprise_id}/application/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)