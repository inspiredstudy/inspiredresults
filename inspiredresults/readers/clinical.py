import pandas as pd


TORONTO_RESULTS_FILENAME = '/trials/INSPIRED/results/clinical/toronto_clinical_results_20190903.csv'
ZURICH_RESULTS_FILENAME = '/trials/INSPIRED/results/clinical/zurich_clinical_results_20190311_clean.csv'
cached_dataframes = {}


def _read_and_clean_zurich(filename):
    df = pd.read_csv(
        filename,
        sep=';',
        parse_dates=['Date of Birth', 'Date of surgery', 'Date of Informed Consent'],
        true_values=['Yes', 'Complete'],
        false_values=['No']
    )

    # clean up column names
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

    # merge baseline and screening
    screening_cols = [
        'inspired_id',
        'pid',
        'date_of_birth',
        'sex',
        'height_(m)',
        'weight_(kg)',
        'previous_surgery_(cervical_spine)',
        'date_of_surgery',
        'informed_consent',
        'date_of_informed_consent',
        'comment',
        'complete?'
    ]

    baseline_cols = [c for c in df.columns if c not in screening_cols and c != 'record_id']

    screening = df[df.event_name == 'Screening']
    baseline = df[df.event_name == 'Baseline']

    df = pd.merge(screening, baseline, on='record_id')

    screening_cols = [c + '_x' for c in screening_cols]
    baseline_cols = [c + '_y' for c in baseline_cols]

    df = df.loc[:, screening_cols + baseline_cols]

    df.columns = [c[:-2] for c in df.columns]

    # set identifier columns
    df['site'] = 2
    df['subject'] = df.inspired_id.str.split('_', expand=True)[1].astype(int)
    df['type'] = df.inspired_id.str.split('_', expand=True)[2].str.lower()

    # harmonize measures
    df['nurick'] = df.nurick_score.str.split(' ', expand=True)[0].astype(float)

    return df


def _read_and_clean_toronto(filename):
    df = pd.read_csv(
        filename,
        sep=',',
        header=1,
        parse_dates=['DOB', 'Scan date', 'Assessment date'],
        na_values=["NA", "?"]
    )

    # clean up column names
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

    # set identifier columns
    df['site'] = 1
    df['subject'] = df.id.str.split('-', expand=True)[1].astype(int)
    df['type'] = 'csm'
    df.loc[df.id == 'INS-012', 'type'] = 'sci'
    df.loc[df.id == 'INS-003', 'type'] = 'sci'

    # harmonize measures
    df.rename(columns={
        'quickdash': 'dash_score',
        'nurick_grade': 'nurick',
        'mjoa': 'total_mjoa',
        'height': 'height_(m)',
        'weight': 'weight_(kg)',
    }, inplace=True)
    df['total_l+r'] = (
        df['r_mrc_strength'] +
        df['l_mrc_strength'] +
        df['r_sensation'] +
        df['l_sensation'] +
        df['r_qual_prehension'] +
        df['l_qual_prehension'] +
        df['r_quan_prehension_(30)'] +
        df['l_quan_prehension_(30)']
    )

    df['height_(m)'] = df['height_(m)'] / 100.0
    df['weight_(kg)'] = round(df['weight_(kg)'] * 0.453592, 1)

    return df


def _read_raw_results(site):
    if site == 1:
        return _read_and_clean_toronto(TORONTO_RESULTS_FILENAME)
    elif site == 2:
        return _read_and_clean_zurich(ZURICH_RESULTS_FILENAME)
    else:
        raise ValueError('Invalid site number')


def _get_value(subject, visit, column):
    if cached_dataframes.get(subject.site) is None:
        cached_dataframes[subject.site] = _read_raw_results(subject.site)
    df = cached_dataframes[subject.site]
    try:
        return df.loc[
            (df.subject == subject.id) &
            (df.site == subject.site) &
            (df.type == subject.type),
            column
        ].iloc[0]
    except IndexError:
        raise KeyError("No values found for {0}".format(column))


def grassp(subject, visit):
    return _get_value(subject, visit, 'total_l+r')


def scim(subject, visit):
    return _get_value(subject, visit, 'total_scim-score')


def dash(subject, visit):
    return _get_value(subject, visit, 'dash_score')


def dash_work(subject, visit):
    return _get_value(subject, visit, 'dash_work_score')


def dash_sport_music(subject, visit):
    return _get_value(subject, visit, 'dash_sport/music_score')
