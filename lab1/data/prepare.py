import os
import tiktoken
import numpy as np
import json

input_file_path = os.path.join(os.path.dirname(__file__), "2021-43_zh_head_0000-0.01.jsonl")
data = ""
with open(input_file_path, "r") as f:
    for line in f:
        obj = json.loads(line.strip())
        data += obj["text"] + "\n\n"
print("=============================== example ===============================")
print(data[:1000])
n = len(data)
train_data = data[: int(n * 0.9)]
val_data = data[int(n * 0.9) :]

enc = tiktoken.get_encoding("cl100k_base")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)

print("============================== statistic ==============================")
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

train_ids = np.array(train_ids, dtype=np.uint32)
val_ids = np.array(val_ids, dtype=np.uint32)
train_ids.tofile(os.path.join(os.path.dirname(__file__), "train.bin"))
val_ids.tofile(os.path.join(os.path.dirname(__file__), "val.bin"))
