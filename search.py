import os
import re
from datetime import datetime as dt

from processors import *


class  StringFinder:

    def __init__(self, query):
        self.matches = []
        self.query = query

    def get_doc_matches(self, path):
        try:
            prc = DocProcessor(path)
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return None
        return prc.find(self.query)

    def search_folder(self, path):
        for entry in os.scandir(path):
            if entry.is_dir():
                self.search_folder(entry.path)
            if entry.is_file() and entry.name.endswith('.docx'):
                doc_matches = self.get_doc_matches(entry.path)
                if doc_matches:
                    self.matches.append((entry, doc_matches))

    def output_results(self):
        time_pattern = "%Y-%m-%d %H:%M:%S"
        query = self.query
        for file, hits in sorted(self.matches, key=lambda x: x[0].stat().st_mtime, reverse=True):
            last_modified = file.stat().st_mtime
            print(file.path, dt.fromtimestamp(last_modified).strftime(time_pattern))
            for hit in hits:
                print('\t' + re.sub(query, f'>>{query}<<', hit), '\n')
            print()