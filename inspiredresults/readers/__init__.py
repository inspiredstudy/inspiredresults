from inspiredresults.readers import cord, dwi, mpm

READERS = {
    'MT_WM': mpm.mt_wm,
    'MT_CGM': mpm.mt_cgm,
    'MT_DGM': mpm.mt_dgm,
    'MT_CEREBELLUM': mpm.mt_cerebellum,
    'A_WM': mpm.a_wm,
    'A_CGM': mpm.a_cgm,
    'A_DGM': mpm.a_dgm,
    'A_CEREBELLUM': mpm.a_cerebellum,
    'R1_UNICORT_WM': mpm.r1_unicort_wm,
    'R1_UNICORT_CGM': mpm.r1_unicort_cgm,
    'R1_UNICORT_DGM': mpm.r1_unicort_dgm,
    'R1_UNICORT_CEREBELLUM': mpm.r1_unicort_cerebellum,
    'R2s_OLS_WM': mpm.r2s_ols_wm,
    'R2s_OLS_CGM': mpm.r2s_ols_cgm,
    'R2s_OLS_DGM': mpm.r2s_ols_dgm,
    'R2s_OLS_CEREBELLUM': mpm.r2s_ols_cerebellum,
    'FA_WM': dwi.fa_wm,
    'FA_CGM': dwi.fa_cgm,
    'FA_DGM': dwi.fa_dgm,
    'FA_CEREBELLUM': dwi.fa_cerebellum,
    'MD_WM': dwi.md_wm,
    'MD_CGM': dwi.md_cgm,
    'MD_DGM': dwi.md_dgm,
    'MD_CEREBELLUM': dwi.md_cerebellum,
    'RD_WM': dwi.rd_wm,
    'RD_CGM': dwi.rd_cgm,
    'RD_DGM': dwi.rd_dgm,
    'RD_CEREBELLUM': dwi.rd_cerebellum,
    'AD_WM': dwi.ad_wm,
    'AD_CGM': dwi.ad_cgm,
    'AD_DGM': dwi.ad_dgm,
    'AD_CEREBELLUM': dwi.ad_cerebellum,
    'CORD_GM_CSA_MEAN': cord.gm_csa_mean,
    'CORD_WM_CSA_MEAN': cord.wm_csa_mean,
    'CORD_FA_IN_WM_MEAN': cord.fa_in_wm_mean,
    'CORD_FA_IN_DC_MEAN': cord.fa_in_dc_mean,
    'CORD_FA_IN_LF_MEAN': cord.fa_in_lf_mean,
    'CORD_FA_IN_VF_MEAN': cord.fa_in_vf_mean,
}


def list_test_codes():
    return sorted(list(READERS.keys()))


def get_reader(test):
    try:
        r = READERS[test]
    except KeyError:
        raise NotImplementedError
    if r is None:
        raise NotImplementedError
    return r
