from inspiredresults.readers import cord, dwi, mpm, clinical, gironax

READERS = {
    'BRAIN_MT_WM': mpm.mt_wm,
    'BRAIN_MT_CGM': mpm.mt_cgm,
    'BRAIN_MT_DGM': mpm.mt_dgm,
    'BRAIN_MT_CEREBELLUM': mpm.mt_cerebellum,
    'BRAIN_A_WM': mpm.a_wm,
    'BRAIN_A_CGM': mpm.a_cgm,
    'BRAIN_A_DGM': mpm.a_dgm,
    'BRAIN_A_CEREBELLUM': mpm.a_cerebellum,
    'BRAIN_R1_UNICORT_WM': mpm.r1_unicort_wm,
    'BRAIN_R1_UNICORT_CGM': mpm.r1_unicort_cgm,
    'BRAIN_R1_UNICORT_DGM': mpm.r1_unicort_dgm,
    'BRAIN_R1_UNICORT_CEREBELLUM': mpm.r1_unicort_cerebellum,
    'BRAIN_R2s_OLS_WM': mpm.r2s_ols_wm,
    'BRAIN_R2s_OLS_CGM': mpm.r2s_ols_cgm,
    'BRAIN_R2s_OLS_DGM': mpm.r2s_ols_dgm,
    'BRAIN_R2s_OLS_CEREBELLUM': mpm.r2s_ols_cerebellum,
    'BRAIN_FA_WM': dwi.fa_wm,
    'BRAIN_FA_CGM': dwi.fa_cgm,
    'BRAIN_FA_DGM': dwi.fa_dgm,
    'BRAIN_FA_CEREBELLUM': dwi.fa_cerebellum,
    'BRAIN_MD_WM': dwi.md_wm,
    'BRAIN_MD_CGM': dwi.md_cgm,
    'BRAIN_MD_DGM': dwi.md_dgm,
    'BRAIN_MD_CEREBELLUM': dwi.md_cerebellum,
    'BRAIN_RD_WM': dwi.rd_wm,
    'BRAIN_RD_CGM': dwi.rd_cgm,
    'BRAIN_RD_DGM': dwi.rd_dgm,
    'BRAIN_RD_CEREBELLUM': dwi.rd_cerebellum,
    'BRAIN_AD_WM': dwi.ad_wm,
    'BRAIN_AD_CGM': dwi.ad_cgm,
    'BRAIN_AD_DGM': dwi.ad_dgm,
    'BRAIN_AD_CEREBELLUM': dwi.ad_cerebellum,
    'BRAIN_NORMALIZED_VOLUME': gironax.brain_vol,
    'BRAIN_NORMALIZED_CGM_VOL': gironax.cortical_gm_vol,
    'BRAIN_NORMALIZED_DGM_VOL': gironax.deep_gm_vol,
    'BRAIN_NORMALIZED_GM_VOL': gironax.gm_vol,
    'BRAIN_NORMALIZED_WM_VOL': gironax.wm_vol,
    'BRAIN_VOL_SCALING_FACTOR': gironax.scaling_factor,
    'CORD_GM_CSA': cord.gm_csa_mean,
    'CORD_WM_CSA': cord.wm_csa_mean,
    'CORD_FA_WM': cord.fa_in_wm_mean,
    'CORD_FA_DC': cord.fa_in_dc_mean,
    'CORD_FA_LF': cord.fa_in_lf_mean,
    'CORD_FA_VF': cord.fa_in_vf_mean,
    'CORD_MD_WM': cord.md_in_wm_mean,
    'CORD_MD_DC': cord.md_in_dc_mean,
    'CORD_MD_LF': cord.md_in_lf_mean,
    'CORD_MD_VF': cord.md_in_vf_mean,
    'CORD_AD_WM': cord.ad_in_wm_mean,
    'CORD_AD_DC': cord.ad_in_dc_mean,
    'CORD_AD_LF': cord.ad_in_lf_mean,
    'CORD_AD_VF': cord.ad_in_vf_mean,
    'CORD_RD_WM': cord.rd_in_wm_mean,
    'CORD_RD_DC': cord.rd_in_dc_mean,
    'CORD_RD_LF': cord.rd_in_lf_mean,
    'CORD_RD_VF': cord.rd_in_vf_mean,
    'CLIN_GRASSP': clinical.grassp,
    'CLIN_GRASSP_SENSATION_R': clinical.grassp_sensation_r,
    'CLIN_GRASSP_SENSATION_L': clinical.grassp_sensation_l,
    'CLIN_GRASSP_QUAL_PREHENSION_R': clinical.grassp_qual_prehension_r,
    'CLIN_GRASSP_QUAL_PREHENSION_L': clinical.grassp_qual_prehension_l,
    'CLIN_GRASSP_QUAN_PREHENSION_R': clinical.grassp_quan_prehension_r,
    'CLIN_GRASSP_QUAN_PREHENSION_L': clinical.grassp_quan_prehension_l,
    'CLIN_SCIM': clinical.scim,
    'CLIN_DASH': clinical.dash,
    'CLIN_DASH_WORK': clinical.dash_work,
    'CLIN_DASH_SPORT_MUSIC': clinical.dash_sport_music,
    'CLIN_NURICK': clinical.nurick,
    'CLIN_MJOA': clinical.mjoa,
    'CLIN_HEIGHT': clinical.height,
    'CLIN_WEIGHT': clinical.weight,
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
