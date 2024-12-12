# 实验文件使用说明
## 各个模块说明
- logs:训练日志
- results:可加载模型
- document文件:实验报告
- add_data.py:合成数据集
- create_val_data.py:由数据集生成验证集
- sft.py:训练代码
- test_model.py:模型测试示例
- miniCPM_HIT_SFT.json:训练集
- eval_miniCPM_HIT_SFT.json:验证集

## 数据集说明
哈工大微调数据集（HIT_SFT.xlsx）以及扩展数据集（Alpaca_GPT4.json）不在文件夹中，若需下载请参照链接[哈工大微调数据集](https://docs.qq.com/sheet/DVGZEZ1B1ampQZlFo?tab=BB08J2)和[扩展数据集索引](https://github.com/chaoswork/sft_datasets/tree/master)

## 模型基座说明
本实验使用的模型"miniCPM-bf16"不在本文件夹中，如需下载，请运行下面代码：

```python
#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('OpenBMB/miniCPM-bf16')
```

并将下载好的模型放入本文件夹中。

未尽说明事项详见实验报告。