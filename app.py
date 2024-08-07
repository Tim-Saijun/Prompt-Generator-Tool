#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 下午4:06
# @Author  : Tim-Saijun https://zair.top
# @File    : compile_po.py
# @Project : PromptGenerator
import os
import gettext

import streamlit as st
from openai import OpenAI

from utils.Simple_Prompt_Generator import metaprompt, pretty_print

# Set up language environment
languages = {
    "English": "en",
    "中文": "zh-CN"
}

# User selects language
st.sidebar.title("🎻 Prompt Generator App")
lang = st.sidebar.selectbox("Choose your language / 选择你的语言", list(languages.keys()))

# Get corresponding language code
lang_code = languages[lang]

# Set language environment
locales_dir = os.path.join(os.path.dirname(__file__), 'locales')
lang_translations = gettext.translation('messages', locales_dir, languages=[lang_code])
lang_translations.install()
_ = lang_translations.gettext

with st.sidebar:
    # Configure sidebar
    st.sidebar.header(_("API Configuration"))
    api_key = st.sidebar.text_input(_("API Key"), type="password", value=os.environ.get("OPENAI_API_KEY"))
    base_url = st.sidebar.text_input(_("Base URL"), value="https://api.openai.com/v1")
    model_name = st.sidebar.text_input(_("Model Name"), value="gpt-4o-mini")

    if api_key is None:
        try:
            if 'OPENAI_API_KEY' in st.secrets:
                api_key = st.secrets['OPENAI_API_KEY']
            if 'OPENAI_BASE_URL' in st.secrets:
                base_url = st.secrets['OPENAI_BASE_URL']
            if 'OPENAI_MODEL_NAME' in st.secrets:
                model_name = st.secrets['OPENAI_MODEL_NAME']
        except:
            pass

    if api_key is not None and base_url is not None and model_name is not None:
        st.success('API configuration already done!', icon='✅')
    else:
        st.warning('Please enter your credentials!', icon='⚠️')

    st.sidebar.write(
        "Note: You can use any model provider that supports the OpenAI API, such as Llama, Kimi, Qwen, etc.")

st.markdown(_("Welcome Message"))
# Main area
with st.form("input_area"):
    st.header(_("Task Description and Variable Input"))
    task = st.text_area(_("Task Description"), value=_("Sample Task"))
    variables_input = st.text_area(_("Optional Variable Names"), value="")
    submitted = st.form_submit_button(_("Submit"))


def generate_prompt():
    # Convert variables to list
    variables = [var.strip() for var in variables_input.split('\n') if var.strip()]

    # API client
    client = None
    if api_key and base_url:
        client = OpenAI(api_key=api_key, base_url=base_url)

    # Replace TASK placeholder
    prompt = metaprompt.replace("{{TASK}}", task)

    # Construct assistant input section
    assistant_partial = "<Inputs>"
    if variables:
        for variable in variables:
            assistant_partial += f"\n{{$" + variable.upper() + "}}"
        assistant_partial += "\n</Inputs>\n<Instructions Structure>"

    # Request API and process response
    message = ""
    if client:
        response = client.chat.completions.create(
            model=model_name,
            max_tokens=4096,
            messages=[
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": assistant_partial},
            ],
            temperature=0,
        )
        message = response.choices[0].message.content
    return message


if submitted:
    message = generate_prompt()
    st.subheader(_("Result"))
    st.write(pretty_print(message))
