from enum import Enum


class TripReason(Enum):
    travail = 579
    sante = 546
    famille = 512
    handicap = 478
    judiciaire = 459
    missions = 438
    transit = 404
    animaux = 370
    courses = 304
    sport = 261
    rassemblement = 190
    demarche = 145


class Trip:
    def __init__(self, date, reasons):
        self.date = date
        self.reasons = reasons


class Profile:
    def __init__(self, firstname, lastname, birthday, placeofbirth, address, zipcode, city):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.placeofbirth = placeofbirth
        self.address = address
        self.zipcode = zipcode
        self.city = city
