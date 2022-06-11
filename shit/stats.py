import csv
from datetime import datetime, timedelta
import os


def str2datetime(val):
    try:
        res = datetime.strptime(str(val), '%d/%m/%Y %H:%M:%S')
    except:
        res = datetime.strptime(str(val), '%Y-%m-%d %H:%M:%S')
    return res


class WorkingInfo:
    def __init__(self, dirname):

        #data_dict нужен для легкого поиска была ли уже эта дата.
        self.data_dict = {} # {'datetime': isWorking}

        for file in map(lambda name: os.path.join(dirname, name), os.listdir(dirname)):
            if os.path.isfile(file):
                self.__read(file)

        self.__remember(dirname)

        # Нужен чтобы брать данные от точки до точки
        self.info = self.getFullList() # [(datetime, isWorking)]

    def __read(self, file, resultFile=False):
        with open(file) as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                # Пропуск первой строчки
                if not resultFile and i == 0:
                    continue

                date = self.__findTime(row)
                if date == "none":
                    print("date = none", file)
                    continue # Почему-то я здесь до этого написал return

                b = self.__isWorking(row, resultFile)
                if str(date) in self.data_dict:
                    b = b or self.data_dict[str(date)]
                self.data_dict[str(date)] = b

    def __remember(self, dirname):
        fileDir = dirname + '/result/result.csv'

        # read from result.csv if it exists
        dir = os.path.dirname(fileDir)
        if not os.path.exists(dir):
            os.makedirs(dir)
        else:
            self.__read(fileDir, resultFile=True)

        # write down information to result.csv
        with open(fileDir, 'w', newline='') as f:
            writer = csv.writer(f)
            lst = []
            for key in sorted(self.data_dict):
                lst.append((key, self.data_dict[key]))
            writer.writerows(lst)

    def getFullList(self):
        lst = []
        last_key = "first"
        for key in sorted(self.data_dict):
            if last_key == "first":
                last_key = key
                lst.append((key, self.data_dict[key]))
            else:
                dt = str2datetime(key) - str2datetime(last_key)
                dt = int(dt.total_seconds() / 60 / 5)  # 60/5

                for i in range(1, dt):
                    k = str(str2datetime(last_key) + timedelta(minutes=i*5))
                    lst.append((k, True))

                lst.append((key, self.data_dict[key]))

                last_key = key

        return lst

    def __findTime(self, row_listData):
        res = "none"
        if(len(row_listData) > 0):
            res = str2datetime(str(row_listData[0]))
        return res

    @staticmethod
    def __isWorking(row, resultFile):
        if resultFile:
            return True if row[1] == "True" else False
        else:
            for i in range(1, len(row)):
                try:
                    val = int(row[i])
                except:
                    val = 0

                if val != 0:
                    return True

            return False

    def __index(self, datetime):
        for i in range(len(self.info)):
            if str2datetime(self.info[i][0]) == datetime:
                return i

    def productive_time(self, start, end):
        res = 0
        steps = int(((end - start).total_seconds()) / (60*5)) + 1
        id = self.__index(start)

        for i in range(steps):
            if self.info[id+i][1]:
                res += 1
        return res / steps

    def __len__(self):
        return len(self.data_dict)


def productive_time(dirname, startTime, endTime):
    info = WorkingInfo(dirname)
    return info.productive_time(startTime, endTime)


if __name__ == '__main__':
    print(productive_time("./assets/stats/AA_dual/",
        datetime(year=2022, month=3, day=18, hour=13, minute=0),
        datetime(year=2022, month=3, day=20, hour=3, minute=55))
    )