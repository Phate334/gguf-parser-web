import json
import os
from pathlib import Path

import gradio as gr
import pandas as pd

from app.devices import Device
from app.models import GgufParser
from app.tables import get_estimate_df, get_gpus_df, get_model_info_df

GGUF_PARSER_VERSION = os.getenv("GGUF_PARSER_VERSION", "v0.12.0")
gguf_parser = Path("gguf-parser-linux-amd64")
gguf_parser_url = f"https://github.com/gpustack/gguf-parser-go/releases/download/{GGUF_PARSER_VERSION}/{gguf_parser}"
DEFAULT_URL = "https://huggingface.co/phate334/Llama-3.1-8B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.1-8b-instruct-q4_k_m.gguf"

with open("devices.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    devices = {key: Device(**value) for key, value in data.items()}

device_options = [
    f"{key} (Memory: {value.memory_size}GB, Bandwidth: {value.memory_bandwidth}GB/s)"
    for key, value in devices.items()
]


def process_url(url, context_length, device_selection):
    try:
        # 取得選擇的裝置鍵值
        device_name = device_selection.split(" ")[0]
        selected_device = devices[device_name]
        res = os.popen(
            f'./{gguf_parser} --ctx-size={context_length} -url {url} --device-metric "{selected_device.FLOPS};{selected_device.memory_bandwidth}GBps" --json'
        ).read()
        parser_result = GgufParser.model_validate_json(res)

        model_info = get_model_info_df(
            parser_result.metadata, parser_result.architecture, parser_result.tokenizer
        )

        estimate_df = get_estimate_df(parser_result.estimate)

        gpus_info_df = get_gpus_df(parser_result.estimate, device_name, selected_device)

        return model_info, estimate_df, gpus_info_df
    except Exception as e:
        return e


if __name__ == "__main__":
    if not gguf_parser.exists():
        os.system(f"wget {gguf_parser_url}&&chmod +x {gguf_parser}")

    with gr.Blocks(title="GGUF Parser") as iface:
        gr.Markdown(
            "This Space is a web GUI for the [gpustack/gguf-parser-go](https://github.com/gpustack/gguf-parser-go) package, designed for users who are not familiar with CLI. For more detailed output results, please consider using the original tool. If you find this GUI helpful, please give that a star."
        )
        url_input = gr.Textbox(
            label="GGUF File URL", placeholder="Enter GGUF URL", value=DEFAULT_URL
        )
        context_length = gr.Number(label="Context Length", value=8192)
        device_dropdown = gr.Dropdown(label="Select Device", choices=device_options)
        submit_btn = gr.Button("Send")

        submit_btn.click(
            fn=process_url,
            inputs=[url_input, context_length, device_dropdown],
            outputs=[
                gr.DataFrame(label="Model Info"),
                gr.DataFrame(label="ESTIMATE"),
                gr.DataFrame(label="GPUs INFO"),
            ],
        )
    iface.launch()
