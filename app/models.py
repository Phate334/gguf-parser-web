from pydantic import BaseModel, Field


class GgufParser(BaseModel):
    metadata: "Metadata"
    architecture: "Architecture"
    tokenizer: "Tokenizer"
    estimate: "Estimate"


class Metadata(BaseModel):
    type_: str = Field(alias="type")
    architecture: str
    quantization_version: int = Field(alias="quantizationVersion")
    alignment: int
    name: str
    file_type: int = Field(alias="fileType")
    little_endian: bool = Field(alias="littleEndian")
    file_size: int = Field(alias="fileSize")
    size: int
    parameters: int
    bits_per_weight: float = Field(alias="bitsPerWeight")


class Architecture(BaseModel):
    type_: str = Field(alias="type")
    architecture: str
    maximum_context_length: int = Field(alias="maximumContextLength")
    embedding_length: int = Field(alias="embeddingLength")
    block_count: int = Field(alias="blockCount")
    feed_forward_length: int = Field(alias="feedForwardLength")
    attention_head_count: int = Field(alias="attentionHeadCount")
    attention_head_count_kv: int = Field(alias="attentionHeadCountKV")
    attention_layer_norm_rmse_epsilon: float = Field(
        alias="attentionLayerNormRMSEpsilon"
    )
    attention_key_length: int = Field(alias="attentionKeyLength")
    attention_value_length: int = Field(alias="attentionValueLength")
    attention_causal: bool = Field(alias="attentionCausal")
    rope_dimension_count: int = Field(alias="ropeDimensionCount")
    rope_frequency_base: int = Field(alias="ropeFrequencyBase")
    vocabulary_length: int = Field(alias="vocabularyLength")
    embedding_gqa: int = Field(alias="embeddingGQA")
    embedding_key_gqa: int = Field(alias="embeddingKeyGQA")
    embedding_value_gqa: int = Field(alias="embeddingValueGQA")


class Tokenizer(BaseModel):
    model: str
    tokens_length: int = Field(alias="tokensLength")
    merges_length: int = Field(alias="mergesLength")
    added_token_length: int = Field(alias="addedTokenLength")
    bos_token_id: int = Field(alias="bosTokenID")
    eos_token_id: int = Field(alias="eosTokenID")
    eot_token_id: int = Field(alias="eotTokenID")
    eom_token_id: int = Field(alias="eomTokenID")
    unknown_token_id: int = Field(alias="unknownTokenID")
    separator_token_id: int = Field(alias="separatorTokenID")
    padding_token_id: int = Field(alias="paddingTokenID")
    tokens_size: int = Field(alias="tokensSize")
    merges_size: int = Field(alias="mergesSize")


class Ram(BaseModel):
    handle_layers: int = Field(alias="handleLayers")
    handle_last_layer: int = Field(alias="handleLastLayer")
    handle_output_layer: bool = Field(alias="handleOutputLayer")
    remote: bool
    position: int
    uma: int
    nonuma: int


class Item(BaseModel):
    offload_layers: int = Field(alias="offloadLayers")
    full_offloaded: bool = Field(alias="fullOffloaded")
    ram: "Ram"
    vrams: list["Ram"]


class Estimate(BaseModel):
    items: list["Item"]
    type_: str = Field(alias="type")
    architecture: str
    context_size: int = Field(alias="contextSize")
    flash_attention: bool = Field(alias="flashAttention")
    no_mmap: bool = Field(alias="noMMap")
    embedding_only: bool = Field(alias="embeddingOnly")
    reranking: bool
    distributable: bool
    logical_batch_size: int = Field(alias="logicalBatchSize")
    physical_batch_size: int = Field(alias="physicalBatchSize")
    type_: str = Field(alias="type")
    architecture: str
    context_size: int = Field(alias="contextSize")
    flash_attention: bool = Field(alias="flashAttention")
    no_mmap: bool = Field(alias="noMMap")
    embedding_only: bool = Field(alias="embeddingOnly")
    reranking: bool
    distributable: bool
    logical_batch_size: int = Field(alias="logicalBatchSize")
    physical_batch_size: int = Field(alias="physicalBatchSize")
