import json
import os
from pathlib import Path

import gradio as gr
import pandas as pd

from app.models import GgufParser
from app.tables import get_estimate_df, get_model_info_df

GGUF_PARSER_VERSION = os.getenv("GGUF_PARSER_VERSION", "v0.12.0")
gguf_parser = Path("gguf-parser-linux-amd64")
gguf_parser_url = f"https://github.com/gpustack/gguf-parser-go/releases/download/{GGUF_PARSER_VERSION}/{gguf_parser}"
DEFAULT_URL = "https://huggingface.co/phate334/Llama-3.1-8B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.1-8b-instruct-q4_k_m.gguf"


def process_url(url, context_length):
    try:
        res = os.popen(
            f"./{gguf_parser} --ctx-size={context_length} -url {url} --json"
        ).read()
        parser_result = GgufParser.model_validate_json(res)

        model_info = get_model_info_df(
            parser_result.metadata, parser_result.architecture, parser_result.tokenizer
        )

        estimate_df = get_estimate_df(parser_result.estimate)

        return model_info, estimate_df
    except Exception as e:
        return e


if __name__ == "__main__":
    if not gguf_parser.exists():
        os.system(f"wget {gguf_parser_url}&&chmod +x {gguf_parser}")

    with open("devices.json", "r", encoding="utf-8") as f:
        device_list = json.load(f)

    with gr.Blocks(title="GGUF Parser") as iface:
        url_input = gr.Textbox(placeholder="Enter GGUF URL", value=DEFAULT_URL)
        context_length = gr.Number(label="Context Length", value=8192)
        submit_btn = gr.Button("Send")

        submit_btn.click(
            fn=process_url,
            inputs=[url_input, context_length],
            outputs=[
                gr.DataFrame(label="Model Info"),
                gr.DataFrame(label="ESTIMATE"),
            ],
        )
    iface.launch()
