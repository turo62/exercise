#It's only about converting string to time format.
import datetime

def stat(strg):
    strg = strg.replace("|", ":")
    strg1 = strg.split(",")
    length = len(strg1)
    arr = datetime.datetime.strptime(strg1[0], '%H:%M:%S').time()
    arr1 = datetime.datetime.strptime(strg1[0], '%H:%M:%S').time()
    return strg1