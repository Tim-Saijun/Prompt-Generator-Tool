


# 🎈 Prompt Generator Tool

Application tool that automatically generates prompts with one click.

The tool is designed to help users generate prompts for various tasks, such as text generation, text classification, and text summarization. The tool uses the OpenAI compatible API to generate prompts and provides users with a simple interface to input their desired task and parameters.

This project is inspired by the [Claude AI prompt generator](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator) and aims to provide a similar experience for generating prompts with a simple and intuitive interface.

## Overview of the App

![demo-en](https://github.com/user-attachments/assets/e3633b4f-da6f-4bef-8d7f-5b50b7a003d2)
![demo-zh](https://github.com/user-attachments/assets/30597922-ad8e-456a-85c8-c5e5fe7e7b3c)

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://prompt-generator-tool.streamlit.app/)

## Run it locally

### Using Docker
```sh
docker run -d \
  -e OPENAI_API_KEY=your_openai_api_key \
  -e OPENAI_BASE_URL=your_openai_base_url \
  -e OPENAI_MODEL_NAME=your_openai_model_name \
  -p 8501:8501 \
  timsaijun/prompt-generator
```
中国大陆的用户可以使用腾讯源：
```sh
docker run -d \
  -e OPENAI_API_KEY=your_openai_api_key \
  -e OPENAI_BASE_URL=your_openai_base_url \
  -e OPENAI_MODEL_NAME=your_openai_model_name \
  -p 8501:8501 \
  ccr.ccs.tencentyun.com/saijun/prompt-generator
```


### From the source code
```sh
pip install -r requirements.txt
streamlit run app.py
```
