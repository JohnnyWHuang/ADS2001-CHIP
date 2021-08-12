"""
Functions for preprocessing dataframes within the CHIP dataset
"""
import re
import pandas as pd

def remove_redundant(dataframe):
    dataframe = dataframe[(dataframe.chipOrControl != "Blank") & (dataframe.chipOrControl != "Unknown")]
    dataframe = dataframe.dropna(subset=['chipOrControl'])
    dataframe.drop(['d.barcode'], axis=1, inplace=True)
    dataframe.drop_duplicates(inplace=True)
    return dataframe


def loci_split(dataframe):
    """
    Separates loci into three separate columns: chromosome, chromosome location and nucleotide.
    """
    chromosome = []
    chromosome_location = []
    nucleotide = []

    for location_string in dataframe.loci.array:
        separated = re.split(r"[:_]+", location_string)
        chromosome.append(separated[0])
        chromosome_location.append(separated[1])
        nucleotide.append(separated[2])

    dataframe['chromosome'] = pd.Series(chromosome).values
    dataframe['chromosome_loc'] = pd.Series(chromosome_location).values
    dataframe['nucleotide'] = pd.Series(nucleotide).values
    dataframe.drop(['loci'], axis=1, inplace=True)

    return dataframe


def ratio_to_int(string):
    """
    Converts a string datatype into an integer, where the string is of the format "x:y", where
    x and y are integers.
    Output is x / y (if y = 0, return 0).
    """
    a, b = string.split(":")
    if int(b) == 0:
        return 0
    else:
        return int(a) / int(b)

def convert_ratios(dataframe, variables):
    for var in variables:
        arr = [ratio_to_int(ratio) for ratio in dataframe[var].array]
        dataframe[var] = pd.Series(arr).values
    return dataframe

def get_len(string):
    a, b = string.split("/")
    if abs(a - b) > 1:

        return len(string) - 1

def nucleotide_length(dataframe):
    """
    Separates loci into three separate columns: chromosome, chromosome location and nucleotide.
    """
    chromosome = []
    chromosome_location = []
    nucleotide = []

    for location_string in dataframe.loci.array:
        separated = re.split(r"[:_]+", location_string)
        chromosome.append(separated[0])
        chromosome_location.append(separated[1])
        nucleotide.append(separated[2])

    dataframe['chromosome'] = pd.Series(chromosome).values
    dataframe['chromosome_loc'] = pd.Series(chromosome_location).values
    dataframe['nucleotide'] = pd.Series(nucleotide).values
    dataframe.drop(['loci'], axis=1, inplace=True)

    return dataframe
