import pandas as pd


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

    df['site'] = 2
    df['subject'] = df.inspired_id.str.split('_', expand=True)[1].astype(int)
    df['type'] = df.inspired_id.str.split('_', expand=True)[2].str.lower()

    return df


def _read_raw_results(site):
    if site == 1:
        raise FileNotFoundError
    elif site == 2:
        return _read_and_clean_zurich(
            '/trials/INSPIRED/results/clinical/zurich_clinical_results_20190311_clean.csv'
        )
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
        return None


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
