# -*- coding: utf-8 -*-
"""Textrank module."""

from summa import keywords


def process_with_textrank(text):
    """Function to process text rank with full text."""
    return keywords.keywords(text)
