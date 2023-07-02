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
3. generate markdown file
```shell
python main.py LMAX-Exchange/disruptor
```

4. generate markdown book
```shell
python main.py book ./explanations/disruptor-master
```

## feature list
- [x] command line
- [x] generate markdown book
- [ ] offline version