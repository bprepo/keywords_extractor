#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `spacy` functionality."""
import pytest
from spacy.util import get_lang_class
import spacy


@pytest.fixture(scope="session")
def en_tokenizer():
    """Check if spacy is installed properly."""
    return get_lang_class("en").Defaults.create_tokenizer()


def test_sentence_tokenization():
    """Check if sentence is tokenized properly"""
    nlp = spacy.load("en")
    doc = nlp(u"This is a sentence. This is another sentence.")
    sents = list(doc.sents)
    assert len(sents) == 2
    assert sents[0].text == "This is a sentence."
    assert sents[1].text == "This is another sentence."
