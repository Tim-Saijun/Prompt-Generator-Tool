#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 下午4:06
# @Author  : Tim-Saijun https://zair.top
# @File    : compile_po.py
# @Project : PromptGenerator
import polib


def compile_mo_files():
    locales = ['en', 'zh-CN']
    for locale in locales:
        po_file = f'{locale}/LC_MESSAGES/messages.po'
        mo_file = f'{locale}/LC_MESSAGES/messages.mo'
        po = polib.pofile(po_file, encoding='utf-8')
        po.save_as_mofile(mo_file)
        print(f"Compiled {po_file} to {mo_file}")


if __name__ == "__main__":
    compile_mo_files()
