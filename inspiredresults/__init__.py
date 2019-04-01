from inspiredresults.subjects import get_subjects
from inspiredresults.fieldnames import FIELD_NAMES
from inspiredresults.readers import get_reader, list_test_codes


VISITS = ("bl",)


def print_header():
    print(*FIELD_NAMES, sep=",")


def output_subject(subject):
    for visit in VISITS:
        for test in list_test_codes():
            reader = get_reader(test)
            try:
                result = reader(subject, visit)
            except FileNotFoundError:
                result = "MISSING"
            except NotImplementedError:
                result = "NOTIMPLEMENTED"
            print_row(subject, visit, test, result)


def print_row(subject, visit, test, result):
    row = (
        f"{subject.site},{subject.type},{subject.id},{subject.age},"
        f"{subject.gender},{visit},{subject.scan_date},{test},{result}"
    )
    print(row)


def main():
    print_header()
    for subject in get_subjects():
        output_subject(subject)
