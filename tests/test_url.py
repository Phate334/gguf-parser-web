from app.utils import cleanup_url

# https://huggingface.co/phate334/Llama-3.1-8B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.1-8b-instruct-q4_k_m.gguf?download=true
# https://huggingface.co/phate334/Llama-3.1-8B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.1-8b-instruct-q4_k_m.gguf
# https://huggingface.co/phate334/Llama-3.1-8B-Instruct-Q4_K_M-GGUF/blob/main/llama-3.1-8b-instruct-q4_k_m.gguf
# cleanup_url 輸出都應該要是 https://huggingface.co/phate334/Llama-3.1-8B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.1-8b-instruct-q4_k_m.gguf
# 其餘非 huggingface.co 的 url 只要前後沒有空白就好

resolve_url = "https://huggingface.co/phate334/Llama-3.1-8B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.1-8b-instruct-q4_k_m.gguf"
resolve_url_download = "https://huggingface.co/phate334/Llama-3.1-8B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.1-8b-instruct-q4_k_m.gguf?download=true"
blob_url = "https://huggingface.co/phate334/Llama-3.1-8B-Instruct-Q4_K_M-GGUF/blob/main/llama-3.1-8b-instruct-q4_k_m.gguf"
other_url = "https://git.gss.com.tw/phate_wang/llm/llama-3.1-8b-instruct-q4_k_m.gguf"


def test_cleanup_url():
    assert cleanup_url(resolve_url) == resolve_url
    assert cleanup_url(resolve_url_download) == resolve_url
    assert cleanup_url(blob_url) == resolve_url
    assert cleanup_url(other_url) == other_url
