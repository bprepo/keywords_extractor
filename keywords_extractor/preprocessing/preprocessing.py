"""Preprocessing module."""

import spacy


def load_model(model_name="en"):
    """Load different spacy models."""
    return spacy.load(model_name)


def read_file(path, encoding="utf8"):
    """Load text files."""
    return open(path, encoding=encoding).read()


def get_doc(nlp, text):
    """Create spacy document object."""
    return nlp(text)


def preprocess(path, model_name):
    """Start preprocessing."""
    return get_doc(load_model(model_name), read_file(path))
