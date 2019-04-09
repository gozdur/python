

from pprint import pprint




MonthConversions = {

    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

pprint(MonthConversions.get('Jan', "Not a valid key"))


