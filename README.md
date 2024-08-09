# SETUP

## Prerequisites
- Python 3.x
- Virtualenv (optional but recommended for isolated environment)

## Installation
1. **Create virtual environment:**

```bash
python3 -m venv poc-venv
```
OR 
```bash
py -m venv poc-venv
```

2. **Activate the virtual environment:**

Linux/MAC
```bash
source poc-venv/bin/activate
```
Windows 
```bash
poc-venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run App:**

```bash
uvicorn app.main:app --port 8002 --reload
```


# NOTES


https://github.com/intangible-explorer/fastapi-projects/tree/main/authentication/JWT-AUTH-AUTHENTICATION

https://medium.com/codex/developing-asynchronous-apis-with-fastapi-5c1bb848649e

