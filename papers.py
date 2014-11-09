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

    # converting json files for pycharm to read
    
    with open("example_entries.json", "r") as entries_reader:
        input_file = entries_reader.read()
        json_inputs = json.loads(input_file)
    with open("countries.json", "r") as country_reader:
        countries_file = country_reader.read()
        json_countries = json.loads(countries_file)
    with open("watchlist.json", "r") as watchlist_reader:
        watchlist_file = watchlist_reader.read()
        json_watchlist = json.loads(watchlist_file)


    # quarantine function

        for country in json_countries:
            if country.get("medical_advisory") != "":
                print("Quarantine")

     # reject function

        for ele in json_inputs:
            if "passport" in ele.keys() and "first_name" in ele.keys() and "last_name" in ele.keys() and "home" in \
            ele.keys() and "entry_reason" in ele.keys() and "from" in ele.keys():
                print("Accept")
            else:
                print("Reject")

        for country in json_countries:
            for visa in json_inputs:
                if key.get("entry_reason") == "visit":
                    if "visitor_visa_required" in country.values() == "1" and "date" > date.time:
                        print("Reject")
                    elif "visitor_visa_required" in country.values() == "1" and "date" < date.time:
                        print("Accept")
                    elif "visitor_visa_required" in country.values() == "0":
                        print("Accept")

                if key.get("entry_reason") == "transit":
                    if "transit_visa_required" in country.values() == "1" and "date" > date.time:
                        print("Reject")
                    elif "transit_visa_required" in country.values() == "1" and "date" < date.time:
                        print("Accept")
                    elif "transit_visa_required" in country.values() == "0":
                        print("Accept")

    # secondary function
                
        for item in jason_watchlist:
            if item.get("first_name" and "last_name") == ele.get("first_name" and "last_name"):
                print("Secondary")
            elif item.get("passport") == ele.get ("passport"):
                print("Secondary")
            else:
                print("Accept")
                        

    # accept function (do we need to have these stipulations included if whatever entry is left is automatically accept?)
    # if we have this function underneath the reject functions above, it will change priority order for these entries when they are not to be accepted)
    
for ele in json_inputs:
            if key.get("home") == "KAN"
                print("Accept")
            if key.get("entry_reason") == "returning" and key.get("home") == "KAN"
                print("Accept")

            else:
                print("Accept")

    
    return ["Reject"]
## not sure where to put the re.IGNORECASE method

    re.IGNORECASE("home" and "passport" and "first_name" and "last_name") etc.
    # or do we say "ignore all uppercase/lowercase discrepancies between all keys and all values in all json files?
    


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
