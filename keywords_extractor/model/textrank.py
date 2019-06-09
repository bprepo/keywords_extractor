# -*- coding: utf-8 -*-
"""Textrank module."""

from summa import keywords


def process_with_textrank(text):
    """Function for keyword extraction."""
    return keywords.keywords(text)
