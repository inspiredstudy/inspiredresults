import sys
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
            except Exception as e:
                result = "ERROR"
                err_msg = "Exception reading {1} for {0.site}/{0.type}/{0.id}: {2!r}".format(
                    subject,
                    test,
                    e
                )
                print(err_msg, file=sys.stderr)
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
