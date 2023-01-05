# FastApi Examples


## Local Setup

### Prerequisites
- python 3.8 or 3.9
- virtualenv (`pip install virtualenv`)

### Steps

1. Clone the repository from using the command:

```bash
git clone https://github.com/famcodings/fast_api_examples.git
``` 
*__Setup__*

2. Run ```virtualenv venv```
3. Activate virtualenv using ```virtualenv .\venv\Scripts\activate``` if on windows and ```source ./venv/bin/activate``` if on linux or MacOS
4. Install Requirements ```pip install -r requirements.txt```
5. Run Server ```uvicorn server:app --reload```
5. Navigate to http://127.0.0.1:8000/docs to start interacting with APIs

