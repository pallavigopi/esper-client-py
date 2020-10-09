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


class EnterpriseUpdateV1(object):
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
        'name': 'str',
        'registered_name': 'str',
        'registered_address': 'str',
        'location': 'str',
        'zipcode': 'str',
        'contact_person': 'str',
        'contact_number': 'str',
        'contact_email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'registered_name': 'registered_name',
        'registered_address': 'registered_address',
        'location': 'location',
        'zipcode': 'zipcode',
        'contact_person': 'contact_person',
        'contact_number': 'contact_number',
        'contact_email': 'contact_email'
    }

    def __init__(self, id=None, name=None, registered_name=None, registered_address=None, location=None, zipcode=None, contact_person=None, contact_number=None, contact_email=None):
        """EnterpriseUpdateV1 - a model defined in Swagger"""

        self._id = None
        self._name = None
        self._registered_name = None
        self._registered_address = None
        self._location = None
        self._zipcode = None
        self._contact_person = None
        self._contact_number = None
        self._contact_email = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if registered_name is not None:
            self.registered_name = registered_name
        if registered_address is not None:
            self.registered_address = registered_address
        if location is not None:
            self.location = location
        if zipcode is not None:
            self.zipcode = zipcode
        if contact_person is not None:
            self.contact_person = contact_person
        if contact_number is not None:
            self.contact_number = contact_number
        if contact_email is not None:
            self.contact_email = contact_email

    @property
    def id(self):
        """Gets the id of this EnterpriseUpdateV1.

        Id of the enterprise

        :return: The id of this EnterpriseUpdateV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnterpriseUpdateV1.

        Id of the enterprise

        :param id: The id of this EnterpriseUpdateV1.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EnterpriseUpdateV1.

        Name of the enterprise

        :return: The name of this EnterpriseUpdateV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnterpriseUpdateV1.

        Name of the enterprise

        :param name: The name of this EnterpriseUpdateV1.
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def registered_name(self):
        """Gets the registered_name of this EnterpriseUpdateV1.

        Registered Name of the enterprise

        :return: The registered_name of this EnterpriseUpdateV1.
        :rtype: str
        """
        return self._registered_name

    @registered_name.setter
    def registered_name(self, registered_name):
        """Sets the registered_name of this EnterpriseUpdateV1.

        Registered Name of the enterprise

        :param registered_name: The registered_name of this EnterpriseUpdateV1.
        :type: str
        """
        if registered_name is not None and len(registered_name) > 255:
            raise ValueError("Invalid value for `registered_name`, length must be less than or equal to `255`")
        if registered_name is not None and len(registered_name) < 1:
            raise ValueError("Invalid value for `registered_name`, length must be greater than or equal to `1`")

        self._registered_name = registered_name

    @property
    def registered_address(self):
        """Gets the registered_address of this EnterpriseUpdateV1.

        Registered address of the enterprise.

        :return: The registered_address of this EnterpriseUpdateV1.
        :rtype: str
        """
        return self._registered_address

    @registered_address.setter
    def registered_address(self, registered_address):
        """Sets the registered_address of this EnterpriseUpdateV1.

        Registered address of the enterprise.

        :param registered_address: The registered_address of this EnterpriseUpdateV1.
        :type: str
        """
        if registered_address is not None and len(registered_address) > 255:
            raise ValueError("Invalid value for `registered_address`, length must be less than or equal to `255`")
        if registered_address is not None and len(registered_address) < 1:
            raise ValueError("Invalid value for `registered_address`, length must be greater than or equal to `1`")

        self._registered_address = registered_address

    @property
    def location(self):
        """Gets the location of this EnterpriseUpdateV1.

        City, State, Country location of the enterprise

        :return: The location of this EnterpriseUpdateV1.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EnterpriseUpdateV1.

        City, State, Country location of the enterprise

        :param location: The location of this EnterpriseUpdateV1.
        :type: str
        """
        if location is not None and len(location) > 255:
            raise ValueError("Invalid value for `location`, length must be less than or equal to `255`")
        if location is not None and len(location) < 1:
            raise ValueError("Invalid value for `location`, length must be greater than or equal to `1`")

        self._location = location

    @property
    def zipcode(self):
        """Gets the zipcode of this EnterpriseUpdateV1.

        Description of the enterprise

        :return: The zipcode of this EnterpriseUpdateV1.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this EnterpriseUpdateV1.

        Description of the enterprise

        :param zipcode: The zipcode of this EnterpriseUpdateV1.
        :type: str
        """
        if zipcode is not None and len(zipcode) > 8:
            raise ValueError("Invalid value for `zipcode`, length must be less than or equal to `8`")
        if zipcode is not None and len(zipcode) < 1:
            raise ValueError("Invalid value for `zipcode`, length must be greater than or equal to `1`")

        self._zipcode = zipcode

    @property
    def contact_person(self):
        """Gets the contact_person of this EnterpriseUpdateV1.

        Person who is the point of contact for the enterprise

        :return: The contact_person of this EnterpriseUpdateV1.
        :rtype: str
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this EnterpriseUpdateV1.

        Person who is the point of contact for the enterprise

        :param contact_person: The contact_person of this EnterpriseUpdateV1.
        :type: str
        """
        if contact_person is not None and len(contact_person) > 255:
            raise ValueError("Invalid value for `contact_person`, length must be less than or equal to `255`")
        if contact_person is not None and len(contact_person) < 1:
            raise ValueError("Invalid value for `contact_person`, length must be greater than or equal to `1`")

        self._contact_person = contact_person

    @property
    def contact_number(self):
        """Gets the contact_number of this EnterpriseUpdateV1.

        Contact number of the enterprise

        :return: The contact_number of this EnterpriseUpdateV1.
        :rtype: str
        """
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        """Sets the contact_number of this EnterpriseUpdateV1.

        Contact number of the enterprise

        :param contact_number: The contact_number of this EnterpriseUpdateV1.
        :type: str
        """
        if contact_number is not None and len(contact_number) > 20:
            raise ValueError("Invalid value for `contact_number`, length must be less than or equal to `20`")
        if contact_number is not None and len(contact_number) < 1:
            raise ValueError("Invalid value for `contact_number`, length must be greater than or equal to `1`")

        self._contact_number = contact_number

    @property
    def contact_email(self):
        """Gets the contact_email of this EnterpriseUpdateV1.

        Contact email address of the enterprise

        :return: The contact_email of this EnterpriseUpdateV1.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this EnterpriseUpdateV1.

        Contact email address of the enterprise

        :param contact_email: The contact_email of this EnterpriseUpdateV1.
        :type: str
        """
        if contact_email is not None and len(contact_email) > 254:
            raise ValueError("Invalid value for `contact_email`, length must be less than or equal to `254`")
        if contact_email is not None and len(contact_email) < 1:
            raise ValueError("Invalid value for `contact_email`, length must be greater than or equal to `1`")

        self._contact_email = contact_email

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
        if issubclass(EnterpriseUpdateV1, dict):
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
        if not isinstance(other, EnterpriseUpdateV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
