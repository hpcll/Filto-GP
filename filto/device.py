import os, re
import uiautomator2


class device_connect(uiautomator2):

    # def app_start(self,name):
    #     uiautomator2.connect().app_start(name)

    def get_device_list(self):
        """获取设备ID"""
        # msg = os.popen("adb devices -l").read()
        msg1 = os.popen("adb devices ").read()
        # print(msg)
        deviceId = re.findall(r'([\w]+)\tdevice', msg1)
        # deviceId_name = re.findall(r"device.*model:(.*)\sdevice", msg)
        d = uiautomator2.connect(deviceId[0])
        return d








