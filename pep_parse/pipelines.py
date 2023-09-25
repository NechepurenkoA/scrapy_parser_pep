import csv
import datetime as dt
import logging

from constants import (
    BASE_DIR,
    RESULTS_DIR_POSTFIX,
    DATETIME_FORMAT,
    FIELD_NAMES
)
from pep_parse.utils import make_rows


class PepParsePipeline:
    def open_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR_POSTFIX
        try:
            results_dir.mkdir(exist_ok=True)
        except (FileNotFoundError, OSError) as exc:
            logging.CRITICAL(
                f'Произошла ошибка при создании папки results: {exc}'
            )
            return
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        self.file_path = results_dir / file_name
        self.status_count = {}

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] = self.status_count.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        total = sum(self.status_count.values())
        rows = make_rows(self.status_count, total)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader()
            writer.writerows(rows)
