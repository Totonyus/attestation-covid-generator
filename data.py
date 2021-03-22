from enum import Enum


class CurfewTripReason(Enum):
    travail = {'page': 1, 'y': 579}
    sante = {'page': 1, 'y': 546}
    famille = {'page': 1, 'y': 512}
    handicap = {'page': 1, 'y': 478}
    judiciaire = {'page': 1, 'y': 458}
    missions = {'page': 1, 'y': 412}
    transit = {'page': 1, 'y': 379}
    animaux = {'page': 1, 'y': 345}


class QuarantineTripReason(Enum):
    sport = {'page': 1, 'y': 367}
    achats = {'page': 1, 'y': 244}
    enfants = {'page': 1, 'y': 161}
    culte_culturel = {'page': 2, 'y': 781}
    demarche = {'page': 2, 'y': 726}
    travail = {'page': 2, 'y': 629}
    sante = {'page': 2, 'y': 533}
    famille = {'page': 2, 'y': 477}
    handicap = {'page': 2, 'y': 422}
    judiciaire = {'page': 2, 'y': 380}
    demenagement = {'page': 2, 'y': 311}
    transit = {'page': 2, 'y': 243}


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
