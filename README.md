# codeGPT
CodeGPT is an innovative solution, leveraging the power of ChatGPT to analyze and interpret programming code. It represents a groundbreaking advancement in the field of coding and software development, using AI technology to help developers understand complex code structures.

Developed predominantly using Python, CodeGPT carries the known benefits of this powerful language, such as simplicity and flexibility. This allows the tool to be highly compatible with a wide variety of operating systems and programming environments.

One unique feature of CodeGPT is its ability to generate Markdown files from the interpreted code. This provides developers with an organized and comprehensible view of their codebase. Furthermore, these Markdown files can be utilized to build a comprehensive website or used as standalone guides for understanding the intricate details of the code.

Key Features:

- Code analysis and interpretation powered by ChatGPT.
- Generation of Markdown files for efficient documentation.
- Capability to generate websites to showcase your code's functionality.
- Compatibility and flexibility ensured by the Python foundation.

In essence, CodeGPT is more than just a code interpreter; it's a comprehensive suite of tools designed to make coding more accessible and efficient. It aids in understanding complex code, generates organized documentation, and can even help present your work through an interactive website. Let CodeGPT be your partner in coding, experience a new way of managing and understanding code, and boost your productivity today.

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
# default file type is java
python main.py analyse LMAX-Exchange/disruptor

# filer python file
# python main.py LMAX-Exchange/disruptor --file-extension py

```

4. generate markdown book
```shell
python main.py book ./explanations/disruptor-master
```

## feature list
- [x] command line
- [x] generate markdown book
- [ ] offline version