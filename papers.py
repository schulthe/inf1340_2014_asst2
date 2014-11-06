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
    with open("example_entries.json", "r") as entries_reader:
        input_file = entries_reader.read()
        json_inputs = json.loads(input_file)

        for ele in json_inputs:
            if "passport" in ele.keys() and "first_name" in ele.keys() and "last_name" in ele.keys() and "home" in \
            ele.keys() and "entry_reason" in ele.keys() and "from" in ele.keys():

                # secondary if on watchlist
                with open("watchlist.json", "r") as watchlist_reader:
                    watchlist_file = watchlist_reader.read()
                    json_watchlist = json.loads(watchlist_file)

                    for item in json_watchlist:
                        if item.values() == ele.values() in json_inputs:

                            with open("countries.json", "r") as country_reader:
                                countries_file = country_reader.read()
                                json_countries = json.loads(countries_file)

                                # quarantine if medical advisory has value
                                for country in json_countries:
                                    if "medical_advisory" in country.values():
                                        print("Quarantine")

                                for country in json_countries:
                                    for visa in json_inputs:
                                        if "entry_reason" == "transit":
                                            if "transit_visa_required" in country.values() == "1" and "date" > date.time:
                                                print("Reject")
                                            elif "transit_visa_required" in country.values() == "1" and "date" < date.time:
                                                print("Accept")
                                            elif "transit_visa_required" in country.values() == "0":
                                                print("Accept")
                                        if "entry_reason" == "visit":
                                            if "visitor_visa_required" in country.values() == "1" and "date" > date.time:
                                                print("Reject")
                                            elif "visitor_visa_required" in country.values() == "1" and "date" < date.time:
                                                print("Accept")
                                            elif "visitor_visa_required" in country.values() == "0":
                                                print("Accept")
                        else:
                            print("Secondary")

    # conflict order - Q, R, S, A

            else:
                print("Reject")

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

decide("test_returning_citizen.json", "watchlist.json", "countries.json")