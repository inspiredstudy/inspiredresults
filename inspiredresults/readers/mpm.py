from inspiredresults.readers.helpers import path_to, TissueLabels, read_seg_file


def read_mt(subject, visit, tissue):
    reads_path = path_to(subject, visit) / "brain/mpm_MT_seg_stats.csv"
    reads = read_seg_file(reads_path)
    return "{0:0.2f}".format(reads[tissue].mean)


def mt_wm(subject, visit):
    return read_mt(subject, visit, TissueLabels.WM)


def mt_cgm(subject, visit):
    return read_mt(subject, visit, TissueLabels.CGM)


def mt_dgm(subject, visit):
    return read_mt(subject, visit, TissueLabels.DGM)


def mt_cerebellum(subject, visit):
    return read_mt(subject, visit, TissueLabels.CEREBELLUM)


def read_a(subject, visit, tissue):
    reads_path = path_to(subject, visit) / "brain/mpm_A_seg_stats.csv"
    reads = read_seg_file(reads_path)
    return "{0:0.2f}".format(reads[tissue].mean)


def a_wm(subject, visit):
    return read_a(subject, visit, TissueLabels.WM)


def a_cgm(subject, visit):
    return read_a(subject, visit, TissueLabels.CGM)


def a_dgm(subject, visit):
    return read_a(subject, visit, TissueLabels.DGM)


def a_cerebellum(subject, visit):
    return read_a(subject, visit, TissueLabels.CEREBELLUM)


def read_r1_unicort(subject, visit, tissue):
    reads_path = path_to(subject, visit) / "brain/mpm_R1_UNICORT_seg_stats.csv"
    reads = read_seg_file(reads_path)
    return "{0:0.2f}".format(reads[tissue].mean)


def r1_unicort_wm(subject, visit):
    return read_r1_unicort(subject, visit, TissueLabels.WM)


def r1_unicort_cgm(subject, visit):
    return read_r1_unicort(subject, visit, TissueLabels.CGM)


def r1_unicort_dgm(subject, visit):
    return read_r1_unicort(subject, visit, TissueLabels.DGM)


def r1_unicort_cerebellum(subject, visit):
    return read_r1_unicort(subject, visit, TissueLabels.CEREBELLUM)


def read_r2s_ols(subject, visit, tissue):
    reads_path = path_to(subject, visit) / "brain/mpm_R2s_OLS_seg_stats.csv"
    reads = read_seg_file(reads_path)
    return "{0:0.2f}".format(reads[tissue].mean)


def r2s_ols_wm(subject, visit):
    return read_r2s_ols(subject, visit, TissueLabels.WM)


def r2s_ols_cgm(subject, visit):
    return read_r2s_ols(subject, visit, TissueLabels.CGM)


def r2s_ols_dgm(subject, visit):
    return read_r2s_ols(subject, visit, TissueLabels.DGM)


def r2s_ols_cerebellum(subject, visit):
    return read_r2s_ols(subject, visit, TissueLabels.CEREBELLUM)
