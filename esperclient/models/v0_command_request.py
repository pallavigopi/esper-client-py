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

from esperclient.models.v0_command_args import V0CommandArgs
from esperclient.models.v0_command_request_status import V0CommandRequestStatus
from esperclient.models.v0_command_schedule_args import V0CommandScheduleArgs
from esperclient.models.v0_command_schedule_enum import V0CommandScheduleEnum
from esperclient.models.v0_device_command_enum import V0DeviceCommandEnum


class V0CommandRequest(object):
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
        'enterprise': 'str',
        'command_type': 'str',
        'devices': 'list[str]',
        'groups': 'list[str]',
        'device_type': 'str',
        'command': 'V0DeviceCommandEnum',
        'command_args': 'V0CommandArgs',
        'schedule': 'V0CommandScheduleEnum',
        'schedule_args': 'V0CommandScheduleArgs',
        'issued_by': 'str',
        'created_on': 'datetime',
        'status': 'list[V0CommandRequestStatus]'
    }

    attribute_map = {
        'id': 'id',
        'enterprise': 'enterprise',
        'command_type': 'command_type',
        'devices': 'devices',
        'groups': 'groups',
        'device_type': 'device_type',
        'command': 'command',
        'command_args': 'command_args',
        'schedule': 'schedule',
        'schedule_args': 'schedule_args',
        'issued_by': 'issued_by',
        'created_on': 'created_on',
        'status': 'status'
    }

    def __init__(self, id=None, enterprise=None, command_type=None, devices=None, groups=None, device_type='active', command=None, command_args=None, schedule=None, schedule_args=None, issued_by=None, created_on=None, status=None):
        """V0CommandRequest - a model defined in Swagger"""

        self._id = None
        self._enterprise = None
        self._command_type = None
        self._devices = None
        self._groups = None
        self._device_type = None
        self._command = None
        self._command_args = None
        self._schedule = None
        self._schedule_args = None
        self._issued_by = None
        self._created_on = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if enterprise is not None:
            self.enterprise = enterprise
        if command_type is not None:
            self.command_type = command_type
        if devices is not None:
            self.devices = devices
        if groups is not None:
            self.groups = groups
        if device_type is not None:
            self.device_type = device_type
        if command is not None:
            self.command = command
        if command_args is not None:
            self.command_args = command_args
        if schedule is not None:
            self.schedule = schedule
        if schedule_args is not None:
            self.schedule_args = schedule_args
        if issued_by is not None:
            self.issued_by = issued_by
        if created_on is not None:
            self.created_on = created_on
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this V0CommandRequest.

        Unique command request identifier

        :return: The id of this V0CommandRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V0CommandRequest.

        Unique command request identifier

        :param id: The id of this V0CommandRequest.
        :type: str
        """

        self._id = id

    @property
    def enterprise(self):
        """Gets the enterprise of this V0CommandRequest.

        Esper account identifier

        :return: The enterprise of this V0CommandRequest.
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this V0CommandRequest.

        Esper account identifier

        :param enterprise: The enterprise of this V0CommandRequest.
        :type: str
        """

        self._enterprise = enterprise

    @property
    def command_type(self):
        """Gets the command_type of this V0CommandRequest.

        Identifies the type of command  ``` * DEVICE: command request is meant for devices * GROUP: command request is meant for groups * DYNAMIC: command request is meant for dynamic set of devices   i.e subset of devices from different groups or otherwise. ``` 

        :return: The command_type of this V0CommandRequest.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """Sets the command_type of this V0CommandRequest.

        Identifies the type of command  ``` * DEVICE: command request is meant for devices * GROUP: command request is meant for groups * DYNAMIC: command request is meant for dynamic set of devices   i.e subset of devices from different groups or otherwise. ``` 

        :param command_type: The command_type of this V0CommandRequest.
        :type: str
        """
        allowed_values = ["DEVICE", "GROUP", "DYNAMIC"]
        if command_type not in allowed_values:
            raise ValueError(
                "Invalid value for `command_type` ({0}), must be one of {1}"
                .format(command_type, allowed_values)
            )

        self._command_type = command_type

    @property
    def devices(self):
        """Gets the devices of this V0CommandRequest.

        list of devices to run commands

        :return: The devices of this V0CommandRequest.
        :rtype: list[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this V0CommandRequest.

        list of devices to run commands

        :param devices: The devices of this V0CommandRequest.
        :type: list[str]
        """

        self._devices = devices

    @property
    def groups(self):
        """Gets the groups of this V0CommandRequest.

        list of groups to run commands

        :return: The groups of this V0CommandRequest.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this V0CommandRequest.

        list of groups to run commands

        :param groups: The groups of this V0CommandRequest.
        :type: list[str]
        """

        self._groups = groups

    @property
    def device_type(self):
        """Gets the device_type of this V0CommandRequest.

        Type of devices to run commands on  ``` * active: Run commands on currently online devices * inactive: Run commands on currently offline devices * all: Run commands on all the devices.   Commands will be queued for offline devices until they come back online. ``` 

        :return: The device_type of this V0CommandRequest.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this V0CommandRequest.

        Type of devices to run commands on  ``` * active: Run commands on currently online devices * inactive: Run commands on currently offline devices * all: Run commands on all the devices.   Commands will be queued for offline devices until they come back online. ``` 

        :param device_type: The device_type of this V0CommandRequest.
        :type: str
        """
        allowed_values = ["active", "inactive", "all"]
        if device_type not in allowed_values:
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def command(self):
        """Gets the command of this V0CommandRequest.


        :return: The command of this V0CommandRequest.
        :rtype: V0DeviceCommandEnum
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this V0CommandRequest.


        :param command: The command of this V0CommandRequest.
        :type: V0DeviceCommandEnum
        """

        self._command = command

    @property
    def command_args(self):
        """Gets the command_args of this V0CommandRequest.


        :return: The command_args of this V0CommandRequest.
        :rtype: V0CommandArgs
        """
        return self._command_args

    @command_args.setter
    def command_args(self, command_args):
        """Sets the command_args of this V0CommandRequest.


        :param command_args: The command_args of this V0CommandRequest.
        :type: V0CommandArgs
        """

        self._command_args = command_args

    @property
    def schedule(self):
        """Gets the schedule of this V0CommandRequest.


        :return: The schedule of this V0CommandRequest.
        :rtype: V0CommandScheduleEnum
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this V0CommandRequest.


        :param schedule: The schedule of this V0CommandRequest.
        :type: V0CommandScheduleEnum
        """

        self._schedule = schedule

    @property
    def schedule_args(self):
        """Gets the schedule_args of this V0CommandRequest.


        :return: The schedule_args of this V0CommandRequest.
        :rtype: V0CommandScheduleArgs
        """
        return self._schedule_args

    @schedule_args.setter
    def schedule_args(self, schedule_args):
        """Sets the schedule_args of this V0CommandRequest.


        :param schedule_args: The schedule_args of this V0CommandRequest.
        :type: V0CommandScheduleArgs
        """

        self._schedule_args = schedule_args

    @property
    def issued_by(self):
        """Gets the issued_by of this V0CommandRequest.

        command is issued by this user

        :return: The issued_by of this V0CommandRequest.
        :rtype: str
        """
        return self._issued_by

    @issued_by.setter
    def issued_by(self, issued_by):
        """Sets the issued_by of this V0CommandRequest.

        command is issued by this user

        :param issued_by: The issued_by of this V0CommandRequest.
        :type: str
        """

        self._issued_by = issued_by

    @property
    def created_on(self):
        """Gets the created_on of this V0CommandRequest.

        Timestamp of command request

        :return: The created_on of this V0CommandRequest.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this V0CommandRequest.

        Timestamp of command request

        :param created_on: The created_on of this V0CommandRequest.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def status(self):
        """Gets the status of this V0CommandRequest.

        Show creent status of commands issued during in this request

        :return: The status of this V0CommandRequest.
        :rtype: list[V0CommandRequestStatus]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V0CommandRequest.

        Show creent status of commands issued during in this request

        :param status: The status of this V0CommandRequest.
        :type: list[V0CommandRequestStatus]
        """

        self._status = status

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
        if issubclass(V0CommandRequest, dict):
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
        if not isinstance(other, V0CommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other