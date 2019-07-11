# coding: utf-8

"""
Esper APIs

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


class DeviceAppPermission(object):
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
        'permission': 'str',
        'grant_state': 'str',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'is_active': 'bool',
        'app': 'str'
    }

    attribute_map = {
        'id': 'id',
        'permission': 'permission',
        'grant_state': 'grant_state',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'is_active': 'is_active',
        'app': 'app'
    }

    def __init__(self, id=None, permission=None, grant_state=None, created_on=None, updated_on=None, is_active=None, app=None):
        """DeviceAppPermission - a model defined in Swagger"""

        self._id = None
        self._permission = None
        self._grant_state = None
        self._created_on = None
        self._updated_on = None
        self._is_active = None
        self._app = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.permission = permission
        if grant_state is not None:
            self.grant_state = grant_state
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if is_active is not None:
            self.is_active = is_active
        if app is not None:
            self.app = app

    @property
    def id(self):
        """Gets the id of this DeviceAppPermission.


        :return: The id of this DeviceAppPermission.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceAppPermission.


        :param id: The id of this DeviceAppPermission.
        :type: str
        """

        self._id = id

    @property
    def permission(self):
        """Gets the permission of this DeviceAppPermission.


        :return: The permission of this DeviceAppPermission.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this DeviceAppPermission.


        :param permission: The permission of this DeviceAppPermission.
        :type: str
        """
        if permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")
        if permission is not None and len(permission) > 255:
            raise ValueError("Invalid value for `permission`, length must be less than or equal to `255`")
        if permission is not None and len(permission) < 1:
            raise ValueError("Invalid value for `permission`, length must be greater than or equal to `1`")

        self._permission = permission

    @property
    def grant_state(self):
        """Gets the grant_state of this DeviceAppPermission.

        * PERMISSION_GRANT_STATE_DEFAULT = 0 * PERMISSION_GRANT_STATE_DENIED = 1 * PERMISSION_GRANT_STATE_GRANTED = 2  For state details check [Android docs](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PERMISSION_GRANT_STATE_DEFAULT) 

        :return: The grant_state of this DeviceAppPermission.
        :rtype: str
        """
        return self._grant_state

    @grant_state.setter
    def grant_state(self, grant_state):
        """Sets the grant_state of this DeviceAppPermission.

        * PERMISSION_GRANT_STATE_DEFAULT = 0 * PERMISSION_GRANT_STATE_DENIED = 1 * PERMISSION_GRANT_STATE_GRANTED = 2  For state details check [Android docs](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PERMISSION_GRANT_STATE_DEFAULT) 

        :param grant_state: The grant_state of this DeviceAppPermission.
        :type: str
        """
        allowed_values = ["PERMISSION_GRANT_STATE_DEFAULT", "PERMISSION_GRANT_STATE_DENIED", "PERMISSION_GRANT_STATE_GRANTED"]
        if grant_state not in allowed_values:
            raise ValueError(
                "Invalid value for `grant_state` ({0}), must be one of {1}"
                .format(grant_state, allowed_values)
            )

        self._grant_state = grant_state

    @property
    def created_on(self):
        """Gets the created_on of this DeviceAppPermission.


        :return: The created_on of this DeviceAppPermission.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeviceAppPermission.


        :param created_on: The created_on of this DeviceAppPermission.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this DeviceAppPermission.


        :return: The updated_on of this DeviceAppPermission.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this DeviceAppPermission.


        :param updated_on: The updated_on of this DeviceAppPermission.
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def is_active(self):
        """Gets the is_active of this DeviceAppPermission.


        :return: The is_active of this DeviceAppPermission.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this DeviceAppPermission.


        :param is_active: The is_active of this DeviceAppPermission.
        :type: bool
        """

        self._is_active = is_active

    @property
    def app(self):
        """Gets the app of this DeviceAppPermission.


        :return: The app of this DeviceAppPermission.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this DeviceAppPermission.


        :param app: The app of this DeviceAppPermission.
        :type: str
        """

        self._app = app

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
        if issubclass(DeviceAppPermission, dict):
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
        if not isinstance(other, DeviceAppPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other