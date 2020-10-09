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

from esperclient.models.group_command_args import GroupCommandArgs
from esperclient.models.group_command_enum import GroupCommandEnum


class GroupCommandRequest(object):
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
        'command_args': 'GroupCommandArgs',
        'command': 'GroupCommandEnum'
    }

    attribute_map = {
        'command_args': 'command_args',
        'command': 'command'
    }

    def __init__(self, command_args=None, command=None):
        """GroupCommandRequest - a model defined in Swagger"""

        self._command_args = None
        self._command = None
        self.discriminator = None

        if command_args is not None:
            self.command_args = command_args
        self.command = command

    @property
    def command_args(self):
        """Gets the command_args of this GroupCommandRequest.


        :return: The command_args of this GroupCommandRequest.
        :rtype: GroupCommandArgs
        """
        return self._command_args

    @command_args.setter
    def command_args(self, command_args):
        """Sets the command_args of this GroupCommandRequest.


        :param command_args: The command_args of this GroupCommandRequest.
        :type: GroupCommandArgs
        """

        self._command_args = command_args

    @property
    def command(self):
        """Gets the command of this GroupCommandRequest.


        :return: The command of this GroupCommandRequest.
        :rtype: GroupCommandEnum
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this GroupCommandRequest.


        :param command: The command of this GroupCommandRequest.
        :type: GroupCommandEnum
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")

        self._command = command

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
        if issubclass(GroupCommandRequest, dict):
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
        if not isinstance(other, GroupCommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
