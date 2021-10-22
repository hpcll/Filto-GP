from time import sleep
from My_Filto import MyFilto


class Case_list(MyFilto):
    # 测试用例
    def test02_open_setting(self):
        """从首页进入设置页"""
        self.d(resourceId="com.video.editor.filto:id/ll_home_bottom_setting").click()  # 打开设置
        sleep(1)
        # Screenshot_img(device_name, "设置")
        self.d(resourceId="com.video.editor.filto:id/ll_home_bottom_discover").click()  # 返回发现页
        # print("回到首页")



