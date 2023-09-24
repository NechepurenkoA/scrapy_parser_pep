import csv
import datetime as dt

from constants import BASE_DIR, DATETIME_FORMAT, FIELD_NAMES
from pep_parse.utils import make_rows


class PepParsePipeline:
    def open_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        self.file_path = results_dir / file_name
        self.status_count = {}
        self.total = 0

    def process_item(self, item, spider):
        status = item['status']
        if status not in self.status_count:
            self.status_count[status] = 1
        elif status in self.status_count:
            self.status_count[status] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        rows = make_rows(self.status_count, self.total)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader()
            writer.writerows(rows)
