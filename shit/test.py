from datetime import datetime

from stats import WorkingInfo

if __name__ == '__main__':
    info = WorkingInfo("./assets/test_stats/")

    print(info.productive_time(
        datetime(year=2022, month=3, day=18, hour=15, minute=25),
        datetime(year=2022, month=3, day=19, hour=17, minute=20))
    )

    print(info.data_dict)
    print(info.info)