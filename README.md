
# Multi-API Automation Pipeline (Minimal)

 Python script that orchestrates calls to two public APIs and returns a merged result.


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
