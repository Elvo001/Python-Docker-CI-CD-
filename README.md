
# Multi-API Automation Pipeline (Minimal)

Minimal Python script that orchestrates calls to two public APIs and returns a merged result.
Swap the endpoints via environment variables to adapt it to your automation use cases.

## Run
```bash
pip install -r requirements.txt
python pipeline.py
```

## Configure
- `API_ONE` (default: https://httpbin.org/get)
- `API_TWO` (default: https://httpbin.org/uuid)
```
export API_ONE=https://httpbin.org/ip
export API_TWO=https://httpbin.org/user-agent
python pipeline.py
```
