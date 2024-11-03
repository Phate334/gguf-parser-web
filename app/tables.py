import pandas as pd

from app.devices import Device
from app.models import Architecture, Estimate, Metadata, Tokenizer
from app.utils import abbreviate_number, human_readable_size


def get_model_info_df(
    metadata: Metadata, architecture: Architecture, tokenizer: Tokenizer
):
    return pd.DataFrame(
        [
            {
                "Type": metadata.type_,
                "Name": metadata.name,
                "Architecture": metadata.architecture,
                "File Size": human_readable_size(metadata.file_size),
                "Parameters": abbreviate_number(metadata.parameters),
                "Bits Per Weight": round(metadata.bits_per_weight, 2),
                "Maximum Context Length": architecture.maximum_context_length,
                "Vocabulary Length": architecture.vocabulary_length,
                "Tokenizer Model": tokenizer.model,
                "Tokens Size": human_readable_size(tokenizer.tokens_size),
            }
        ]
    )


def get_estimate_df(estimate: Estimate):

    return pd.DataFrame(
        [
            {
                "Max Token per Sec.": round(
                    estimate.items[0].maximum_tokens_per_second, 2
                ),
                "Context Size": estimate.context_size,
                "Offload Layers": estimate.items[0].offload_layers,
                "Full Offloaded": estimate.items[0].full_offloaded,
                "CPU Handle Layers": estimate.items[0].ram.handle_layers,
                "CPU UMA": human_readable_size(estimate.items[0].ram.uma),
                "CPU NONUMA": human_readable_size(estimate.items[0].ram.nonuma),
            }
        ]
    )


def get_gpus_df(estimate: Estimate, gpu_name: str, selected_device: Device):
    return pd.DataFrame(
        [
            {
                "GPU": gpu_name,
                "GPU Memory Size": selected_device.memory_size,
                "Handle Layers": gpu.handle_layers,
                "UMA": human_readable_size(gpu.uma),
                "NONUMA": human_readable_size(gpu.nonuma),
            }
            for gpu in estimate.items[0].vrams
        ]
    )
