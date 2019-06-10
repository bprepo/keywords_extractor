#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `textrank` functionality."""
import pytest
import RAKE
from gensim.summarization import keywords as gen_keywords
from summa import keywords



@pytest.mark.parametrize(
    "text",
    [
        """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit, sed do
    eiusmod tempor incididunt ut labore
    et dolore magna aliqua."""
    ],
)
def test_if_keywords(text):
    """Test if there are keywords."""
    assert len(keywords.keywords(text)) > 0
    rake = RAKE.Rake(RAKE.SmartStopList())
    assert len(rake.run(text, minCharacters=1, maxWords=1, minFrequency=1)) > 0
    assert len(gen_keywords(text)) > 0
