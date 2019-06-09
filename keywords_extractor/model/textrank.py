# -*- coding: utf-8 -*-
"""Textrank module."""

from summa import keywords


def process_with_textrank(text):
    """Process text to extract keywords."""
    return keywords.keywords(text)
