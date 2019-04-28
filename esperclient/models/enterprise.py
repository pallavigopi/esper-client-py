# coding: utf-8

"""
Esper Manage API

OpenAPI spec version: 1.0.0
Contact: developer@esper.io
---------------------------------------------------------

Copyright 2019 Esper, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""



import pprint
import re  # noqa: F401

import six

from esperclient.models.enterprise_detail import EnterpriseDetail  # noqa: F401,E501
from esperclient.models.google_enterprise import GoogleEnterprise  # noqa: F401,E501


class Enterprise(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'url': 'str',
        'name': 'str',
        'display_name': 'str',
        'short_code': 'str',
        'mdm_service': 'int',
        'details': 'EnterpriseDetail',
        'default_policy': 'int',
        'emm': 'GoogleEnterprise',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'is_active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'name': 'name',
        'display_name': 'display_name',
        'short_code': 'short_code',
        'mdm_service': 'mdm_service',
        'details': 'details',
        'default_policy': 'default_policy',
        'emm': 'emm',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'is_active': 'is_active'
    }

    def __init__(self, id=None, url=None, name=None, display_name=None, short_code=None, mdm_service=None, details=None, default_policy=None, emm=None, created_on=None, updated_on=None, is_active=None):  # noqa: E501
        """Enterprise - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self._name = None
        self._display_name = None
        self._short_code = None
        self._mdm_service = None
        self._details = None
        self._default_policy = None
        self._emm = None
        self._created_on = None
        self._updated_on = None
        self._is_active = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        self.name = name
        if display_name is not None:
            self.display_name = display_name
        self.short_code = short_code
        if mdm_service is not None:
            self.mdm_service = mdm_service
        self.details = details
        if default_policy is not None:
            self.default_policy = default_policy
        if emm is not None:
            self.emm = emm
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if is_active is not None:
            self.is_active = is_active

    @property
    def id(self):
        """Gets the id of this Enterprise.  # noqa: E501

        Enterprise id  # noqa: E501

        :return: The id of this Enterprise.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Enterprise.

        Enterprise id  # noqa: E501

        :param id: The id of this Enterprise.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this Enterprise.  # noqa: E501


        :return: The url of this Enterprise.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Enterprise.


        :param url: The url of this Enterprise.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this Enterprise.  # noqa: E501


        :return: The name of this Enterprise.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Enterprise.


        :param name: The name of this Enterprise.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Enterprise.  # noqa: E501


        :return: The display_name of this Enterprise.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Enterprise.


        :param display_name: The display_name of this Enterprise.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 50:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `50`")  # noqa: E501
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def short_code(self):
        """Gets the short_code of this Enterprise.  # noqa: E501


        :return: The short_code of this Enterprise.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this Enterprise.


        :param short_code: The short_code of this Enterprise.  # noqa: E501
        :type: str
        """
        if short_code is None:
            raise ValueError("Invalid value for `short_code`, must not be `None`")  # noqa: E501
        if short_code is not None and len(short_code) > 10:
            raise ValueError("Invalid value for `short_code`, length must be less than or equal to `10`")  # noqa: E501
        if short_code is not None and len(short_code) < 1:
            raise ValueError("Invalid value for `short_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._short_code = short_code

    @property
    def mdm_service(self):
        """Gets the mdm_service of this Enterprise.  # noqa: E501


        :return: The mdm_service of this Enterprise.  # noqa: E501
        :rtype: int
        """
        return self._mdm_service

    @mdm_service.setter
    def mdm_service(self, mdm_service):
        """Sets the mdm_service of this Enterprise.


        :param mdm_service: The mdm_service of this Enterprise.  # noqa: E501
        :type: int
        """

        self._mdm_service = mdm_service

    @property
    def details(self):
        """Gets the details of this Enterprise.  # noqa: E501


        :return: The details of this Enterprise.  # noqa: E501
        :rtype: EnterpriseDetail
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Enterprise.


        :param details: The details of this Enterprise.  # noqa: E501
        :type: EnterpriseDetail
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    @property
    def default_policy(self):
        """Gets the default_policy of this Enterprise.  # noqa: E501

        Policy associated with enteprise  # noqa: E501

        :return: The default_policy of this Enterprise.  # noqa: E501
        :rtype: int
        """
        return self._default_policy

    @default_policy.setter
    def default_policy(self, default_policy):
        """Sets the default_policy of this Enterprise.

        Policy associated with enteprise  # noqa: E501

        :param default_policy: The default_policy of this Enterprise.  # noqa: E501
        :type: int
        """

        self._default_policy = default_policy

    @property
    def emm(self):
        """Gets the emm of this Enterprise.  # noqa: E501


        :return: The emm of this Enterprise.  # noqa: E501
        :rtype: GoogleEnterprise
        """
        return self._emm

    @emm.setter
    def emm(self, emm):
        """Sets the emm of this Enterprise.


        :param emm: The emm of this Enterprise.  # noqa: E501
        :type: GoogleEnterprise
        """

        self._emm = emm

    @property
    def created_on(self):
        """Gets the created_on of this Enterprise.  # noqa: E501


        :return: The created_on of this Enterprise.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Enterprise.


        :param created_on: The created_on of this Enterprise.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this Enterprise.  # noqa: E501


        :return: The updated_on of this Enterprise.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this Enterprise.


        :param updated_on: The updated_on of this Enterprise.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def is_active(self):
        """Gets the is_active of this Enterprise.  # noqa: E501


        :return: The is_active of this Enterprise.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Enterprise.


        :param is_active: The is_active of this Enterprise.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Enterprise, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Enterprise):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
