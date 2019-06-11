"""Extractors module."""

from abc import abstractmethod
import logging

from gensim.summarization import keywords as gensim_keywords
import RAKE
from summa import keywords as textrank_keywords


log = logging.getLogger("extractor")


class Extractors:
    """
    Abstract base class for all extractors.

    Every new type of class must implement these methods.
    """

    @property
    @abstractmethod
    def keywords(self):
        """Extract keywords from text."""
        pass


class RakeExtractor(Extractors):
    """Rake class to extract keywords."""

    def __init__(self, text):
        """Take a text to process."""
        super().__init__()
        self._text = text

    @property
    def keywords(self):
        """Process text to extract keywords."""
        rake = RAKE.Rake(RAKE.SmartStopList())
        self._keywords = rake.run(
            self._text, minCharacters=1, maxWords=1, minFrequency=1
        )
        return self._keywords


class TextrankExtractor(Extractors):
    """Textrank class to extract keywords."""

    def __init__(self, text):
        """Take a text to process."""
        super().__init__()
        self._text = text

    @property
    def keywords(self):
        """Process text to extract keywords."""
        self._keywords = textrank_keywords.keywords(self._text)
        return self._keywords


class GensimExtractor(Extractors):
    """Gensim class to extract keywords."""

    def __init__(self, text):
        """Take a text to process."""
        super().__init__()
        self._text = text

    @property
    def keywords(self):
        """Process text to extract keywords."""
        self._keywords = gensim_keywords(self._text)
        return self._keywords
