# -*- coding: utf-8 -*-

"""Main module."""

import os

from keywords_extractor.model.extractors import GensimExtractor, RakeExtractor
from keywords_extractor.model.extractors import TextrankExtractor
from keywords_extractor.model.flair import process_with_flair
from keywords_extractor.preprocessing.preprocessing import preprocess


def main(args=None):
    """Sample main app."""
    project_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_path, "data", "test_data.txt")
    doc = preprocess(file_path, "en")
    textrank = TextrankExtractor(doc.text)
    rake = RakeExtractor(doc.text)
    gensim = GensimExtractor(doc.text)

    print("textrank: \n", textrank.keywords)
    print("rake: \n", rake.keywords)
    print("gensim: \n", gensim.keywords)

    flair = process_with_flair(doc.text)
    for sent in flair:
        print(sent)
        print(sent.embedding)


if __name__ == "__main__":
    main()
