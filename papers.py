#!/usr/bin/env python3

""" Computer-based immigration office for Kanadia """

__author__ = 'Sarah-Anne Schultheis, Sonia Duda'
__email__ = "sarah.schultheis@mail.utoronto.ca, sonia.duda@mail.utoronto.ca"

__copyright__ = "2014 Sarah-Anne Schultheis, Sonia Duda"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import re
import datetime
import json

def decide(input_file, watchlist_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject", "Secondary", and "Quarantine"
    """

    # reject if incomplete entry

    # quarantine if medical advisory in "from" country

    # secondary if on watchlist

    # reason
        # accept if return home and citizen, if no med advisory (Q) or watchlist (S)
        # accept if transit, if country needs transit visa, if valid (less than 2 years) or R
        # accept if visiting, if country needs visitor visa, if valid (less than 2 years) or R

    # conflict order - Q, R, S, A

with open("example_entries.json", "r") as file_reader:
    input_file = file_reader.read()
with open ("watchlist.json", "r") as file_reader:
    watchlist_file = file_reader.read()
with open ("countries.json", "r") as file_reader:
    countries_file = file_reader.read()

if file_contents.key ("first_name") == "":
    return ("Reject")

for passport in file_contents:
    print(passport)
file_contents = file_reader.read()


    return ["Reject"]


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_format = re.compile('.{5}-.{5}-.{5}-.{5}-.{5}')

    if passport_format.match(passport_number):
        return True
    else:
        return False


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
