#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `spacy` functionality."""
import pytest
import spacy
from spacy.util import get_lang_class


@pytest.mark.parametrize("text", u"This is a sentence. This is another sentence.")
def test_sentence_tokenization(text):
    """Check if sentence is tokenized properly"""
    nlp = spacy.load("en")
    doc = nlp(text)
    sents = list(doc.sents)
    assert len(sents) == 2
    assert sents[0].text == "This is a sentence."
    assert sents[1].text == "This is another sentence."
