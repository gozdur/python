

from pprint import pprint




MonthConversions = {

    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

pprint(MonthConversions.get('Dec', "Not a valid key"))


