from datetime import datetime

from quarantinecertificate import QuarantineCertificate
from curfewcertificate import CurfewCertificate

from data import CurfewTripReason, QuarantineTripReason, Trip, Profile

profile = Profile(
    firstname="Jean",
    lastname="Bob",
    birthday="11/10/1974",
    placeofbirth="Paris",
    address="10 Rue de la tour",
    zipcode="75001",
    city="Paris"
)

ctrip = Trip(date=datetime.now(),
             reasons=[
                 CurfewTripReason.travail,
                 CurfewTripReason.sante,
                 CurfewTripReason.famille,
                 CurfewTripReason.handicap,
                 CurfewTripReason.judiciaire,
                 CurfewTripReason.missions,
                 CurfewTripReason.transit,
                 CurfewTripReason.animaux,
             ])

ltrip = Trip(date=datetime.now(),
             reasons=[
                 QuarantineTripReason.sport,
                 QuarantineTripReason.achats,
                 QuarantineTripReason.enfants,
                 QuarantineTripReason.culte_culturel,
                 QuarantineTripReason.demarche,
                 QuarantineTripReason.travail,
                 QuarantineTripReason.sante,
                 QuarantineTripReason.famille,
                 QuarantineTripReason.handicap,
                 QuarantineTripReason.judiciaire,
                 QuarantineTripReason.demenagement,
                 QuarantineTripReason.transit,
             ])


def main():
    lc = QuarantineCertificate(profile, ltrip)
    lc.save(directory="tests")

    # cc = CurfewCertificate(profile, ctrip)
    # cc.save(directory="tests")


if __name__ == "__main__":
    main()
