from time import sleep

from appium import webdriver
desired_caps={}
#系统类型
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = 6.0
# 模拟器地址
desired_caps['deviceName'] = "127.0.0.1:7555"
# 测试包名
desired_caps['appPackage'] = "com.xueqiu.android"
# 首次进入的页面
desired_caps['appActivity'] = "com.xueqiu.android.main.view.MainActivity"
# 初始设置，清理缓存(没有弹框)
desired_caps["noReset"] = "true"
#首次启动的时候不停止app
desired_caps['dontStopAppOnReset']='true'
#提升速度
desired_caps['skipDeviceInitialization']='true'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
#给一定的加载时间去找到那个元素
driver.implicitly_wait(5)
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
#返回到上一个页面
driver.back()
#再执行一次 返回到首页
driver.back()
sleep(2)
driver.quit()
