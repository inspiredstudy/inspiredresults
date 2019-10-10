from inspiredresults.readers.helpers import path_to


def brain_vol(subject, visit):
    visit_path = path_to(subject, visit)
    girona_path = visit_path / 'brain' / 'gironax' / 'gironax.txt'
    with girona_path.open() as f:
        for l in f:
            if l.startswith("Brain volume"):
                nbv, ubv = l[13:].strip().split()
                nbv = "{0:0.2f}".format(float(nbv) / 1000.0)
                break
    return nbv


def cortical_gm_vol(subject, visit):
    visit_path = path_to(subject, visit)
    girona_path = visit_path / 'brain' / 'gironax' / 'gironax.txt'
    with girona_path.open() as f:
        for l in f:
            if l.startswith("CGM"):
                normvol, _ = l[13:].strip().split()
                normvol = "{0:0.2f}".format(float(normvol) / 1000.0)
                break
    return normvol


def deep_gm_vol(subject, visit):
    visit_path = path_to(subject, visit)
    girona_path = visit_path / 'brain' / 'gironax' / 'gironax.txt'
    with girona_path.open() as f:
        for l in f:
            if l.startswith("DGM"):
                normvol, _ = l[13:].strip().split()
                normvol = "{0:0.2f}".format(float(normvol) / 1000.0)
                break
    return normvol


def gm_vol(subject, visit):
    visit_path = path_to(subject, visit)
    girona_path = visit_path / 'brain' / 'gironax' / 'gironax.txt'
    with girona_path.open() as f:
        for l in f:
            if l.startswith("GM"):
                normvol, _ = l[13:].strip().split()
                normvol = "{0:0.2f}".format(float(normvol) / 1000.0)
                break
    return normvol


def wm_vol(subject, visit):
    visit_path = path_to(subject, visit)
    girona_path = visit_path / 'brain' / 'gironax' / 'gironax.txt'
    with girona_path.open() as f:
        for l in f:
            if l.startswith("WM"):
                normvol, _ = l[13:].strip().split()
                normvol = "{0:0.2f}".format(float(normvol) / 1000.0)
                break
    return normvol


def scaling_factor(subject, visit):
    visit_path = path_to(subject, visit)
    girona_path = visit_path / 'brain' / 'gironax' / 'gironax.txt'
    with girona_path.open() as f:
        for l in f:
            if l.startswith("Scaling factor"):
                _, factor = l.strip().split("=")
                factor = "{0:0.2f}".format(float(factor))
                break
    return factor
