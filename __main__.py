# -*- coding: utf-8 -*-

"""Main module."""

import os
from keywords_extractor.data.preprocessing import preprocess
from keywords_extractor.model.textrank import process_with_textrank


def main(args=None):
    """Sample main app."""
    project_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_path, "data", "test_data.txt")
    doc = preprocess(file_path, "en")
    for sent in doc.sents:
        print(sent)
    print(process_with_textrank(doc.text))


if __name__ == "__main__":
    main()
