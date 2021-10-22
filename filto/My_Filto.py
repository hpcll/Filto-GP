import os
import re
import unittest
import warnings
import uiautomator2 as u2


class MyFilto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        msg = os.popen("adb devices").read()
        deviceId = re.findall(r'([\w]+)\tdevice', msg)[0]
        cls.d = u2.connect(deviceId)

    def setUp(self) -> None:
        self.d.app_start("com.video.editor.filto")

    def tearDown(self) -> None:
        os.popen("adb shell am force-stop com.video.editor.filto")



