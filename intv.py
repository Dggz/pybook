from copy import copy


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @property
    def year(self):
        print(f"property")
        return self._year

    @year.setter
    def year(self, value):
        print(f"setter {value}")
        self._year = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value


current_day = Date(2022, 2, 16)
print('initd')
past_days = 50
past_dates = []

for _ in range(past_days, 0, -1):
    past_dates.append(copy(current_day))

    current_day.day -= 1
    if current_day.day == 0:
        current_day.day = 30
        current_day.month -= 1

    if current_day.month == 0:
        current_day.month = 12
        current_day.year -= 1

for date in past_dates:
    print(f"Date: {date.year, date.month, date.day}; "
          f"Days since beginning of year: {(date.month - 1) * 30 + date.day}")
