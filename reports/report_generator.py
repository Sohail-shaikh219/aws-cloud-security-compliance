import csv
from config import REPORT_FILE_PATH


def generate_csv_report(findings):
    with open(REPORT_FILE_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Resource", "Issue", "Risk Level"])
        writer.writerows(findings)
