class Board:
    def __init__(self):
        self.properties = ["Old Kent Rd",
                           "Whitechapel Rd",
                           "The Angel Islington",
                           "Euston Rd",
                           "Pentonville Rd",
                           "Pall Mall",
                           "Whitehall",
                           "Northumberland Ave.",
                           "Bow Street",
                           "Marlborough Street",
                           "Vine Street",
                           "Strand",
                           "Fleet Street",
                           "Trafalgar Square",
                           "Leicester Square",
                           "Coventry Street",
                           "Piccadilly",
                           "Regent Street",
                           "Oxford Street",
                           "Bond Street",
                           "Park Lane",
                           "Mayfair"]

        self.stations = ["King's Cross Station",
                         "Marylebone Station",
                         "Fenchurch Station",
                         "Liverpool Station", ]

        self.utilities = ["Electric Company",
                          "Water Works"]

    def list_properties(self):
        return self.properties

    def list_stations(self):
        return self.stations

    def list_utilies(self):
        return self.utilities
