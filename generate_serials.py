def birthdaySerialNumbers():
    # Opening (or creating) a text file for writing
    with open("special_serials.txt", "a") as file:
        for year in range(1776, 2125):
            for month in range(1, 13):
                for day in range(1, 32):
                    month_str = "0" + str(month) if len(str(month)) == 1 else str(month)
                    day_str = "0" + str(day) if len(str(day)) == 1 else str(day)

                    us_format = month_str + day_str + str(year)
                    euro_format = day_str + month_str + str(year)
                    intl_format = str(year) + month_str + day_str

                    file.write(us_format + "\r")
                    file.write(euro_format + "\r")
                    file.write(intl_format + "\r")


def lowSerialNumbers():
    with open("special_serials.txt", "a") as file:
        for i in range(10000):
            temp = "000" + str(i)
            while len(temp) < 8:
                temp = "0" + temp
            if i < 1001:
                file.write(temp[::-1] + "\r")
            file.write(temp + "\r")


if __name__ == "__main__":
    birthdaySerialNumbers()
    lowSerialNumbers()
