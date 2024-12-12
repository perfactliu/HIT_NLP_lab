"""
将HIT的SFT数据衔接至alpaca_GPT4的结尾
"""
import pandas as pd
import json

# 读取Excel文件
df = pd.read_excel('HIT_SFT.xlsx', usecols=None, engine='xlrd')

# 创建一个空列表来存储转换后的数据
json_data = []

# 遍历每一行，从第二行开始（索引从0开始，所以第二行是索引1）
for index, row in df.iloc[1:].iterrows():
    data = {
        "instruction": row[0],  # 第一列
        "input": row[1],        # 第二列
        "output": row[2]        # 第三列
    }
    json_data.append(data)

# 读取已有的JSON文件
try:
    with open('Alpaca_GPT4.json', 'r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)
except FileNotFoundError:
    # 如果文件不存在，初始化为空列表
    existing_data = []

# 将新的数据追加到现有数据中
existing_data.extend(json_data)

# 将更新后的数据写回文件
with open('miniCPM_HIT_SFT.json', 'w', encoding='utf-8') as json_file:
    json.dump(existing_data, json_file,default = str, ensure_ascii=False, indent=4)
