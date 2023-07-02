# codeGPT
It can help you to understand code.

It based on chatGPT

## init venv environment
```shell
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
```

## How to use
1. change env.example to .env
```shell
mv env.example .env
```
2. input your OPEN api key to `.env` file
```shell
OPENAI_API_KEY=sk-xxxxxxxxxxxxx
```
3. change code repository name in `analysis_repository.py`

4. run `analysis_repository.py` file
```shell
python analysis_repository.py
```

## feature list
- [] generate markdown book
- [] command line
- [] offline version