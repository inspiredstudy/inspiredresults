from collections import namedtuple
import pyexcel_ods3

DEMOGRAPHICS_FILE = "/trials/INSPIRED/documents/demographics.ods"

Subject = namedtuple(
    "Subject",
    ("site", "type", "id", "dob", "age", "gender", "scan_date", "date_received")
)


def get_subjects():
    data = pyexcel_ods3.get_data(DEMOGRAPHICS_FILE)
    for r in data["Sheet1"][1:]:
        if not r:
            break
        if len(r) < 9:
            r.append(None)
        for i, v in enumerate(r):
            if not v:
                r[i] = "NA"
        yield Subject(*r[0:8])


if __name__ == "__main__":
    for s in get_subjects():
        print(s)
