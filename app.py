import os
from pathlib import Path

import gradio as gr

GGUF_PARSER_VERSION = os.getenv("GGUF_PARSER_VERSION", "v0.12.0")
gguf_parser = Path("gguf-parser-linux-amd64")

def greet(tmp):
    # Run the gguf-parser-go binary
    gguf_parser_output = os.popen(f"./{gguf_parser} --version").read()
    return f"{gguf_parser_output}"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

if __name__ == "__main__":
    if not gguf_parser.exists():
        gguf_parser_url = f"https://github.com/gpustack/gguf-parser-go/releases/download/{GGUF_PARSER_VERSION}/gguf-parser-linux-amd64"
        os.system(f"wget {gguf_parser_url}")
        os.system(f"chmod +x {gguf_parser}")
    iface.launch()
