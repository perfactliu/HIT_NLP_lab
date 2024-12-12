from transformers import AutoTokenizer,AutoModelForCausalLM

# 加载模型和分词器
# model_name = "./openBMB/miniCPM-bf16"
model_name = "./results"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
input_text = "请简要介绍哈尔滨工业大学的历史。"  # 示例问题
inputs = tokenizer(input_text, return_tensors="pt")

# 使用模型生成回答
outputs = model.generate(**inputs, max_length=150)
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(answer)







