# -*- coding: utf-8 -*-
"""Flair module."""

from flair.embeddings import BertEmbeddings, FlairEmbeddings
from flair.embeddings import Sentence, StackedEmbeddings


def combine_embeddings():
    """Combine embeddings into one stacked embedding."""
    # init Flair embeddings
    flair_forward_embedding = FlairEmbeddings("multi-forward")
    flair_backward_embedding = FlairEmbeddings("multi-backward")

    # init multilingual BERT
    bert_embedding = BertEmbeddings("bert-base-multilingual-cased")

    return StackedEmbeddings(
        embeddings=[flair_forward_embedding,
                    flair_backward_embedding,
                    bert_embedding]
    )


def process_with_flair(text):
    """Process text to create embeddings."""
    sentence = Sentence(text)
    combine_embeddings().embed(sentence)
    return sentence
