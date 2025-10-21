
import os
import time
from typing import Dict, Any
import requests

API_ONE = os.getenv("API_ONE", "https://httpbin.org/get")
API_TWO = os.getenv("API_TWO", "https://httpbin.org/uuid")

def fetch(url: str) -> Dict[str, Any]:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()

def run_pipeline() -> Dict[str, Any]:
    "Minimal multi-API orchestration demo (sequential for simplicity)."
    t0 = time.time()
    a = fetch(API_ONE)
    b = fetch(API_TWO)
    return {
        "elapsed_sec": round(time.time() - t0, 3),
        "api_one_sample": a,
        "api_two_sample": b,
    }

if __name__ == "__main__":
    print(run_pipeline())
