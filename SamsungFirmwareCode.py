import sys

firmware_code = sys.argv[1]
year = {"A": 2001, " B": 2002, " C": 2003, " D": 2004, " E": 2005, "F": 2006, "G": 2007, "H": 2008, "I": 2009,
        "J": 2010, "K": 2011, "L": 2012, "M": 2013, "N": 2014, "O": 2015, "P": 2016, "Q": 2017, "R": 2018, "S": 2019,
        "T": 2020, "U": 2021, "V": 2022, "W": 2023, "X": 2024, "Y": 2025, "Z": 2026}
month = {"A": "January",
         "B": "February",
         "C": "March",
         "D": "April",
         "E": "May",
         "F": "June",
         "G": "July",
         "H": "August",
         "I": "September",
         "J": "October",
         "K": "November",
         "L": "December"}

while not len(firmware_code) == 13:
    print("Firmware code must be 13 digits")
    firmware_code = input("Enter firmware code: ")

sample_code = "G935VVRU4API3"
print("Model: {0}".format(firmware_code[:5]))
print("Region: {0}".format(firmware_code[5:8]))
print("Bootloader Revision: {0}".format(firmware_code[8]))
print("Year: {0}".format(year[firmware_code[10]]))
print("Month: {0}".format(month[firmware_code[11]]))
print("Firmware Revision: {0}".format(firmware_code[12]))
