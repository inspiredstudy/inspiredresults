from inspiredresults.readers.helpers import path_to
from csv import DictReader
import pandas as pd


def gm_csa_mean(subject, visit):
    csa_path = path_to(subject, visit) / "cord/sct_processing/t2s/gm_csa.csv"
    csa_read = DictReader(csa_path.open("r"))
    row = next(csa_read)
    mean_area = row["MEAN(CSA [mm^2])"]
    return "{0:0.2f}".format(float(mean_area))


def wm_csa_mean(subject, visit):
    csa_path = path_to(subject, visit) / "cord/sct_processing/t2s/wm_csa.csv"
    csa_read = DictReader(csa_path.open("r"))
    row = next(csa_read)
    mean_area = row["MEAN(CSA [mm^2])"]
    return "{0:0.2f}".format(float(mean_area))


def _dwi_read(subject, visit, contrast, tract):
    filename = "{0}_in_{1}.csv".format(contrast.upper(), tract.upper())
    read_path = path_to(subject, visit) / "cord/sct_processing/dwi" / filename
    df = pd.read_csv(read_path)
    res = df["MAP()"].mean()
    if contrast in ["AD", "RD", "MD"]:
        res *= 1000.0
    return "{0:0.2f}".format(res)


def fa_in_wm_mean(subject, visit):
    return _dwi_read(subject, visit, "FA", "WM")


def fa_in_dc_mean(subject, visit):
    return _dwi_read(subject, visit, "FA", "DC")


def fa_in_lf_mean(subject, visit):
    return _dwi_read(subject, visit, "FA", "LF")


def fa_in_vf_mean(subject, visit):
    return _dwi_read(subject, visit, "FA", "VF")


def md_in_wm_mean(subject, visit):
    return _dwi_read(subject, visit, "MD", "WM")


def md_in_dc_mean(subject, visit):
    return _dwi_read(subject, visit, "MD", "DC")


def md_in_lf_mean(subject, visit):
    return _dwi_read(subject, visit, "MD", "LF")


def md_in_vf_mean(subject, visit):
    return _dwi_read(subject, visit, "MD", "VF")


def ad_in_wm_mean(subject, visit):
    return _dwi_read(subject, visit, "AD", "WM")


def ad_in_dc_mean(subject, visit):
    return _dwi_read(subject, visit, "AD", "DC")


def ad_in_lf_mean(subject, visit):
    return _dwi_read(subject, visit, "AD", "LF")


def ad_in_vf_mean(subject, visit):
    return _dwi_read(subject, visit, "AD", "VF")


def rd_in_wm_mean(subject, visit):
    return _dwi_read(subject, visit, "RD", "WM")


def rd_in_dc_mean(subject, visit):
    return _dwi_read(subject, visit, "RD", "DC")


def rd_in_lf_mean(subject, visit):
    return _dwi_read(subject, visit, "RD", "LF")


def rd_in_vf_mean(subject, visit):
    return _dwi_read(subject, visit, "RD", "VF")
