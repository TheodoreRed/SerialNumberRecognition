def birthdaySerialNumbers():
    # Open the file in append mode
    with open("special_serials.txt", "a") as file:
        # Iterate through years, months, and days
        for year in range(1776, 2125):
            for month in range(1, 13):
                for day in range(1, 32):
                    # Format month and day to have leading zeros
                    month_str = "0" + str(month) if len(str(month)) == 1 else str(month)
                    day_str = "0" + str(day) if len(str(day)) == 1 else str(day)

                    # Construct different date formats
                    us_format = month_str + day_str + str(year)
                    euro_format = day_str + month_str + str(year)
                    intl_format = str(year) + month_str + day_str

                    # Save the formats to the file
                    file.write(us_format + "\r")
                    file.write(euro_format + "\r")
                    file.write(intl_format + "\r")


def lowSerialNumbers():
    # Open the file in append mode
    with open("special_serials.txt", "a") as file:
        # Iterate through the first 10,000 numbers
        for i in range(10000):
            temp = "000" + str(i)
            # Format number to have leading zeros
            while len(temp) < 8:
                temp = "0" + temp
            # Save numbers and some reversed versions
            if i < 1001:
                file.write(temp[::-1] + "\r")
            file.write(temp + "\r")


# Execute both functions when the script is run
if __name__ == "__main__":
    birthdaySerialNumbers()
    lowSerialNumbers()
