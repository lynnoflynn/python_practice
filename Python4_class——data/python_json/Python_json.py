import json
#json.dump 表示把python对象写入在文件中
#json.dumps 表示把python对象转化成字符串
dict_hogwarts = {
    "a": [1, 2, 3],
    "name": ["spider man", "战士"]
}
# 在data.json中写入Python object数据
# with open("data.json", "w") as f:
#     json.dump(dict_hogwarts, f)

# print(type(dict_hogwarts))
# print(type(json.dumps(dict_hogwarts)))
# <class 'dict'>
# <class 'str'>
json_load = json.load(open("data.json"))
print("使用json_load的数据类型为",type(json_load))