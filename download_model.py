import huggingface_hub

#从命令行获取模型名称
import sys
repo_id = sys.argv[1]

# Download model from the Hub to local cache
model_dir = huggingface_hub.snapshot_download(repo_id,ignore_patterns=["*.h5", "*.ot", "*.msgpack"])
print(model_dir)
