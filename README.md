# 哈工大自然语言处理实验介绍
哈工大NLP课程实验由车万翔教授指导，共两次，涉及训练transformer(decoder_only)语言生成模型以及微调已有的预训练大语言模型。初学者通过这两个实验可以初步了解自然语言处理的基本流程以及实现方式。 
## 实验1：从零开始实现基于Transformer的语言模型
实现过程详见jupyter文档，使用本代码前需要先自行准备语料训练数据集（保存为json文件），将其放入data文件夹，并改写prepare.py文件。文本数据集格式示例如下：
```json
{"text": "其实不难看出，在上述关系中，只有夫妻关系是最基本的。婆婆、儿媳、祖父母之间的关系不应该一直绑在一起。许多家庭仍无法“打破”这些亲密关系的实际压力或家庭感情:一方面老人承受生理和心理压力帮助孩子照顾家庭但另一方面他们不能没有他们的子孙。感受:一方面，孩子们对下一代的养育方式有很多抱怨，另一方面，他们无法承受没有老人帮助的压力。因此，矛盾会一次又一次地出现。\n在亲密关系中适度的“分手”并不意味着放弃亲情。不管亲情有多好，它也需要呼吸的空间。传统的三代同堂的家庭模式显然不能适应现在的社会。如何尽快完成传统家庭向现代家庭的过渡，是家庭和社会都必须面对的问题。\n中国人民大学人口与发展研究中心副主任宋健认为，生活在同一屋檐下，不同的一代人有着不同的生活习惯和生活方式，这不可避免地会产生摩擦和相互适应的问题。房价居高不下，居住空间相对狭小。城市家庭尤其如此。\n这种家庭冲突的背后其实是合理分担育儿责任的问题。无论祖父母是愿意照顾孙辈，还是选择享受轻松自由的晚年，都应该得到认可和尊重。目前，有必要尽快完善社会化包容性托儿服务，以缓解家庭育儿困难。\n"}
```
## 实验2：类ChatGPT通用对话系统
实验2主要实现的是针对预训练大语言模型的特定场景微调，说明文档详见./lab2/README.md