from enum import Enum


class TripReason(Enum):
    travail = 540
    sante = 508
    famille = 474
    handicap = 441
    convocation = 418
    missions = 397
    transits = 363
    animaux = 330


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
