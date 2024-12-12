"""
从训练集中取出1/5的数据存入验证集
"""
import json
import random

# 读取原始的 JSON 文件
with open('miniCPM_HIT_SFT.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 计算随机选择的数据的数量，取 1/5
sample_size = len(data) // 5

# 从原始数据中随机选择 1/5
validation_data = random.sample(data, sample_size)

# 将选中的数据保存到新的 JSON 文件中
with open('eval_miniCPM_HIT_SFT.json', 'w', encoding='utf-8') as file:
    json.dump(validation_data, file, ensure_ascii=False, indent=4)

print(f"选中了 {sample_size} 条数据并保存到 'eval_miniCPM_HIT_SFT.json' 文件中")
