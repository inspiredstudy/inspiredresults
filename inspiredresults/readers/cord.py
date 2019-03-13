import xlrd


GM_CSA_MEAN_PATH = "/trials/INSPIRED/results/sct/GM_CSA/csa_mean.xls"
WM_CSA_MEAN_PATH = "/trials/INSPIRED/results/sct/WM_CSA/csa_mean.xls"
FA_IN_WM_PATH = "/trials/INSPIRED/results/sct/diffusion/FA_in_WM.xls"
FA_IN_DC_PATH = "/trials/INSPIRED/results/sct/diffusion/FA_in_DC.xls"
FA_IN_LF_PATH = "/trials/INSPIRED/results/sct/diffusion/FA_in_LF.xls"
FA_IN_VF_PATH = "/trials/INSPIRED/results/sct/diffusion/FA_in_VF.xls"


def gm_csa_mean(subject, visit):
    wb = xlrd.open_workbook(GM_CSA_MEAN_PATH)
    sheet = wb.sheet_by_index(0)
    row = 0
    while True:
        row += 1
        try:
            cells = sheet.row_values(row)
        except IndexError:
            break
        if not cells[1].startswith("/mounts/auto/trials/INSPIRED/scans"):
            continue
        site, type_, id_, row_visit = cells[1].split("/")[6:10]
        site = int(site)
        id_ = int(id_)
        if site == subject.site and id_ == subject.id and type_ == subject.type and visit == row_visit:
            return "{0:0.2f}".format(cells[6])
    return "MISSING"


def wm_csa_mean(subject, visit):
    wb = xlrd.open_workbook(WM_CSA_MEAN_PATH)
    sheet = wb.sheet_by_index(0)
    row = 0
    while True:
        row += 1
        try:
            cells = sheet.row_values(row)
        except IndexError:
            break
        if not cells[1].startswith("/mounts/auto/trials/INSPIRED/scans"):
            continue
        site, type_, id_, row_visit = cells[1].split("/")[6:10]
        site = int(site)
        id_ = int(id_)
        if site == subject.site and id_ == subject.id and type_ == subject.type and visit == row_visit:
            return "{0:0.2f}".format(cells[6])
    return "MISSING"


def fa_in_wm_mean(subject, visit):
    wb = xlrd.open_workbook(FA_IN_WM_PATH)
    sheet = wb.sheet_by_index(0)
    row = 0
    while True:
        row += 1
        try:
            cells = sheet.row_values(row)
        except IndexError:
            break
        if not cells[1].startswith("/mounts/auto/trials/INSPIRED/scans"):
            continue
        site, type_, id_, row_visit = cells[1].split("/")[6:10]
        site = int(site)
        id_ = int(id_)
        if site == subject.site and id_ == subject.id and type_ == subject.type and visit == row_visit:
            return "{0:0.2f}".format(cells[8])
    return "MISSING"


def fa_in_dc_mean(subject, visit):
    wb = xlrd.open_workbook(FA_IN_DC_PATH)
    sheet = wb.sheet_by_index(0)
    row = 0
    while True:
        row += 1
        try:
            cells = sheet.row_values(row)
        except IndexError:
            break
        if not cells[1].startswith("/mounts/auto/trials/INSPIRED/scans"):
            continue
        site, type_, id_, row_visit = cells[1].split("/")[6:10]
        site = int(site)
        id_ = int(id_)
        if site == subject.site and id_ == subject.id and type_ == subject.type and visit == row_visit:
            return "{0:0.2f}".format(cells[8])
    return "MISSING"


def fa_in_lf_mean(subject, visit):
    wb = xlrd.open_workbook(FA_IN_LF_PATH)
    sheet = wb.sheet_by_index(0)
    row = 0
    while True:
        row += 1
        try:
            cells = sheet.row_values(row)
        except IndexError:
            break
        if not cells[1].startswith("/mounts/auto/trials/INSPIRED/scans"):
            continue
        site, type_, id_, row_visit = cells[1].split("/")[6:10]
        site = int(site)
        id_ = int(id_)
        if site == subject.site and id_ == subject.id and type_ == subject.type and visit == row_visit:
            return "{0:0.2f}".format(cells[8])
    return "MISSING"


def fa_in_vf_mean(subject, visit):
    wb = xlrd.open_workbook(FA_IN_VF_PATH)
    sheet = wb.sheet_by_index(0)
    row = 0
    while True:
        row += 1
        try:
            cells = sheet.row_values(row)
        except IndexError:
            break
        if not cells[1].startswith("/mounts/auto/trials/INSPIRED/scans"):
            continue
        site, type_, id_, row_visit = cells[1].split("/")[6:10]
        site = int(site)
        id_ = int(id_)
        if site == subject.site and id_ == subject.id and type_ == subject.type and visit == row_visit:
            return "{0:0.2f}".format(cells[8])
    return "MISSING"
