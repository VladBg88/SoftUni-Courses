import math

SF_COFFEE = 0.50
SF_WATER = 0.80
SF_BEER = 1.20
SF_SWEETS = 1.45
SF_PEANUTS = 1.60

PD_COFFEE = 0.40
PD_WATER = 0.70
PD_BEER = 1.15
PD_SWEETS = 1.30
PD_PEANUTS = 1.50

VN_COFFEE = 0.45
VN_WATER = 0.70
VN_BEER = 1.10
VN_SWEETS = 1.35
VN_PEANUTS = 1.55

product = input()
city = input()
pcs = float(input())

if city == "Sofia":
    if product == "coffee":
        print(round(SF_COFFEE * pcs, 2))
    if product == "water":
        print(round(SF_WATER * pcs, 2))
    if product == "beer":
        print(round(SF_BEER * pcs, 2))
    if product == "sweets":
        print(round(SF_SWEETS * pcs, 4))
    if product == "peanuts":
        print(round(SF_PEANUTS * pcs, 2))

if city == "Plovdiv":
    if product == "coffee":
        print(round(PD_COFFEE * pcs, 2))
    if product == "water":
        print(round(PD_WATER * pcs, 2))
    if product == "beer":
        print(round(PD_BEER * pcs, 2))
    if product == "sweets":
        print(round(PD_SWEETS * pcs, 4))
    if product == "peanuts":
        print(round(PD_PEANUTS * pcs, 2))

if city == "Varna":
    if product == "coffee":
        print(round(VN_COFFEE * pcs, 2))
    if product == "water":
        print(round(VN_WATER * pcs, 2))
    if product == "beer":
        print(round(VN_BEER * pcs, 2))
    if product == "sweets":
        print(round(VN_SWEETS * pcs, 4))
    if product == "peanuts":
        print(round(VN_PEANUTS * pcs, 2))


