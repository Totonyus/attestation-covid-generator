from datetime import datetime

from lockdowncertificate import LockdownCertificate
from curfewcertificate import CurfewCertificate

from data import CurfewTripReason, LockdownTripReason, Trip, Profile

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
                CurfewTripReason.courses,
                CurfewTripReason.sport,
                CurfewTripReason.rassemblement,
                CurfewTripReason.demarche
            ])

ltrip = Trip(date=datetime.now(),
             reasons=[
                 LockdownTripReason.travail,
                 LockdownTripReason.sante,
                 LockdownTripReason.famille,
                 LockdownTripReason.handicap,
                 LockdownTripReason.judiciaire,
                 LockdownTripReason.missions,
                 LockdownTripReason.transit,
                 LockdownTripReason.animaux,
                 LockdownTripReason.courses,
                 LockdownTripReason.sport,
                 LockdownTripReason.rassemblement,
                 LockdownTripReason.demarche
             ])

def main():
    lc = LockdownCertificate(profile, ltrip)
    lc.save(directory="tests")

    cc = CurfewCertificate(profile, ctrip)
    cc.save(directory="tests")


if __name__ == "__main__":
    main()
