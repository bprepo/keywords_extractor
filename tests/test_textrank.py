#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `textrank` functionality."""
import pytest
from summa import keywords


def test_if_keywords():
    """Test if there are keywords"""
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    assert len(keywords.keywords(text)) > 0

