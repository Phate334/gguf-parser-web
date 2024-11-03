from pydantic import BaseModel, Field


class Device(BaseModel):
    memory_size: int = Field(alias="memorySize")
    memory_bandwidth: float = Field(alias="memoryBandwidth")
    FLOPS: str
