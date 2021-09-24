import time
import unittest
import uiautomator2 as u2
from My_Filto import MyFilto
from device import device_connect


class Case_list(MyFilto,device_connect):

    # 测试用例
    def test01_open_app(self):
        # 启动App
        self.app_start("com.video.editor.filto")
        time.sleep(1)


    def test02_open_setting(self):
        self.get_device_list()
        time.sleep(5)
        """从首页进入设置页"""
        self(resourceId="com.video.editor.filto:id/ll_home_bottom_setting").click()  # 打开设置
        time.sleep(1)
        # Screenshot_img(device_name, "设置")
        self(resourceId="com.video.editor.filto:id/ll_home_bottom_discover").click()  # 返回发现页
        print("回到首页")



