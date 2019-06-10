# -*- coding: utf-8 -*-
"""gensim module."""

from gensim.summarization import keywords, mz_keywords


def process_with_gensim(text):
    """Process text to extract keywords."""
    return keywords(text)


# Beta - this functionality has a lot of bugs
def process_with_gensim_mz(text):
    """Process text to extract keywords."""
    return mz_keywords(text, blocksize=128)
