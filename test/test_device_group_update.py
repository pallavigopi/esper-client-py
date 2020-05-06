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



from __future__ import absolute_import

import unittest

import esperclient
from esperclient.models.device_group_update import DeviceGroupUpdate
from esperclient.rest import ApiException


class TestDeviceGroupUpdate(unittest.TestCase):
    """DeviceGroupUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeviceGroupUpdate(self):
        """Test DeviceGroupUpdate"""
        model = esperclient.models.device_group_update.DeviceGroupUpdate()
        pass


if __name__ == '__main__':
    unittest.main()
