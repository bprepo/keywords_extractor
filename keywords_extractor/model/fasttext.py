# -*- coding: utf-8 -*-
"""Textrank module."""

import fasttext

def process_with_fasttext(file_path):
    model = fasttext.skipgram(file_path,file_path[:-4])
    return model['test']