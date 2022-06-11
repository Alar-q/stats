from datetime import datetime

from stats import WorkingInfo, productive_time


class Rig:
    def __init__(self, dirname, s, e):
        self.productive_time = productive_time(dirname, s, e)


class Videocard:
    # Привязан к Rig и общая мощность, электричество умножается на продуктивное время
    def __init__(self, rig, hashrate, watt, name=""):
        self.name = name
        self.hashrate = hashrate * rig.productive_time
        self.watt = watt * rig.productive_time


class Person:
    # Хранит массив карт
    def __init__(self, name):
        self.name = name
        self.videocards = []
        self.percentage = []

    def add(self, videocard, percentage):
        self.videocards.append(videocard)
        self.percentage.append(percentage/100)
        return self

    def getHashrate(self):
        sum = 0
        for i in range(len(self.videocards)):
            # print(self.videocards[i].hashrate, self.percentage[i])
            sum += self.videocards[i].hashrate * (self.percentage[i] / 100)
        return sum

    def getWatts(self):
        sum = 0
        for i in range(len(self.videocards)):
            sum += self.videocards[i].watt * (self.percentage[i] / 100)
        return sum

    def __str__(self):
        return f"---{self.name.upper()}---\n" \
               f"HashRate: {int(self.getHashrate())} hash\n" \
               f"Watts: {int(self.getWatts())} watt\n"


class Stats:
    def __init__(self, earnings, electricity):
        self.persons = {} # {'name': person}
        self.earnings = earnings
        self.electricity = electricity

    def add(self, person):
        self.persons[person.name] = person

    def totalHashrate(self):
        res = 0
        for name, person in self.persons.items():
            res += person.getHashrate()
        return res

    def totalWatts(self):
        res = 0
        for name, person in self.persons.items():
            res += person.getWatts()
        return res

    def statsOf(self, name):
        p = self.persons[name]
        rev = int(self.earnings * (p.getHashrate() / self.totalHashrate()))
        elBill = int(self.electricity * (p.getWatts() / self.totalWatts()))
        return f"{str(p)}" \
               f"Revenue: {rev}\n" \
               f"Electr. bill: {elBill}\n" \
               f"Profit: {rev - elBill}\n"

    def __str__(self):
        personsStats = ""
        for name, person in self.persons.items():
            personsStats += "\n" + self.statsOf(name)

        return f"-- EARNINGS: {self.earnings} --\n" \
               f"-- ELECTRICITY BILL: {self.electricity} --\n" \
               f"-- AV HASHRATE: {int(self.totalHashrate())} --\n" \
               f"-- AV ELECTRICITY CONSUMPTION: {int(self.totalWatts())} --\n" \
               f"{personsStats}"


if __name__ == "__main__":
    start = datetime(year=2022, month=3, day=20, hour=13, minute=0)
    end = datetime(year=2022, month=3, day=21, hour=15, minute=55)

    AA_dual = Rig("./assets/stats/AA_dual/", start, end)
    AA_green = Rig("./assets/stats/AA_green/", start, end)
    AU_green = Rig("./assets/stats/AU_green/", start, end)
    AU_red = Rig("./assets/stats/AU_red/", start, end)

    c1060 = Videocard(AU_green, "1060", 20, 40)
    c1080 = Videocard(AU_green, "1060", 30, 80)

    Alar = Person("Alar")
    Alar.add(c1060, 100)
    Alar.add(c1080, 100)

    stats = Stats(100, 100)
    stats.add(Alar)

    # print(stats.statsOf("Alar", 100, 100))
    print(stats)
