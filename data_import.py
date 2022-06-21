from os.path import abspath, dirname, join

import pandas as pd
from sklearn.preprocessing import scale

BASE_DIR = dirname(abspath(__file__))


def import_discovery_data(scale_rna=True):
    """
    Imports discovery cohort's RNA-seq data.

    Parameters:
        scale_rna (bool, default:True): scale RNA-seq data

    Returns:
        data (pandas.DataFrame): RNA-seq measurements for discovery cohort
    """
    data = pd.read_csv(
        join(BASE_DIR, 'data', 'discovery_data.txt.gz'),
        index_col=0
    )

    if scale_rna:
        data[:] = scale(data)

    return data


def import_discovery_meta():
    """
    Imports discovery cohort's clinical metadata.

    Parameters:
        None.

    Returns:
        meta (pandas.DataFrame): clinical metadata for discovery cohort
    """
    meta = pd.read_csv(
        join(BASE_DIR, 'data', 'discovery_metadata.txt'),
        index_col=0
    )
    return meta


def import_validation_data(scale_rna=True):
    """
    Imports validation cohort's RNA-seq data.

    Parameters:
        scale_rna (bool, default:True): scale RNA-seq data

    Returns:
        data (pandas.DataFrame): RNA-seq measurements for validation cohort
    """
    data = pd.read_csv(
        join(BASE_DIR, 'data', 'validation_data.txt.gz'),
        index_col=0
    )

    if scale_rna:
        data[:] = scale(data)

    return data


def import_validation_meta():
    """
    Imports validation cohort's clinical metadata.

    Parameters:
        None.

    Returns:
        meta (pandas.DataFrame): clinical metadata for validation cohort
    """
    meta = pd.read_csv(
        join(BASE_DIR, 'data', 'validation_metadata.txt'),
        index_col=0
    )
    return meta
