def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date_input = input("Enter Date: ").strip()

        if "/" in date_input:
            try:
                month, day, year = date_input.split("/")
                if int(month) <= 12 and int(day) <= 31:
                    print(f"{int(year):04}-{int(month):02}-{int(day):02}")
                    break
            except ValueError:
                pass

        elif "," in date_input:
            try:
                parts = date_input.replace(",", "").split(" ")
                if len(parts) == 3:
                    month_name, day, year = parts
                    if month_name in months:
                        month_num = months.index(month_name) + 1
                        if int(day) <= 31:
                            print(f"{int(year):04}-{month_num:02}-{int(day):02}")
                            break
            except ValueError:
                pass


if __name__ == "__main__":
    main()
