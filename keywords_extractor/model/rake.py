# -*- coding: utf-8 -*-
"""RAKE module."""

import RAKE


def process_with_RAKE(text):
    """Process text to extract keywords."""
    rake = RAKE.Rake(RAKE.SmartStopList())
    return rake.run(text, minCharacters=1, maxWords=1, minFrequency=1)
