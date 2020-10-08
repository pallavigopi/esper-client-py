# coding: utf-8

"""
ESPER API REFERENCE

OpenAPI spec version: 1.0.0
Contact: developer@esper.io
---------------------------------------------------------

Copyright 2019 Shoonya Enterprises Inc.

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
import re

import six


class TokenRenewV0(object):
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
        'user': 'str',
        'enterprise': 'str',
        'token': 'str',
        'expires_at': 'datetime',
        'developerapp': 'str',
        'scope': 'str',
        'created_on': 'datetime',
        'updated_on': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'enterprise': 'enterprise',
        'token': 'token',
        'expires_at': 'expires_at',
        'developerapp': 'developerapp',
        'scope': 'scope',
        'created_on': 'created_on',
        'updated_on': 'updated_on'
    }

    def __init__(self, id=None, user=None, enterprise=None, token=None, expires_at=None, developerapp=None, scope=None, created_on=None, updated_on=None):
        """TokenRenewV0 - a model defined in Swagger"""

        self._id = None
        self._user = None
        self._enterprise = None
        self._token = None
        self._expires_at = None
        self._developerapp = None
        self._scope = None
        self._created_on = None
        self._updated_on = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if enterprise is not None:
            self.enterprise = enterprise
        if token is not None:
            self.token = token
        if expires_at is not None:
            self.expires_at = expires_at
        if developerapp is not None:
            self.developerapp = developerapp
        if scope is not None:
            self.scope = scope
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on

    @property
    def id(self):
        """Gets the id of this TokenRenewV0.

        Id of the token

        :return: The id of this TokenRenewV0.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TokenRenewV0.

        Id of the token

        :param id: The id of this TokenRenewV0.
        :type: str
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this TokenRenewV0.

        Id of the user resource

        :return: The user of this TokenRenewV0.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TokenRenewV0.

        Id of the user resource

        :param user: The user of this TokenRenewV0.
        :type: str
        """

        self._user = user

    @property
    def enterprise(self):
        """Gets the enterprise of this TokenRenewV0.

        Id of the enterprise resource

        :return: The enterprise of this TokenRenewV0.
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this TokenRenewV0.

        Id of the enterprise resource

        :param enterprise: The enterprise of this TokenRenewV0.
        :type: str
        """

        self._enterprise = enterprise

    @property
    def token(self):
        """Gets the token of this TokenRenewV0.

        API token for accessing esper APIs

        :return: The token of this TokenRenewV0.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TokenRenewV0.

        API token for accessing esper APIs

        :param token: The token of this TokenRenewV0.
        :type: str
        """

        self._token = token

    @property
    def expires_at(self):
        """Gets the expires_at of this TokenRenewV0.

        Date and time of when your API token will get expired

        :return: The expires_at of this TokenRenewV0.
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this TokenRenewV0.

        Date and time of when your API token will get expired

        :param expires_at: The expires_at of this TokenRenewV0.
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def developerapp(self):
        """Gets the developerapp of this TokenRenewV0.

        Id of the developer app resource that you created using the esper dev console

        :return: The developerapp of this TokenRenewV0.
        :rtype: str
        """
        return self._developerapp

    @developerapp.setter
    def developerapp(self, developerapp):
        """Sets the developerapp of this TokenRenewV0.

        Id of the developer app resource that you created using the esper dev console

        :param developerapp: The developerapp of this TokenRenewV0.
        :type: str
        """

        self._developerapp = developerapp

    @property
    def scope(self):
        """Gets the scope of this TokenRenewV0.

        This defines what access scopes your API token has

        :return: The scope of this TokenRenewV0.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this TokenRenewV0.

        This defines what access scopes your API token has

        :param scope: The scope of this TokenRenewV0.
        :type: str
        """

        self._scope = scope

    @property
    def created_on(self):
        """Gets the created_on of this TokenRenewV0.

        Date and time of when this resource was created

        :return: The created_on of this TokenRenewV0.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this TokenRenewV0.

        Date and time of when this resource was created

        :param created_on: The created_on of this TokenRenewV0.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this TokenRenewV0.

        Date and time of when this resource was updated

        :return: The updated_on of this TokenRenewV0.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this TokenRenewV0.

        Date and time of when this resource was updated

        :param updated_on: The updated_on of this TokenRenewV0.
        :type: datetime
        """

        self._updated_on = updated_on

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
        if issubclass(TokenRenewV0, dict):
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
        if not isinstance(other, TokenRenewV0):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other