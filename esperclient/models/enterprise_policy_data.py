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

from esperclient.models.enterprise_policy_data_device_password_policy import EnterprisePolicyDataDevicePasswordPolicy
from esperclient.models.enterprise_policy_data_device_update_policy import EnterprisePolicyDataDeviceUpdatePolicy
from esperclient.models.enterprise_policy_data_frp_googles import EnterprisePolicyDataFrpGoogles
from esperclient.models.enterprise_policy_data_google_account_permission import EnterprisePolicyDataGoogleAccountPermission
from esperclient.models.enterprise_policy_data_phone_policy import EnterprisePolicyDataPhonePolicy


class EnterprisePolicyData(object):
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
        'keyguard_disabled': 'bool',
        'safe_boot_disabled': 'bool',
        'status_bar_disabled': 'bool',
        'factory_reset_disabled': 'bool',
        'screenshot_disabled': 'bool',
        'usb_connectivity_disabled': 'bool',
        'sms_disabled': 'bool',
        'outgoing_calls_disabled': 'bool',
        'camera_disabled': 'bool',
        'nfc_beam_disabled': 'bool',
        'disable_play_store': 'bool',
        'usb_file_transfer_disabled': 'bool',
        'tethering_disabled': 'bool',
        'date_time_config_disabled': 'bool',
        'app_uninstall_disabled': 'bool',
        'google_assistant_disabled': 'bool',
        'disable_local_app_install': 'bool',
        'adb_disabled': 'bool',
        'phone_policy': 'EnterprisePolicyDataPhonePolicy',
        'frp_googles': 'list[EnterprisePolicyDataFrpGoogles]',
        'google_account_permission': 'EnterprisePolicyDataGoogleAccountPermission',
        'device_password_policy': 'EnterprisePolicyDataDevicePasswordPolicy',
        'minimum_password_length': 'int',
        'permission_policy': 'str',
        'device_update_policy': 'EnterprisePolicyDataDeviceUpdatePolicy',
        'settings_access_level': 'str',
        'settings_app_password': 'str'
    }

    attribute_map = {
        'keyguard_disabled': 'keyguardDisabled',
        'safe_boot_disabled': 'safeBootDisabled',
        'status_bar_disabled': 'statusBarDisabled',
        'factory_reset_disabled': 'factoryResetDisabled',
        'screenshot_disabled': 'screenshotDisabled',
        'usb_connectivity_disabled': 'usbConnectivityDisabled',
        'sms_disabled': 'smsDisabled',
        'outgoing_calls_disabled': 'outgoingCallsDisabled',
        'camera_disabled': 'cameraDisabled',
        'nfc_beam_disabled': 'nfcBeamDisabled',
        'disable_play_store': 'disablePlayStore',
        'usb_file_transfer_disabled': 'usbFileTransferDisabled',
        'tethering_disabled': 'tetheringDisabled',
        'date_time_config_disabled': 'dateTimeConfigDisabled',
        'app_uninstall_disabled': 'appUninstallDisabled',
        'google_assistant_disabled': 'googleAssistantDisabled',
        'disable_local_app_install': 'disableLocalAppInstall',
        'adb_disabled': 'adbDisabled',
        'phone_policy': 'phonePolicy',
        'frp_googles': 'frpGoogles',
        'google_account_permission': 'googleAccountPermission',
        'device_password_policy': 'devicePasswordPolicy',
        'minimum_password_length': 'minimumPasswordLength',
        'permission_policy': 'permissionPolicy',
        'device_update_policy': 'deviceUpdatePolicy',
        'settings_access_level': 'settingsAccessLevel',
        'settings_app_password': 'settingsAppPassword'
    }

    def __init__(self, keyguard_disabled=None, safe_boot_disabled=None, status_bar_disabled=None, factory_reset_disabled=None, screenshot_disabled=None, usb_connectivity_disabled=None, sms_disabled=None, outgoing_calls_disabled=None, camera_disabled=None, nfc_beam_disabled=None, disable_play_store=None, usb_file_transfer_disabled=None, tethering_disabled=None, date_time_config_disabled=None, app_uninstall_disabled=None, google_assistant_disabled=None, disable_local_app_install=None, adb_disabled=None, phone_policy=None, frp_googles=None, google_account_permission=None, device_password_policy=None, minimum_password_length=None, permission_policy=None, device_update_policy=None, settings_access_level=None, settings_app_password=None):
        """EnterprisePolicyData - a model defined in Swagger"""

        self._keyguard_disabled = None
        self._safe_boot_disabled = None
        self._status_bar_disabled = None
        self._factory_reset_disabled = None
        self._screenshot_disabled = None
        self._usb_connectivity_disabled = None
        self._sms_disabled = None
        self._outgoing_calls_disabled = None
        self._camera_disabled = None
        self._nfc_beam_disabled = None
        self._disable_play_store = None
        self._usb_file_transfer_disabled = None
        self._tethering_disabled = None
        self._date_time_config_disabled = None
        self._app_uninstall_disabled = None
        self._google_assistant_disabled = None
        self._disable_local_app_install = None
        self._adb_disabled = None
        self._phone_policy = None
        self._frp_googles = None
        self._google_account_permission = None
        self._device_password_policy = None
        self._minimum_password_length = None
        self._permission_policy = None
        self._device_update_policy = None
        self._settings_access_level = None
        self._settings_app_password = None
        self.discriminator = None

        if keyguard_disabled is not None:
            self.keyguard_disabled = keyguard_disabled
        if safe_boot_disabled is not None:
            self.safe_boot_disabled = safe_boot_disabled
        if status_bar_disabled is not None:
            self.status_bar_disabled = status_bar_disabled
        if factory_reset_disabled is not None:
            self.factory_reset_disabled = factory_reset_disabled
        if screenshot_disabled is not None:
            self.screenshot_disabled = screenshot_disabled
        if usb_connectivity_disabled is not None:
            self.usb_connectivity_disabled = usb_connectivity_disabled
        if sms_disabled is not None:
            self.sms_disabled = sms_disabled
        if outgoing_calls_disabled is not None:
            self.outgoing_calls_disabled = outgoing_calls_disabled
        if camera_disabled is not None:
            self.camera_disabled = camera_disabled
        if nfc_beam_disabled is not None:
            self.nfc_beam_disabled = nfc_beam_disabled
        if disable_play_store is not None:
            self.disable_play_store = disable_play_store
        if usb_file_transfer_disabled is not None:
            self.usb_file_transfer_disabled = usb_file_transfer_disabled
        if tethering_disabled is not None:
            self.tethering_disabled = tethering_disabled
        if date_time_config_disabled is not None:
            self.date_time_config_disabled = date_time_config_disabled
        if app_uninstall_disabled is not None:
            self.app_uninstall_disabled = app_uninstall_disabled
        if google_assistant_disabled is not None:
            self.google_assistant_disabled = google_assistant_disabled
        if disable_local_app_install is not None:
            self.disable_local_app_install = disable_local_app_install
        if adb_disabled is not None:
            self.adb_disabled = adb_disabled
        if phone_policy is not None:
            self.phone_policy = phone_policy
        if frp_googles is not None:
            self.frp_googles = frp_googles
        if google_account_permission is not None:
            self.google_account_permission = google_account_permission
        if device_password_policy is not None:
            self.device_password_policy = device_password_policy
        if minimum_password_length is not None:
            self.minimum_password_length = minimum_password_length
        if permission_policy is not None:
            self.permission_policy = permission_policy
        if device_update_policy is not None:
            self.device_update_policy = device_update_policy
        if settings_access_level is not None:
            self.settings_access_level = settings_access_level
        if settings_app_password is not None:
            self.settings_app_password = settings_app_password

    @property
    def keyguard_disabled(self):
        """Gets the keyguard_disabled of this EnterprisePolicyData.

        Should KeyGuard be disabled?

        :return: The keyguard_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._keyguard_disabled

    @keyguard_disabled.setter
    def keyguard_disabled(self, keyguard_disabled):
        """Sets the keyguard_disabled of this EnterprisePolicyData.

        Should KeyGuard be disabled?

        :param keyguard_disabled: The keyguard_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._keyguard_disabled = keyguard_disabled

    @property
    def safe_boot_disabled(self):
        """Gets the safe_boot_disabled of this EnterprisePolicyData.

        Should SafeBoot be disabled?

        :return: The safe_boot_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._safe_boot_disabled

    @safe_boot_disabled.setter
    def safe_boot_disabled(self, safe_boot_disabled):
        """Sets the safe_boot_disabled of this EnterprisePolicyData.

        Should SafeBoot be disabled?

        :param safe_boot_disabled: The safe_boot_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._safe_boot_disabled = safe_boot_disabled

    @property
    def status_bar_disabled(self):
        """Gets the status_bar_disabled of this EnterprisePolicyData.

        Should Status Bar be disabled?

        :return: The status_bar_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._status_bar_disabled

    @status_bar_disabled.setter
    def status_bar_disabled(self, status_bar_disabled):
        """Sets the status_bar_disabled of this EnterprisePolicyData.

        Should Status Bar be disabled?

        :param status_bar_disabled: The status_bar_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._status_bar_disabled = status_bar_disabled

    @property
    def factory_reset_disabled(self):
        """Gets the factory_reset_disabled of this EnterprisePolicyData.

        Should Factory Reset be disabled?

        :return: The factory_reset_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._factory_reset_disabled

    @factory_reset_disabled.setter
    def factory_reset_disabled(self, factory_reset_disabled):
        """Sets the factory_reset_disabled of this EnterprisePolicyData.

        Should Factory Reset be disabled?

        :param factory_reset_disabled: The factory_reset_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._factory_reset_disabled = factory_reset_disabled

    @property
    def screenshot_disabled(self):
        """Gets the screenshot_disabled of this EnterprisePolicyData.

        Should Screenshot capability be disabled?

        :return: The screenshot_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._screenshot_disabled

    @screenshot_disabled.setter
    def screenshot_disabled(self, screenshot_disabled):
        """Sets the screenshot_disabled of this EnterprisePolicyData.

        Should Screenshot capability be disabled?

        :param screenshot_disabled: The screenshot_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._screenshot_disabled = screenshot_disabled

    @property
    def usb_connectivity_disabled(self):
        """Gets the usb_connectivity_disabled of this EnterprisePolicyData.

        Should USB connectivity be disabled?

        :return: The usb_connectivity_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._usb_connectivity_disabled

    @usb_connectivity_disabled.setter
    def usb_connectivity_disabled(self, usb_connectivity_disabled):
        """Sets the usb_connectivity_disabled of this EnterprisePolicyData.

        Should USB connectivity be disabled?

        :param usb_connectivity_disabled: The usb_connectivity_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._usb_connectivity_disabled = usb_connectivity_disabled

    @property
    def sms_disabled(self):
        """Gets the sms_disabled of this EnterprisePolicyData.

        Should SMS functionality be disabled?

        :return: The sms_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._sms_disabled

    @sms_disabled.setter
    def sms_disabled(self, sms_disabled):
        """Sets the sms_disabled of this EnterprisePolicyData.

        Should SMS functionality be disabled?

        :param sms_disabled: The sms_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._sms_disabled = sms_disabled

    @property
    def outgoing_calls_disabled(self):
        """Gets the outgoing_calls_disabled of this EnterprisePolicyData.

        Should Outgoing Calls be disabled?

        :return: The outgoing_calls_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._outgoing_calls_disabled

    @outgoing_calls_disabled.setter
    def outgoing_calls_disabled(self, outgoing_calls_disabled):
        """Sets the outgoing_calls_disabled of this EnterprisePolicyData.

        Should Outgoing Calls be disabled?

        :param outgoing_calls_disabled: The outgoing_calls_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._outgoing_calls_disabled = outgoing_calls_disabled

    @property
    def camera_disabled(self):
        """Gets the camera_disabled of this EnterprisePolicyData.

        Should Camera be disabled?

        :return: The camera_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._camera_disabled

    @camera_disabled.setter
    def camera_disabled(self, camera_disabled):
        """Sets the camera_disabled of this EnterprisePolicyData.

        Should Camera be disabled?

        :param camera_disabled: The camera_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._camera_disabled = camera_disabled

    @property
    def nfc_beam_disabled(self):
        """Gets the nfc_beam_disabled of this EnterprisePolicyData.

        Should NFC capability be disabled?

        :return: The nfc_beam_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._nfc_beam_disabled

    @nfc_beam_disabled.setter
    def nfc_beam_disabled(self, nfc_beam_disabled):
        """Sets the nfc_beam_disabled of this EnterprisePolicyData.

        Should NFC capability be disabled?

        :param nfc_beam_disabled: The nfc_beam_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._nfc_beam_disabled = nfc_beam_disabled

    @property
    def disable_play_store(self):
        """Gets the disable_play_store of this EnterprisePolicyData.

        Should Google Play Store be disabled on the device?

        :return: The disable_play_store of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._disable_play_store

    @disable_play_store.setter
    def disable_play_store(self, disable_play_store):
        """Sets the disable_play_store of this EnterprisePolicyData.

        Should Google Play Store be disabled on the device?

        :param disable_play_store: The disable_play_store of this EnterprisePolicyData.
        :type: bool
        """

        self._disable_play_store = disable_play_store

    @property
    def usb_file_transfer_disabled(self):
        """Gets the usb_file_transfer_disabled of this EnterprisePolicyData.

        Should USB File transfer capability be disabled?

        :return: The usb_file_transfer_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._usb_file_transfer_disabled

    @usb_file_transfer_disabled.setter
    def usb_file_transfer_disabled(self, usb_file_transfer_disabled):
        """Sets the usb_file_transfer_disabled of this EnterprisePolicyData.

        Should USB File transfer capability be disabled?

        :param usb_file_transfer_disabled: The usb_file_transfer_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._usb_file_transfer_disabled = usb_file_transfer_disabled

    @property
    def tethering_disabled(self):
        """Gets the tethering_disabled of this EnterprisePolicyData.

        Should USB Tethering capability be enabled?

        :return: The tethering_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._tethering_disabled

    @tethering_disabled.setter
    def tethering_disabled(self, tethering_disabled):
        """Sets the tethering_disabled of this EnterprisePolicyData.

        Should USB Tethering capability be enabled?

        :param tethering_disabled: The tethering_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._tethering_disabled = tethering_disabled

    @property
    def date_time_config_disabled(self):
        """Gets the date_time_config_disabled of this EnterprisePolicyData.

        Should Date/Time configuration capability be disabled?

        :return: The date_time_config_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._date_time_config_disabled

    @date_time_config_disabled.setter
    def date_time_config_disabled(self, date_time_config_disabled):
        """Sets the date_time_config_disabled of this EnterprisePolicyData.

        Should Date/Time configuration capability be disabled?

        :param date_time_config_disabled: The date_time_config_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._date_time_config_disabled = date_time_config_disabled

    @property
    def app_uninstall_disabled(self):
        """Gets the app_uninstall_disabled of this EnterprisePolicyData.

        Should App uninstall capability be disabled?

        :return: The app_uninstall_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._app_uninstall_disabled

    @app_uninstall_disabled.setter
    def app_uninstall_disabled(self, app_uninstall_disabled):
        """Sets the app_uninstall_disabled of this EnterprisePolicyData.

        Should App uninstall capability be disabled?

        :param app_uninstall_disabled: The app_uninstall_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._app_uninstall_disabled = app_uninstall_disabled

    @property
    def google_assistant_disabled(self):
        """Gets the google_assistant_disabled of this EnterprisePolicyData.

        Should Google Assistant feature be disabled?

        :return: The google_assistant_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._google_assistant_disabled

    @google_assistant_disabled.setter
    def google_assistant_disabled(self, google_assistant_disabled):
        """Sets the google_assistant_disabled of this EnterprisePolicyData.

        Should Google Assistant feature be disabled?

        :param google_assistant_disabled: The google_assistant_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._google_assistant_disabled = google_assistant_disabled

    @property
    def disable_local_app_install(self):
        """Gets the disable_local_app_install of this EnterprisePolicyData.

        Should Side-loading of Applications be disabled?

        :return: The disable_local_app_install of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._disable_local_app_install

    @disable_local_app_install.setter
    def disable_local_app_install(self, disable_local_app_install):
        """Sets the disable_local_app_install of this EnterprisePolicyData.

        Should Side-loading of Applications be disabled?

        :param disable_local_app_install: The disable_local_app_install of this EnterprisePolicyData.
        :type: bool
        """

        self._disable_local_app_install = disable_local_app_install

    @property
    def adb_disabled(self):
        """Gets the adb_disabled of this EnterprisePolicyData.

        Should Android Debugger be disabled?

        :return: The adb_disabled of this EnterprisePolicyData.
        :rtype: bool
        """
        return self._adb_disabled

    @adb_disabled.setter
    def adb_disabled(self, adb_disabled):
        """Sets the adb_disabled of this EnterprisePolicyData.

        Should Android Debugger be disabled?

        :param adb_disabled: The adb_disabled of this EnterprisePolicyData.
        :type: bool
        """

        self._adb_disabled = adb_disabled

    @property
    def phone_policy(self):
        """Gets the phone_policy of this EnterprisePolicyData.


        :return: The phone_policy of this EnterprisePolicyData.
        :rtype: EnterprisePolicyDataPhonePolicy
        """
        return self._phone_policy

    @phone_policy.setter
    def phone_policy(self, phone_policy):
        """Sets the phone_policy of this EnterprisePolicyData.


        :param phone_policy: The phone_policy of this EnterprisePolicyData.
        :type: EnterprisePolicyDataPhonePolicy
        """

        self._phone_policy = phone_policy

    @property
    def frp_googles(self):
        """Gets the frp_googles of this EnterprisePolicyData.

        Details regarding Factory Reset Protection capability. List of permitted Google People IDs, emails and such

        :return: The frp_googles of this EnterprisePolicyData.
        :rtype: list[EnterprisePolicyDataFrpGoogles]
        """
        return self._frp_googles

    @frp_googles.setter
    def frp_googles(self, frp_googles):
        """Sets the frp_googles of this EnterprisePolicyData.

        Details regarding Factory Reset Protection capability. List of permitted Google People IDs, emails and such

        :param frp_googles: The frp_googles of this EnterprisePolicyData.
        :type: list[EnterprisePolicyDataFrpGoogles]
        """

        self._frp_googles = frp_googles

    @property
    def google_account_permission(self):
        """Gets the google_account_permission of this EnterprisePolicyData.


        :return: The google_account_permission of this EnterprisePolicyData.
        :rtype: EnterprisePolicyDataGoogleAccountPermission
        """
        return self._google_account_permission

    @google_account_permission.setter
    def google_account_permission(self, google_account_permission):
        """Sets the google_account_permission of this EnterprisePolicyData.


        :param google_account_permission: The google_account_permission of this EnterprisePolicyData.
        :type: EnterprisePolicyDataGoogleAccountPermission
        """

        self._google_account_permission = google_account_permission

    @property
    def device_password_policy(self):
        """Gets the device_password_policy of this EnterprisePolicyData.


        :return: The device_password_policy of this EnterprisePolicyData.
        :rtype: EnterprisePolicyDataDevicePasswordPolicy
        """
        return self._device_password_policy

    @device_password_policy.setter
    def device_password_policy(self, device_password_policy):
        """Sets the device_password_policy of this EnterprisePolicyData.


        :param device_password_policy: The device_password_policy of this EnterprisePolicyData.
        :type: EnterprisePolicyDataDevicePasswordPolicy
        """

        self._device_password_policy = device_password_policy

    @property
    def minimum_password_length(self):
        """Gets the minimum_password_length of this EnterprisePolicyData.

        What is the minimum length for your device's password

        :return: The minimum_password_length of this EnterprisePolicyData.
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        """Sets the minimum_password_length of this EnterprisePolicyData.

        What is the minimum length for your device's password

        :param minimum_password_length: The minimum_password_length of this EnterprisePolicyData.
        :type: int
        """
        if minimum_password_length is not None and minimum_password_length < 4:
            raise ValueError("Invalid value for `minimum_password_length`, must be a value greater than or equal to `4`")

        self._minimum_password_length = minimum_password_length

    @property
    def permission_policy(self):
        """Gets the permission_policy of this EnterprisePolicyData.

        What permission should be applied by default for all apps, henceforth?

        :return: The permission_policy of this EnterprisePolicyData.
        :rtype: str
        """
        return self._permission_policy

    @permission_policy.setter
    def permission_policy(self, permission_policy):
        """Sets the permission_policy of this EnterprisePolicyData.

        What permission should be applied by default for all apps, henceforth?

        :param permission_policy: The permission_policy of this EnterprisePolicyData.
        :type: str
        """
        allowed_values = ["PERMISSION_POLICY_PROMPT", "PERMISSION_POLICY_AUTO_GRANT", "PERMISSION_POLICY_AUTO_DENY"]
        if permission_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `permission_policy` ({0}), must be one of {1}"
                .format(permission_policy, allowed_values)
            )

        self._permission_policy = permission_policy

    @property
    def device_update_policy(self):
        """Gets the device_update_policy of this EnterprisePolicyData.


        :return: The device_update_policy of this EnterprisePolicyData.
        :rtype: EnterprisePolicyDataDeviceUpdatePolicy
        """
        return self._device_update_policy

    @device_update_policy.setter
    def device_update_policy(self, device_update_policy):
        """Sets the device_update_policy of this EnterprisePolicyData.


        :param device_update_policy: The device_update_policy of this EnterprisePolicyData.
        :type: EnterprisePolicyDataDeviceUpdatePolicy
        """

        self._device_update_policy = device_update_policy

    @property
    def settings_access_level(self):
        """Gets the settings_access_level of this EnterprisePolicyData.

        Type of Android settings app to be applied? Default System Settings or ESPER Settings App?

        :return: The settings_access_level of this EnterprisePolicyData.
        :rtype: str
        """
        return self._settings_access_level

    @settings_access_level.setter
    def settings_access_level(self, settings_access_level):
        """Sets the settings_access_level of this EnterprisePolicyData.

        Type of Android settings app to be applied? Default System Settings or ESPER Settings App?

        :param settings_access_level: The settings_access_level of this EnterprisePolicyData.
        :type: str
        """
        allowed_values = ["SYSTEM", "SHOONYA", "NONE"]
        if settings_access_level not in allowed_values:
            raise ValueError(
                "Invalid value for `settings_access_level` ({0}), must be one of {1}"
                .format(settings_access_level, allowed_values)
            )

        self._settings_access_level = settings_access_level

    @property
    def settings_app_password(self):
        """Gets the settings_app_password of this EnterprisePolicyData.

        Lock Password (optional) for the ESPER Settings app

        :return: The settings_app_password of this EnterprisePolicyData.
        :rtype: str
        """
        return self._settings_app_password

    @settings_app_password.setter
    def settings_app_password(self, settings_app_password):
        """Sets the settings_app_password of this EnterprisePolicyData.

        Lock Password (optional) for the ESPER Settings app

        :param settings_app_password: The settings_app_password of this EnterprisePolicyData.
        :type: str
        """

        self._settings_app_password = settings_app_password

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
        if issubclass(EnterprisePolicyData, dict):
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
        if not isinstance(other, EnterprisePolicyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
