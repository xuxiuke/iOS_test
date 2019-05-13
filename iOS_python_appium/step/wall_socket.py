#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年04月22日

@author: Duke    墙面插座+场景
"""

from appiumframework.PO import base_page
from appiumframework.PO import excel
import time

class Wall_socket(base_page.Action):

    # 前置条件：从设备列表进入设备详情页
    def socket_details_page(self):
        self.find_name('设备').click()  # 点击设备
        self.find_name('墙面插座').click()  # 点击墙面插座
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)

    # 前置条件：创建场景名称
    def creat_scene_name(self, name):
        self.switch_h5()
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(name)  # 输入新场景名称呵呵123
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
        time.sleep(1)
        self.switch_app()

    # 前置条件：创建任务-开
    def creat_tasks(self):
        self.find_name('添加任务').click()
        time.sleep(1)
        self.find_name('墙面插座').click()
        time.sleep(1)
        self.find_name('开').click()
        time.sleep(1)
        self.find_name('完成').click()
        time.sleep(2)

    # 前置条件：墙面插座详情页，关闭状态
    def closed_state(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        self.socket_details_page()  # 进入墙面插座设备详情页
        if self.find_name('已开启'):
            self.switch_h5()
            self.find_xpath(excel.xpath_con('socket_switch')).click()  # 点击开关按钮
            time.sleep(1)

    # 前置条件：墙面插座详情页，打开状态
    def opened_state(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        self.socket_details_page()  # 进入墙面插座设备详情页
        if self.find_name('已关闭'):
            self.switch_h5()
            self.find_xpath(excel.xpath_con('socket_switch')).click()  # 点击开关按钮
            time.sleep(1)

    # 1、设备，进入墙面插座详情页
    def details_page(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        self.socket_details_page()  # 进入墙面插座设备详情页
        if self.find_name('已开启'):
            return True
        elif self.find_name('已关闭'):
            return True
        else:
            return False

    # 2、设备-插座详情页，点击返回按钮，返回设备列表页面
    def details_page_back(self):
        self.details_page()  # 进入设备详情页
        self.switch_h5()
        self.find_xpath(excel.xpath_con('socket_back')).click()  # 点击返回按钮
        self.switch_app()
        return self.find_name('全部类别')  # 确认返回设备列表页面，找全部分区也可

    # 3、设备-插座详情页，关闭状态，点击开关按钮，打开插座
    def open_socket(self):
        self.closed_state()  # 进入设备详情页，关闭状态
        self.switch_h5()
        self.find_xpath(excel.xpath_con('socket_switch')).click()  # 点击开关按钮
        time.sleep(1)
        self.switch_app()
        return self.find_name('已开启')

    # 4、设备-插座详情页，打开状态，点击开关按钮，关闭插座
    def close_socket(self):
        self.opened_state()  # 进入设备详情页，打开状态
        self.switch_h5()
        self.find_xpath(excel.xpath_con('socket_switch')).click()  # 点击开关按钮
        time.sleep(1)
        self.switch_app()
        return self.find_name('已关闭')

    # 5、设备-插座详情页，点击更多按钮，进入更多页面
    def more_pages(self):
        self.details_page()  # 进入设备详情页
        self.switch_h5()
        self.find_xpath(excel.xpath_con('socket_more')).click()  # 点击右上更多按钮
        self.switch_app()
        return self.find_name('删除设备')

    # 6、设备-插座详情页-更多，点击返回按钮，进入设备详情页
    def more_pages_back(self):
        self.more_pages()  # 进入更多页面
        self.find_name('common icon back').click()  # 点击左上返回按钮
        time.sleep(2)
        if self.find_name('已开启'):
            return True
        elif self.find_name('已关闭'):
            return True
        else:
            return False

    # 7、设备-插座详情页-更多，重命名哈哈123-确定
    def rename(self):
        self.more_pages()  # 进入更多页面
        self.find_name('重命名').click()  # 点击重命名
        self.find_name('清除文本').click()  # 清空输入框
        self.input_content("type == 'XCUIElementTypeTextField'", '插座：自动化测试')  # 输入新名称
        self.find_name('Done').click()  # 点击完成按钮
        self.find_name('确定').click()  # 点击确定按钮
        self.find_name('处理中...')
        return self.find_name('插座：自动化测试')

    # 8、设备-插座详情页-更多，重命名哈哈123-确定，返回设备列表，可以查找到新设备名称
    def rename_back(self):
        self.rename()  # 修改名称
        time.sleep(1)
        self.driver.back()  # 点击返回
        time.sleep(2)
        return self.find_name('插座：自动化测试')

    # 9、设备-插座详情页-更多，重命名哈哈123-取消
    def rename_cancel(self):
        self.more_pages()  # 进入更多页面
        self.find_name('重命名').click()  # 点击重命名
        self.find_name('清除文本').click()  # 清空输入框
        self.input_content("type == 'XCUIElementTypeTextField'", '插座：自动化测试')  # 输入新名称
        self.find_name('Done').click()  # 点击完成按钮
        self.find_name('取消').click()  # 点击取消按钮
        return self.find_name('插座：自动化测试')

    # 10、设备-插座详情页-更多，命名已有的设备名称，toast提示：设备名称重复！加zzz最后运行！
    def zzz_rename_repeat(self):
        self.more_pages()  # 进入更多页面
        self.find_name('重命名').click()  # 点击重命名
        self.find_name('清除文本').click()  # 清空输入框
        # self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('水浸：自动化')  # 输入重复的设备名称
        self.input_content("type == 'XCUIElementTypeTextField'", '水浸：自动化')  # 输入重复的设备名称
        self.find_name('Done').click()  # 点击完成按钮
        self.find_name('确定').click()  # 点击确定按钮
        self.find_name('处理中...')
        return self.find_name('设备名称重复！')

    # 11、设备-插座详情页-更多，重命名-不输入名称，确定按钮点击无效，重命名弹窗还在
    def rename_none(self):
        self.more_pages()  # 进入更多页面
        self.find_name('重命名').click()  # 点击重命名
        self.find_name('清除文本').click()  # 清空输入框
        self.find_name('Done').click()  # 点击完成按钮
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        return self.find_name('取消') and self.find_name('确定')

    # 12、设备-插座详情页-更多，点击分区，进入分区页面
    def zone_pages(self):
        self.more_pages()  # 进入更多页面
        self.find_name('分区').click()  # 点击分区
        return self.find_name('管理分区')

    # 13、设备-插座详情页-更多-分区，点击返回按钮，返回更多页面
    def zone_pages_back(self):
        self.zone_pages()  # 进入分区页面
        self.find_name('common icon back').click()  # 点击左上返回按钮
        return self.find_name('更多')

    # 14、设备-插座详情页-更多，前置条件至少有一个分区，点击分区，返回更多页面
    def modify_zone(self):
        self.zoning_management_page()  # 分区管理页面,删除已有分区
        self.creat_zone('自动化测试14')  # 新建区域
        self.driver.back()  # 返回设备列表页面
        self.find_name('墙面插座').click()  # 点击墙面插座
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.switch_h5()
        self.find_xpath(excel.xpath_con('socket_more')).click()  # 点击右上更多按钮
        self.switch_app()
        self.find_name('分区').click()  # 点击分区
        self.find_name('自动化测试14').click()  # 点击新建的区域
        self.find_name('处理中...')
        time.sleep(2)
        f1 = bool(self.find_name('更多'))
        f2 = bool(self.find_name('未分区'))
        return f2 == False and f1 == True  # 验证是否返回更多页面、分区右侧不再显示为未分区

    # 15、设备-插座详情页-更多，点击未分区，返回更多页面，未分区可以查找到
    def non_zone(self):
        self.zone_pages()
        self.find_name('未分区').click()  # 点击未分区
        time.sleep(2)
        if self.find_name('管理分区'):
            self.driver.back()
        return self.find_name('未分区')

    # 16、设备-插座详情页-更多-分区，点击右上管理分区，进入分区管理页面
    def zoning_pages(self):
        self.zone_pages()
        self.find_name('管理分区').click()  # 点击右上管理分区按钮
        return self.find_name('分区管理')

    # 17、设备-插座详情页-更多-分区-分区管理，点击返回按钮，返回分区页面
    def zoning_pages_back(self):
        self.zoning_pages()  # 进入分区管理页面
        self.driver.back()  # 点击返回按钮
        return self.find_name('管理分区')

    # 18、设备-插座详情页-更多，点击设备信息，进入设备信息页面，产品名称
    def device_information(self):
        self.more_pages()  # 进入更多页面
        self.find_name('设备信息').click()  # 点击设备信息
        time.sleep(7)
        return self.find_name('产品名称')

    # 19、设备-插座详情页-更多-设备信息，点击返回按钮，返回更多页面
    def device_information_back(self):
        self.more_pages()  # 进入更多页面
        self.find_name('设备信息').click()  # 点击设备信息
        time.sleep(7)
        self.driver.back()  # 点击返回按钮
        return self.find_name('更多')

    # 20、设备-插座详情页-更多，点击找设备，弹窗设备指示灯将闪烁10秒
    def find_device(self):
        self.more_pages()  # 进入更多页面
        self.find_name('找设备').click()  # 点击找设备
        return self.find_name('设备指示灯将闪烁10秒，请查找...')

    # 21、设备-插座详情页-更多-找设备弹窗，点击已找到，弹窗消失
    def find_device_found(self):
        self.find_device()  # 找设备弹窗
        self.find_name('已找到').click()  # 点击已找到
        return self.find_name('设备指示灯将闪烁10秒，请查找...')

    # 22、设备-插座详情页-更多-找设备弹窗，点击再闪一次，弹窗还在
    def find_device_find(self):
        self.find_device()  # 找设备弹窗
        self.find_name('再闪一次').click()  # 点击再闪一次
        time.sleep(1)
        return self.find_name('设备指示灯将闪烁10秒，请查找...')

    # 23、设备-插座详情页-更多，点击删除设备，弹窗确定删除设备吗？
    def delete_device(self):
        self.more_pages()  # 进入更多页面
        self.find_name('删除设备').click()  # 点击删除设备按钮
        return self.find_name('确定删除设备吗？')

    # 24、设备-插座详情页-更多-删除设备弹窗，点击取消按钮，弹窗消失（删除设备用例省略）
    def delete_device_cancel(self):
        self.delete_device()  # 删除设备
        self.find_name('取消').click()  # 点击取消按钮
        return self.find_name('确定删除设备吗？')

    # 25、场景，设置场景打开插座    --------------------------------------------------------------
    def scene_open_socket(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.creat_scene_name('场景自动化25')  # 创建场景名称
        self.creat_tasks()  # 创建任务
        self.find_name('保存').click()
        return self.find_name('场景自动化25')

    # 26、关闭插座，点击打开插座场景
    def click_scene_open_socket(self):
        self.scene_open_socket()  # 设置场景，打开插座
        time.sleep(1)
        self.socket_details_page()  # 进入墙面插座设备详情页
        if self.find_name('已开启'):
            self.switch_h5()
            self.find_xpath(excel.xpath_con('socket_switch')).click()  # 点击关闭插座
            time.sleep(1)
            self.find_xpath(excel.xpath_con('socket_back')).click()  # 点击返回按钮
            self.switch_app()
        else:
            self.switch_h5()
            self.find_xpath(excel.xpath_con('socket_back')).click()  # 点击返回按钮
            self.switch_app()
        self.find_name('首页').click()  # 点击首页
        self.find_name('场景自动化25').click()
        time.sleep(1)
        self.socket_details_page()  # 进入墙面插座设备详情页
        return self.find_name('已开启')

    # 27、场景，设置场景关闭插座
    def scene_close_socket(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.creat_scene_name('场景自动化27')  # 创建场景名称
        self.find_name('添加任务').click()
        time.sleep(1)
        self.find_name('墙面插座').click()
        time.sleep(1)
        self.find_name('关').click()
        time.sleep(1)
        self.find_name('完成').click()
        time.sleep(2)
        self.find_name('保存').click()
        return self.find_name('场景自动化27')

    # 28、打开插座，点击关闭插座场景
    def click_scene_close_socket(self):
        self.scene_close_socket()  # 设置场景，关闭插座
        time.sleep(1)
        self.socket_details_page()  # 进入墙面插座设备详情页
        if self.find_name('已关闭'):
            self.switch_h5()
            self.find_xpath(excel.xpath_con('socket_switch')).click()  # 点击打开插座
            time.sleep(1)
            self.find_xpath(excel.xpath_con('socket_back')).click()  # 点击返回按钮
            self.switch_app()
        else:
            self.switch_h5()
            self.find_xpath(excel.xpath_con('socket_back')).click()  # 点击返回按钮
            self.switch_app()
        self.find_name('首页').click()  # 点击首页
        self.find_name('场景自动化27').click()
        time.sleep(1)
        self.socket_details_page()  # 进入墙面插座设备详情页
        return self.find_name('已关闭')

    # 29、场景，添加延时页面，点击延时按钮，弹出延时设置编辑框
    def scene_time(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.creat_scene_name('场景自动化29')  # 创建场景名称
        self.find_name('添加任务').click()
        time.sleep(1)
        self.find_name('墙面插座').click()
        time.sleep(1)
        self.find_name('开').click()
        time.sleep(1)
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").click()  # 点击打开延时按钮
        time.sleep(1)
        return self.find_name('00')

    # 30、场景，添加延时页面，点击延时按钮，弹出延时设置编辑框，再次点击延时按钮，编辑框隐藏
    def scene_time_off(self):
        self.scene_time()  # 场景，打开延时开关
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").click()  # 点击打开延时按钮
        time.sleep(1)
        return self.find_name('00')

    # 31、场景，添加延时页面，设置延时任务，编辑场景页面查找？秒后执行
    def scene_delay(self):
        self.scene_time()  # 场景，打开延时开关
        self.find_xpath(excel.xpath_con('delay_02_seconds')).click()  # 点击03秒
        time.sleep(1)
        self.find_name('完成').click()
        self.find_name('完成').click()
        time.sleep(2)
        return self.find_ios_predicate("name CONTAINS '2秒后执行'")

    # 32、场景，设置场景打开插座，点击返回按钮，弹窗：编辑的场景尚未保存，是否退出
    def editscene_back(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.creat_scene_name('场景自动化32')  # 创建场景名称
        self.creat_tasks()  # 创建任务
        self.find_xpath(excel.xpath_con('scene_goback')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.find_name('编辑的场景尚未保存，是否退出')  # 判断弹窗元素是否存在

    # 33、场景，设置场景打开插座，点击返回按钮，点击取消，弹窗消失
    def editscene_back_cancel(self):
        self.editscene_back()  # 场景编辑页面，编辑的场景尚未保存弹窗
        self.find_name('取消').click()  # 点击取消按钮
        return self.find_name('编辑的场景尚未保存，是否退出')  # 判断弹窗元素是否存在

    # 34、场景，设置场景打开插座，点击返回按钮，点击退出，任务未保存
    def editscene_back_exit(self):
        self.editscene_back()  # 场景编辑页面，编辑的场景尚未保存弹窗
        self.find_name('退出').click()  # 点击退出按钮
        time.sleep(1)
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        self.find_name('编辑场景').click()  # 点击编辑场景
        time.sleep(1)
        return self.find_ios_predicate("name CONTAINS '墙面插座'")

    # 35、场景，设置场景打开插座，点击返回按钮，点击保存并退出，任务保存成功
    def editscene_back_exitsave(self):
        self.editscene_back()  # 场景编辑页面，编辑的场景尚未保存弹窗
        self.find_name('保存并退出').click()  # 点击退出保存按钮
        time.sleep(1)
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        self.find_name('编辑场景').click()  # 点击编辑场景
        time.sleep(2)
        return self.find_ios_predicate("name CONTAINS '墙面插座'")

    # 36、场景，设置场景打开插座，左划拉出删除按钮
    def editscene_delete(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.creat_scene_name('场景自动化36')  # 创建场景名称
        self.creat_tasks()  # 创建任务
        self.leftswip_editscene(2000)
        return self.find_name('删除')

    # 37、场景，设置场景打开插座，左划拉出删除按钮，点击删除，任务被删除
    def editscene_delete_click(self):
        self.editscene_delete()  # 场景编辑页面，拉出删除按钮
        time.sleep(1)
        self.find_name('删除').click()  # 点击删除按钮
        time.sleep(1)
        return self.find_ios_predicate("name CONTAINS '墙面插座'")

    # 38、场景，设置场景打开插座，点击任务，可以重新设置任务，进入设置设备状态页面
    def editscene_edit(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.creat_scene_name('场景自动化38')  # 创建场景名称
        self.creat_tasks()  # 创建任务
        self.find_ios_predicate("name CONTAINS '墙面插座'").click()  # 点击第一个任务
        time.sleep(1)
        return self.find_name('设置设备状态')

    # 39、场景，添加设备页面，点击全部分区，拉出所有分区，查找未分区
    def editscene_allzone(self):
        self.old_gateway()  # 账号登陆，绑定网关，网关中心页面
        self.driver.back()
        time.sleep(1)
        self.find_name('智能').click()
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.creat_scene_name('场景自动化39')  # 创建场景名称
        self.find_name('添加任务').click()
        time.sleep(1)
        self.find_name('全部分区').click()  # 点击全部分区
        time.sleep(1)
        return self.find_name('未分区')  # 验证未分区元素是否存在

    # 40、场景，添加设备页面，点击全部类别，拉出所有类别，查找智能门锁
    def editscene_allcategory(self):
        self.old_gateway()  # 账号登陆，绑定网关，网关中心页面
        self.driver.back()
        time.sleep(1)
        self.find_name('智能').click()
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.creat_scene_name('场景自动化40')  # 创建场景名称
        self.find_name('添加任务').click()
        time.sleep(1)
        self.find_name('全部类别').click()  # 点击全部类别
        time.sleep(1)
        return self.find_name('智能门锁')

    # 41、场景，添加设备页面，点击批量添加，进入批量添加页面，查找全选
    def editscene_batchadd(self):
        self.old_gateway()  # 账号登陆，绑定网关，网关中心页面
        self.driver.back()
        time.sleep(1)
        self.find_name('智能').click()
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.creat_scene_name('场景自动化41')  # 创建场景名称
        self.find_name('添加任务').click()
        time.sleep(1)
        self.find_name('批量添加').click()  # 点击批量添加
        time.sleep(1)
        return self.find_name('全选')
