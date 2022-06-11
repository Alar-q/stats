import csv


def parseFloat(str):
    if len(str) == 0:
        return 0
    spl = str.split(",")
    if len(spl) > 1:
        return float(spl[0]) + (float(spl[1]) / (10**len(spl[1])))
    else:
        return float(str)


class Videocard:
    def __init__(self, name, hashrate, watt):
        self.name = name
        self.origHashrate = hashrate
        self.hashrate = hashrate
        self.watt = watt

    def scale(self, percentage):
        self.hashrate *= percentage
        self.watt *= percentage
        return self

    def __str__(self):
        return f"{self.name}\n" \
               f"       hashrate={round(self.origHashrate, 2)}\n" \
               f"       electricity={round(self.watt, 2)}\n"


class Person:
    def __init__(self, name):
        self.isCountingW = True
        self.name = name
        self.videocards = []

    def dontCountW(self):
        self.isCountingW = False

    def add(self, videocard):
        self.videocards.append(videocard)

    def getHashrate(self):
        res = 0
        for v in self.videocards:
            res += v.hashrate
        return res

    def getWatts(self):
        if not self.isCountingW:
            return 0
        res = 0
        for v in self.videocards:
            res += v.watt
        return res

    def __str__(self):
        res = f"{self.name}\n"
        for v in self.videocards:
            res += f"   {str(v)}\n"
        return res


class Rig:
    def __init__(self, name, prod_time):
        self.name = name
        self.prod_time = prod_time

""" 
    returns Persons array 
"""
def initPersons(file, rigs):

    persons = []

    with open(file) as f:
        for i, row in enumerate(csv.reader(f)):
            if i == 0:
                continue
            name = row[0]
            if name != "":
                persons.append(Person(name))

            v_name = row[1]
            if v_name != "":
                hashrate = parseFloat(row[2])
                electricity = parseFloat(row[3])
                belongs_prop = parseFloat(row[4])
                prod_time = -1

                rig_name = row[5]

                for rig in rigs:
                    if rig.name == rig_name:
                        prod_time = rig.prod_time

                if prod_time == -1:
                    print(f"69 line: prod_time = -1, {persons[len(persons) - 1].name}, {v_name}")

                # print(v_name, hashrate, electricity, row[2])

                videocard = Videocard(v_name, hashrate, electricity) \
                    .scale(belongs_prop) \
                    .scale(prod_time)

                persons[len(persons) - 1].add(videocard)

    return persons


class Stats:
    def __init__(self, persons, earnings, electricity):
        self.persons = persons
        self.earnings = earnings
        self.electricity = electricity

    def totalHashrate(self):
        res = 0
        for p in self.persons:
            res += p.getHashrate()
        return res

    def totalWatts(self):
        res = 0
        for p in self.persons:
            res += p.getWatts()
        return res

    def __str__(self):
        tH = self.totalHashrate()
        tW = self.totalWatts()

        personsStats = ""
        for p in self.persons:
            pH = p.getHashrate()
            pW = p.getWatts()
            revenue = (pH / tH) * self.earnings
            bill = (pW / tW) * self.electricity

            personsStats += f"\n---{p.name.upper()}---\n" \
                            f"  Hashrate: {round(pH, 2)}MH/S({round((pH / tH) * 100, 2)}%)\n" \
                            f"  Watts   : {int(pW)}({round((pW / tW) * 100, 2)}%)\n" \
                            f"  Revenue : {int(revenue)}\n" \
                            f"  El. bill: {int(bill)}\n" \
                            f"  Profit  : {int((p.getHashrate() / tH) * self.earnings - (p.getWatts() / tW) * self.electricity)} \n"

        return f"-- EARNINGS: {self.earnings} --\n" \
               f"-- ELECTRICITY BILL: {self.electricity} --\n" \
               f"-- AV HASHRATE: {round(tH, 2)} MH/S --\n" \
               f"-- AV ELECTRICITY CONSUMPTION: {int(tW)} Watt --\n" \
               f"{personsStats}"


if __name__ == "__main__":
    AA_rig = Rig("AA", 1)
    AU_rig = Rig("AU",  1)

    persons = initPersons("./assets/ИП Pawloona - hashrates.csv", [AA_rig, AU_rig])
    # for i in persons:
    #     if True and (i.name == "Amir" or i.name == "Alimzhan"):
    #         i.dontCountW()

    EARNINGS = 162224
    ELECTRICITY = 0

    stats = Stats(persons, EARNINGS, ELECTRICITY)
    print(stats)
    # for p in persons:
    #     print(p)

"""
-- AV HASHRATE: 776.78 MH/S --
-- AV ELECTRICITY CONSUMPTION: 2672 Watt --

---ULAN---
  Hashrate: 89.79MH/S(11.56%)
  Watts   : 279(10.46%)

---ALAR---
  Hashrate: 309.21MH/S(39.81%)
  Watts   : 1053(39.43%)

---ANSAR---
  Hashrate: 60.09MH/S(7.74%)
  Watts   : 184(6.91%)

---AMIR---
  Hashrate: 155.01MH/S(19.96%)
  Watts   : 571(21.37%)

---ALIMZHAN---
  Hashrate: 119.45MH/S(15.38%)
  Watts   : 458(17.14%)

---AUNT---
  Hashrate: 31.41MH/S(4.04%)
  Watts   : 75(2.81%)

---NURIK---
  Hashrate: 11.81MH/S(1.52%)
  Watts   : 50(1.87%)
"""
