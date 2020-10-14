import yaml
data = yaml.safe_load(open("game.yml"))
#dump , dict -> yml
# a = [[{'a':1},'admin2'],'admin3']
# print(yaml.safe_dump(a))

a = [[{'a':1},'admin2'],'admin3']

# python 对象写入了yaml 文件
with open("data3","w") as f:
    yaml.safe_dump(a,f)

