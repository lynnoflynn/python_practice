import yaml
data = yaml.safe_load(open("game.yml"))
#打印出来yaml 转换的字典
print(data)
#打印出来yaml 转换的字典，key值me对应的value
print(data["me"])
#打印出来yaml 转换的字典，key值me对应的value 的key值对应为hp”
print(data["me"]["hp"])
