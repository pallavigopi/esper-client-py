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

from esperclient.models.command_args import CommandArgs
from esperclient.models.device_command_enum import DeviceCommandEnum


class DeviceCommand(object):
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
        'current_base_uri': 'str',
        'command_args': 'CommandArgs',
        'action': 'str',
        'schedule': 'str',
        'group_schedule_id': 'str',
        'command': 'DeviceCommandEnum',
        'state': 'str',
        'details': 'str',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'enterprise': 'str',
        'device': 'str',
        'group_command': 'str',
        'issued_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'current_base_uri': 'current_base_uri',
        'command_args': 'command_args',
        'action': 'action',
        'schedule': 'schedule',
        'group_schedule_id': 'group_schedule_id',
        'command': 'command',
        'state': 'state',
        'details': 'details',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'enterprise': 'enterprise',
        'device': 'device',
        'group_command': 'group_command',
        'issued_by': 'issued_by'
    }

    def __init__(self, id=None, current_base_uri=None, command_args=None, action=None, schedule=None, group_schedule_id=None, command=None, state=None, details=None, created_on=None, updated_on=None, enterprise=None, device=None, group_command=None, issued_by=None):
        """DeviceCommand - a model defined in Swagger"""

        self._id = None
        self._current_base_uri = None
        self._command_args = None
        self._action = None
        self._schedule = None
        self._group_schedule_id = None
        self._command = None
        self._state = None
        self._details = None
        self._created_on = None
        self._updated_on = None
        self._enterprise = None
        self._device = None
        self._group_command = None
        self._issued_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if current_base_uri is not None:
            self.current_base_uri = current_base_uri
        if command_args is not None:
            self.command_args = command_args
        if action is not None:
            self.action = action
        if schedule is not None:
            self.schedule = schedule
        if group_schedule_id is not None:
            self.group_schedule_id = group_schedule_id
        self.command = command
        if state is not None:
            self.state = state
        if details is not None:
            self.details = details
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        self.enterprise = enterprise
        self.device = device
        if group_command is not None:
            self.group_command = group_command
        if issued_by is not None:
            self.issued_by = issued_by

    @property
    def id(self):
        """Gets the id of this DeviceCommand.


        :return: The id of this DeviceCommand.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceCommand.


        :param id: The id of this DeviceCommand.
        :type: str
        """

        self._id = id

    @property
    def current_base_uri(self):
        """Gets the current_base_uri of this DeviceCommand.


        :return: The current_base_uri of this DeviceCommand.
        :rtype: str
        """
        return self._current_base_uri

    @current_base_uri.setter
    def current_base_uri(self, current_base_uri):
        """Sets the current_base_uri of this DeviceCommand.


        :param current_base_uri: The current_base_uri of this DeviceCommand.
        :type: str
        """
        if current_base_uri is not None and len(current_base_uri) < 1:
            raise ValueError("Invalid value for `current_base_uri`, length must be greater than or equal to `1`")

        self._current_base_uri = current_base_uri

    @property
    def command_args(self):
        """Gets the command_args of this DeviceCommand.


        :return: The command_args of this DeviceCommand.
        :rtype: CommandArgs
        """
        return self._command_args

    @command_args.setter
    def command_args(self, command_args):
        """Sets the command_args of this DeviceCommand.


        :param command_args: The command_args of this DeviceCommand.
        :type: CommandArgs
        """

        self._command_args = command_args

    @property
    def action(self):
        """Gets the action of this DeviceCommand.


        :return: The action of this DeviceCommand.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this DeviceCommand.


        :param action: The action of this DeviceCommand.
        :type: str
        """
        allowed_values = ["acknowledge", "in_progress", "success", "failed"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def schedule(self):
        """Gets the schedule of this DeviceCommand.


        :return: The schedule of this DeviceCommand.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this DeviceCommand.


        :param schedule: The schedule of this DeviceCommand.
        :type: str
        """

        self._schedule = schedule

    @property
    def group_schedule_id(self):
        """Gets the group_schedule_id of this DeviceCommand.


        :return: The group_schedule_id of this DeviceCommand.
        :rtype: str
        """
        return self._group_schedule_id

    @group_schedule_id.setter
    def group_schedule_id(self, group_schedule_id):
        """Sets the group_schedule_id of this DeviceCommand.


        :param group_schedule_id: The group_schedule_id of this DeviceCommand.
        :type: str
        """

        self._group_schedule_id = group_schedule_id

    @property
    def command(self):
        """Gets the command of this DeviceCommand.


        :return: The command of this DeviceCommand.
        :rtype: DeviceCommandEnum
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this DeviceCommand.


        :param command: The command of this DeviceCommand.
        :type: DeviceCommandEnum
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")

        self._command = command

    @property
    def state(self):
        """Gets the state of this DeviceCommand.


        :return: The state of this DeviceCommand.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DeviceCommand.


        :param state: The state of this DeviceCommand.
        :type: str
        """
        allowed_values = ["Command Initiated", "Command Acknowledged", "Command In Progress", "Command TimeOut", "Command Success", "Command Failure", "Command Scheduled"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def details(self):
        """Gets the details of this DeviceCommand.


        :return: The details of this DeviceCommand.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DeviceCommand.


        :param details: The details of this DeviceCommand.
        :type: str
        """

        self._details = details

    @property
    def created_on(self):
        """Gets the created_on of this DeviceCommand.


        :return: The created_on of this DeviceCommand.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeviceCommand.


        :param created_on: The created_on of this DeviceCommand.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this DeviceCommand.


        :return: The updated_on of this DeviceCommand.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this DeviceCommand.


        :param updated_on: The updated_on of this DeviceCommand.
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def enterprise(self):
        """Gets the enterprise of this DeviceCommand.


        :return: The enterprise of this DeviceCommand.
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this DeviceCommand.


        :param enterprise: The enterprise of this DeviceCommand.
        :type: str
        """
        if enterprise is None:
            raise ValueError("Invalid value for `enterprise`, must not be `None`")

        self._enterprise = enterprise

    @property
    def device(self):
        """Gets the device of this DeviceCommand.


        :return: The device of this DeviceCommand.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DeviceCommand.


        :param device: The device of this DeviceCommand.
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")

        self._device = device

    @property
    def group_command(self):
        """Gets the group_command of this DeviceCommand.


        :return: The group_command of this DeviceCommand.
        :rtype: str
        """
        return self._group_command

    @group_command.setter
    def group_command(self, group_command):
        """Sets the group_command of this DeviceCommand.


        :param group_command: The group_command of this DeviceCommand.
        :type: str
        """

        self._group_command = group_command

    @property
    def issued_by(self):
        """Gets the issued_by of this DeviceCommand.


        :return: The issued_by of this DeviceCommand.
        :rtype: str
        """
        return self._issued_by

    @issued_by.setter
    def issued_by(self, issued_by):
        """Sets the issued_by of this DeviceCommand.


        :param issued_by: The issued_by of this DeviceCommand.
        :type: str
        """

        self._issued_by = issued_by

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
        if issubclass(DeviceCommand, dict):
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
        if not isinstance(other, DeviceCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
