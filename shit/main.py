from datetime import datetime
from logic import Rig, Videocard, Person, Stats

EARNINGS = 100
ELECTRICITY_BILL = 100

stats = Stats(EARNINGS, ELECTRICITY_BILL)

startTime = datetime(year=2022, month=3, day=20, hour=13, minute=0)
endTime = datetime(year=2022, month=3, day=21, hour=15, minute=55)

# <-- Rigs -->
AA_dual = Rig("./assets/stats/AA_dual/", startTime, endTime)
AA_green = Rig("./assets/stats/AA_green/", startTime, endTime)
AU_green = Rig("./assets/stats/AU_green/", startTime, endTime)
AU_red = Rig("./assets/stats/AU_red/", startTime, endTime)

# <-- VideoCards -->
# <-- AA_dual -->
c3060tix4_amir_alim1 = Videocard(AA_dual, (40.41 + 41.57 + 41.60 + + 41.51) / 4, (131 + 173 + 168 + 157) / 4)
c6600_amir5 = Videocard(AA_dual, 28.63, 67)

# <-- AA_green -->
c1060_alim6 = Videocard(AA_green, 21.22, 82)
c1070ti_alim7 = Videocard(AA_green, 28.37, 111)
c580_alim8 = Videocard(AA_green, 27.23, 109)

# <-- AU_red -->
c6600x3_alar_ulan9 = Videocard(AU_red, 29, 50)
c580_alar12 = Videocard(AU_red, 30.65, 117)
c480_alar13 = Videocard(AU_red, 28.05, 92)

# <-- AU_green -->
с1060x2_alar_ulan_nurik14 = Videocard(AU_green, (23.94+23.67)/2, 99)
c1660ti_alar16 = Videocard(AU_green, 30.91, 75)
c2060_ulan_ansar17 = Videocard(AU_green, 32.81, 82)
c1070asus1_alar18 = Videocard(AU_green, 24.25, 114)
c1660_alar_ulan19 = Videocard(AU_green, 25.25, 71)
c1070gig_alar20 = Videocard(AU_green, 25.42, 129)
c1660s_ulan_ansar21 = Videocard(AU_green, 29.42, 70)
c2060s_alar22 = Videocard(AU_green, 43.75, 89)
c1070asus2_alar23 = Videocard(AU_green, 25.46, 136)
c1660ti_aunt24 = Videocard(AU_green, 31.55, 76)

# <-- Persons -->
Alar = Person("Alar")
Ulan = Person("Ulan")
Amir = Person("Amir")
Alimzhan = Person("Alimzhan")
Nurik = Person("Nurik")
Aunt = Person("Aunt")
Ansar = Person("Ansar")


def initAlar():
    Alar.add(c6600x3_alar_ulan9, 183)
    Alar.add(c580_alar12, 100)
    Alar.add(c480_alar13, 100)
    Alar.add(с1060x2_alar_ulan_nurik14, 100)
    Alar.add(c1660ti_alar16, 100)
    Alar.add(c1070asus1_alar18, 100)
    Alar.add(c1660_alar_ulan19, 50)
    Alar.add(c1070gig_alar20, 100)
    Alar.add(c2060s_alar22, 100)
    Alar.add(c1070asus2_alar23, 100)

    stats.add(Alar)


def initUlan():
    Ulan.add(c6600x3_alar_ulan9, 117)
    Ulan.add(c1660_alar_ulan19, 50)
    Ulan.add(c2060_ulan_ansar17, 50)
    Ulan.add(c1660s_ulan_ansar21, 25)
    Ulan.add(с1060x2_alar_ulan_nurik14, 50)

    stats.add(Ulan)


def initAmir():
    Amir.add(c3060tix4_amir_alim1, 300)
    Amir.add(c6600_amir5, 100)

    stats.add(Amir)


def initAlimzhan():
    Alimzhan.add(c3060tix4_amir_alim1, 100)
    Alimzhan.add(c1060_alim6, 100)
    Alimzhan.add(c1070ti_alim7, 100)
    Alimzhan.add(c580_alim8, 100)

    stats.add(Alimzhan)


def initNurik():
    Nurik.add(с1060x2_alar_ulan_nurik14, 50)

    stats.add(Nurik)


def initAunt():
    Aunt.add(c1660ti_aunt24, 100)
    stats.add(Aunt)


def initAnsar():
    Ansar.add(c2060_ulan_ansar17, 50)
    Ansar.add(c1660s_ulan_ansar21, 75)

    stats.add(Ansar)


if __name__ == '__main__':
    print("-- AA_dual", str(int(AA_dual.productive_time * 100)) + "%", "--")
    print("-- AA_green", str(int(AA_green.productive_time * 100))  + "%", "--")
    print("-- AU_green", str(int(AU_green.productive_time * 100)) + "%", "--")
    print("-- AU_red", str(int(AU_red.productive_time * 100)) + "%", "--")
    print()

    initAlar()
    initUlan()
    initAmir()
    initAlimzhan()
    initNurik()
    initAunt()
    initAnsar()

    print(stats)
