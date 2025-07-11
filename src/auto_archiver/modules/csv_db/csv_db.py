import os
from auto_archiver.utils.custom_logger import logger
from csv import DictWriter
from dataclasses import asdict

from auto_archiver.core import Database
from auto_archiver.core import Metadata


class CSVDb(Database):
    """
    Outputs results to a CSV file
    """

    def done(self, item: Metadata, cached: bool = False) -> None:
        """archival result ready - should be saved to DB"""
        logger.success(f"DONE {item}")
        is_empty = not os.path.isfile(self.csv_file) or os.path.getsize(self.csv_file) == 0
        with open(self.csv_file, "a", encoding="utf-8") as outf:
            writer = DictWriter(outf, fieldnames=asdict(Metadata()))
            if is_empty:
                writer.writeheader()
            writer.writerow(asdict(item))
