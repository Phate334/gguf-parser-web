import pandas as pd

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
                "Context Size": estimate.context_size,
                "Flash Attention": estimate.flash_attention,
                "Logical Batch Size": estimate.logical_batch_size,
                "Physical Batch Size": estimate.physical_batch_size,
            }
        ]
    )
