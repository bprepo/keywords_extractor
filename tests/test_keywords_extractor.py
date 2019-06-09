#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `keywords_extractor` package."""
import pytest
from spacy.util import get_lang_class


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


@pytest.fixture(scope="session")
def en_tokenizer():
    """Check if spacy is installed properly"""
    return get_lang_class("en").Defaults.create_tokenizer()
