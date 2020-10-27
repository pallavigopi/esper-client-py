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

from esperclient.models.owner import Owner


class Content(object):
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
        'id': 'int',
        'download_url': 'str',
        'name': 'str',
        'key': 'str',
        'is_dir': 'bool',
        'kind': 'str',
        'hash': 'str',
        'size': 'str',
        'path': 'str',
        'permissions': 'str',
        'tags': 'list[str]',
        'description': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'enterprise': 'str',
        'owner': 'Owner'
    }

    attribute_map = {
        'id': 'id',
        'download_url': 'download_url',
        'name': 'name',
        'key': 'key',
        'is_dir': 'is_dir',
        'kind': 'kind',
        'hash': 'hash',
        'size': 'size',
        'path': 'path',
        'permissions': 'permissions',
        'tags': 'tags',
        'description': 'description',
        'created': 'created',
        'modified': 'modified',
        'enterprise': 'enterprise',
        'owner': 'owner'
    }

    def __init__(self, id=None, download_url=None, name=None, key=None, is_dir=False, kind=None, hash=None, size=None, path=None, permissions=None, tags=None, description=None, created=None, modified=None, enterprise=None, owner=None):
        """Content - a model defined in Swagger"""

        self._id = None
        self._download_url = None
        self._name = None
        self._key = None
        self._is_dir = None
        self._kind = None
        self._hash = None
        self._size = None
        self._path = None
        self._permissions = None
        self._tags = None
        self._description = None
        self._created = None
        self._modified = None
        self._enterprise = None
        self._owner = None
        self.discriminator = None

        self.id = id
        if download_url is not None:
            self.download_url = download_url
        if name is not None:
            self.name = name
        if key is not None:
            self.key = key
        if is_dir is not None:
            self.is_dir = is_dir
        if kind is not None:
            self.kind = kind
        if hash is not None:
            self.hash = hash
        if size is not None:
            self.size = size
        if path is not None:
            self.path = path
        if permissions is not None:
            self.permissions = permissions
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if enterprise is not None:
            self.enterprise = enterprise
        if owner is not None:
            self.owner = owner

    @property
    def id(self):
        """Gets the id of this Content.

        Unique content Identifier

        :return: The id of this Content.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Content.

        Unique content Identifier

        :param id: The id of this Content.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def download_url(self):
        """Gets the download_url of this Content.

        URL to download the content

        :return: The download_url of this Content.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this Content.

        URL to download the content

        :param download_url: The download_url of this Content.
        :type: str
        """

        self._download_url = download_url

    @property
    def name(self):
        """Gets the name of this Content.

        Name of the content

        :return: The name of this Content.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Content.

        Name of the content

        :param name: The name of this Content.
        :type: str
        """

        self._name = name

    @property
    def key(self):
        """Gets the key of this Content.


        :return: The key of this Content.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Content.


        :param key: The key of this Content.
        :type: str
        """
        if key is not None and len(key) > 255:
            raise ValueError("Invalid value for `key`, length must be less than or equal to `255`")
        if key is not None and len(key) < 1:
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `1`")

        self._key = key

    @property
    def is_dir(self):
        """Gets the is_dir of this Content.


        :return: The is_dir of this Content.
        :rtype: bool
        """
        return self._is_dir

    @is_dir.setter
    def is_dir(self, is_dir):
        """Sets the is_dir of this Content.


        :param is_dir: The is_dir of this Content.
        :type: bool
        """

        self._is_dir = is_dir

    @property
    def kind(self):
        """Gets the kind of this Content.

        The mime type of the content

        :return: The kind of this Content.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Content.

        The mime type of the content

        :param kind: The kind of this Content.
        :type: str
        """
        if kind is not None and len(kind) > 255:
            raise ValueError("Invalid value for `kind`, length must be less than or equal to `255`")

        self._kind = kind

    @property
    def hash(self):
        """Gets the hash of this Content.

        Hash string of the content

        :return: The hash of this Content.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Content.

        Hash string of the content

        :param hash: The hash of this Content.
        :type: str
        """

        self._hash = hash

    @property
    def size(self):
        """Gets the size of this Content.

        Size of the content in bytes

        :return: The size of this Content.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Content.

        Size of the content in bytes

        :param size: The size of this Content.
        :type: str
        """
        if size is not None and len(size) > 255:
            raise ValueError("Invalid value for `size`, length must be less than or equal to `255`")

        self._size = size

    @property
    def path(self):
        """Gets the path of this Content.

        Path to the content

        :return: The path of this Content.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Content.

        Path to the content

        :param path: The path of this Content.
        :type: str
        """

        self._path = path

    @property
    def permissions(self):
        """Gets the permissions of this Content.

        The permssion string for the content

        :return: The permissions of this Content.
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Content.

        The permssion string for the content

        :param permissions: The permissions of this Content.
        :type: str
        """

        self._permissions = permissions

    @property
    def tags(self):
        """Gets the tags of this Content.

        Tags for the content

        :return: The tags of this Content.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Content.

        Tags for the content

        :param tags: The tags of this Content.
        :type: list[str]
        """

        self._tags = tags

    @property
    def description(self):
        """Gets the description of this Content.

        Description for the content

        :return: The description of this Content.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Content.

        Description for the content

        :param description: The description of this Content.
        :type: str
        """

        self._description = description

    @property
    def created(self):
        """Gets the created of this Content.


        :return: The created of this Content.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Content.


        :param created: The created of this Content.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Content.


        :return: The modified of this Content.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Content.


        :param modified: The modified of this Content.
        :type: datetime
        """

        self._modified = modified

    @property
    def enterprise(self):
        """Gets the enterprise of this Content.

        URL of the enterprise resource

        :return: The enterprise of this Content.
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this Content.

        URL of the enterprise resource

        :param enterprise: The enterprise of this Content.
        :type: str
        """

        self._enterprise = enterprise

    @property
    def owner(self):
        """Gets the owner of this Content.


        :return: The owner of this Content.
        :rtype: Owner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Content.


        :param owner: The owner of this Content.
        :type: Owner
        """

        self._owner = owner

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
        if issubclass(Content, dict):
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
        if not isinstance(other, Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
