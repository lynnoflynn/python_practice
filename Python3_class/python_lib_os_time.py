#os模块
#import os
# #print (os.listdir("./"))
# # os.removedirs("testdir")删除文件
# #print(os.getcwd())获取当前目录
# print(os.path.exists("b"))判断文件或者目录是否存在
# if not os.path.exists("b"):
#     os.mkdir("b") 创建目录
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt","w")
#     f.write("hello, os using")
#     f.close()

# time模块
import time
# print(time.asctime())国外的时间格式
# print(time.time())时间戳
# #1599053135.621849
# print(time.localtime())时间戳转成时间元组
# #time.struct_time(tm_year=2020, tm_mon=9, tm_mday=2, tm_hour=21, tm_min=35, tm_sec=38, tm_wday=2, tm_yday=246, tm_isdst=0)
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) 将党建的时间戳转成带格式的时间
# #2020-09-02 21:30:59
# 获取两天前的时间
now_timestamp = time.time()
Two_days = 2*24*60*60
Two_days_ago = now_timestamp-Two_days
time.localtime(Two_days_ago)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(Two_days_ago)))
