from enum import Enum
from collections import namedtuple
from pathlib import Path


class TissueLabels(Enum):
    CSF = 1
    CGM = 2
    WM = 3
    DGM = 4
    CEREBELLUM = 5


TissueProperties = namedtuple("TissueProperties", ("mean", "std", "volume"))

reads_cache = {}


def path_to(subject, visit):
    p = Path("/trials/INSPIRED/scans/")
    p = p / "{0:02d}".format(subject.site)
    p = p / subject.type
    p = p / "{0:03d}".format(subject.id)
    p = p / visit
    return p


def read_seg_file(p):
    if p not in reads_cache:
        reads = {}
        with p.open() as f:
            for line in f:
                if line == "\n":
                    continue
                elif line == "ID\tLabel\tMean\tStd\tVolume\n":
                    continue
                _, label, mean, std, volume = line.strip().split("\t")
                label = int(label)
                mean = float(mean)
                std = float(std)
                volume = int(volume)
                reads[TissueLabels(label)] = TissueProperties(mean, std, volume)
        reads_cache[p] = reads
    return reads_cache[p]
