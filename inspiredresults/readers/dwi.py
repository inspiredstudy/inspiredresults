from inspiredresults.readers.helpers import path_to, TissueLabels, read_seg_file


def read_fa(subject, visit, tissue):
    reads_path = path_to(subject, visit) / "brain/dwi_fa_seg_stats.csv"
    reads = read_seg_file(reads_path)
    return "{0:0.2f}".format(reads[tissue].mean)


def fa_wm(subject, visit):
    return read_fa(subject, visit, TissueLabels.WM)


def fa_cgm(subject, visit):
    return read_fa(subject, visit, TissueLabels.CGM)


def fa_dgm(subject, visit):
    return read_fa(subject, visit, TissueLabels.DGM)


def fa_cerebellum(subject, visit):
    return read_fa(subject, visit, TissueLabels.CEREBELLUM)


def read_rd(subject, visit, tissue):
    reads_path = path_to(subject, visit) / "brain/dwi_rd1000_seg_stats.csv"
    reads = read_seg_file(reads_path)
    return "{0:0.2f}".format(reads[tissue].mean)


def rd_wm(subject, visit):
    return read_rd(subject, visit, TissueLabels.WM)


def rd_cgm(subject, visit):
    return read_rd(subject, visit, TissueLabels.CGM)


def rd_dgm(subject, visit):
    return read_rd(subject, visit, TissueLabels.DGM)


def rd_cerebellum(subject, visit):
    return read_rd(subject, visit, TissueLabels.CEREBELLUM)


def read_ad(subject, visit, tissue):
    reads_path = path_to(subject, visit) / "brain/dwi_ad1000_seg_stats.csv"
    reads = read_seg_file(reads_path)
    return "{0:0.2f}".format(reads[tissue].mean)


def ad_wm(subject, visit):
    return read_ad(subject, visit, TissueLabels.WM)


def ad_cgm(subject, visit):
    return read_ad(subject, visit, TissueLabels.CGM)


def ad_dgm(subject, visit):
    return read_ad(subject, visit, TissueLabels.DGM)


def ad_cerebellum(subject, visit):
    return read_ad(subject, visit, TissueLabels.CEREBELLUM)


def read_md(subject, visit, tissue):
    reads_path = path_to(subject, visit) / "brain/dwi_md1000_seg_stats.csv"
    reads = read_seg_file(reads_path)
    return "{0:0.2f}".format(reads[tissue].mean)


def md_wm(subject, visit):
    return read_md(subject, visit, TissueLabels.WM)


def md_cgm(subject, visit):
    return read_md(subject, visit, TissueLabels.CGM)


def md_dgm(subject, visit):
    return read_md(subject, visit, TissueLabels.DGM)


def md_cerebellum(subject, visit):
    return read_md(subject, visit, TissueLabels.CEREBELLUM)
