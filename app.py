import json
import os
from pathlib import Path

import gradio as gr
import pandas as pd

GGUF_PARSER_VERSION = os.getenv("GGUF_PARSER_VERSION", "v0.12.0")
gguf_parser = Path("gguf-parser-linux-amd64")
gguf_parser_url = f"https://github.com/gpustack/gguf-parser-go/releases/download/{GGUF_PARSER_VERSION}/{gguf_parser}"


def process_url(url):
    try:
        res = os.popen(f"./{gguf_parser} -url {url} --json").read()
        data = json.loads(res)

        architecture_df = pd.DataFrame([data["architecture"]])

        estimate_df = pd.DataFrame(
            [
                {
                    # "maximumTokensPerSecond": data["estimate"]["items"][0][
                    #     "maximumTokensPerSecond"
                    # ],
                    "offloadLayers": data["estimate"]["items"][0]["offloadLayers"],
                    "fullOffloaded": data["estimate"]["items"][0]["fullOffloaded"],
                    "contextSize": data["estimate"]["contextSize"],
                    "flashAttention": data["estimate"]["flashAttention"],
                    "distributable": data["estimate"]["distributable"],
                }
            ]
        )

        metadata_df = pd.DataFrame([data["metadata"]])

        tokenizer_df = pd.DataFrame([data["tokenizer"]])

        return architecture_df, estimate_df, metadata_df, tokenizer_df
    except Exception as e:
        return e


if __name__ == "__main__":
    if not gguf_parser.exists():
        os.system(f"wget {gguf_parser_url}")
        os.system(f"chmod +x {gguf_parser}")

    with open("devices.json", "r", encoding="utf-8") as f:
        device_list = json.load(f)

    with gr.Blocks(title="GGUF 分析器") as iface:
        url_input = gr.Textbox(label="輸入 GGUF URL")
        submit_btn = gr.Button("送出")

        gr.Markdown("### 模型架構")
        architecture_table = gr.DataFrame()

        gr.Markdown("### 效能評估")
        estimate_table = gr.DataFrame()

        gr.Markdown("### 中繼資料")
        metadata_table = gr.DataFrame()

        gr.Markdown("### 分詞器")
        tokenizer_table = gr.DataFrame()

        submit_btn.click(
            fn=process_url,
            inputs=url_input,
            outputs=[
                architecture_table,
                estimate_table,
                metadata_table,
                tokenizer_table,
            ],
        )
    iface.launch()
