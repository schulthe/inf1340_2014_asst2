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
    
    with open(input_file, "r") as entries_reader:
        input_file = entries_reader.read()
        json_inputs = json.loads(input_file)
    with open(countries_file, "r") as country_reader:
        countries_file = country_reader.read()
        json_countries = json.loads(countries_file)
    with open(watchlist_file, "r") as watchlist_reader:
        watchlist_file = watchlist_reader.read()
        json_watchlist = json.loads(watchlist_file)

    entry_list = []

    for ele in json_inputs:
        if ("passport") in ele.keys() and ("first_name") in ele.keys() and ("last_name") in ele.keys() and ("home") in \
            ele.keys() and ("entry_reason") in ele.keys() and ("from") in ele.keys():

    # quarantine function

            from_country = json_countries.get(ele.get["from"].get["country"]).get["medical_advisory"].lower()
            if from_country != "":
                entry_list.append("Quarantine")
            if "via" in ele.keys().lower():
                via_country = json_countries.get(ele.get["via"].get["country"]).get["medical_advisory"].lower()
                if via_country != "":
                    entry_list.append("Quarantine")

    # reject function

            if ele.get["entry_reason"].lower() == "visit":
                home_country = ele.get("home").get("country").lower()
                if json_countries.get(home_country).get("visitor_visa_required") == "1":
                    if "visa" in ele.keys:
                        if valid_date_format(ele.get("visa").get("date")) == False:
                            entry_list.append("Reject")
                        oldest_acceptable_visa_date = datetime.date.today() - datetime.date.timedelta(days = 730)
                        if ele.get("visa").get("date") < oldest_acceptable_visa_date.isoformat():
                            entry_list.append("Reject")
                else:
                    entry_list.append("Accept")

            if ele.get["entry_reason"] == "transit":
                home_country = ele.get("home").get("country").lower()
                if json_countries.get(home_country).get("transit_visa_required") == "1":
                    if "visa" in ele.keys:
                        if valid_date_format(ele.get["visa"].get["date"]) == False:
                            entry_list.append("Reject")
                        oldest_acceptable_visa_date = datetime.date.today() - datetime.date.timedelta(days = 730)
                        if ele.get["visa"].get["date"] < oldest_acceptable_visa_date.isoformat():
                            entry_list.append("Reject")
                else:
                    entry_list.append("Accept")

    # secondary function
                
            for item in json_watchlist:
                if item.get["first_name"].lower() == ele.get["first_name"].lower() and item.get["last_name"].lower() \
                == ele.get["last_name"].lower():
                    entry_list.append("Secondary")
                elif item.get["passport"].lower() == ele.get["passport"].lower():
                    entry_list.append("Secondary")
                else:
                    entry_list.append("Accept")
        else:
            entry_list.append("Reject")

 # priority function

        if entry_list == "Accept" and "Secondary" and "Reject" and "Quarantine":
            entry_list = "Quarantine"
        elif entry_list == "Accept" and "Secondary" and "Reject":
            entry_list = "Reject"
        elif entry_list == "Accept" and "Secondary" and "Quarantine":
            entry_list = "Quarantine"
        elif entry_list == "Secondary" and "Reject" and "Quarantine":
            entry_list = "Quarantine"
        elif entry_list == "Accept" and "Reject" and "Quarantine":
            entry_list = "Quarantine"
        elif entry_list == "Accept" and "Secondary":
            entry_list = "Secondary"
        elif entry_list == "Accept" and "Reject":
            entry_list = "Reject"
        elif entry_list == "Accept" and "Quarantine":
            entry_list = "Quarantine"
        elif entry_list == "Reject" and "Secondary":
            entry_list = "Reject"
        elif entry_list == "Quarantine" and "Secondary":
            entry_list = "Quarantine"
        elif entry_list == "Reject" and "Quarantine":
            entry_list = "Quarantine"
        else:
            entry_list = "Accept"

    return entry_list

def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_format = re.compile('^\w{5}-\w{5}$')

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