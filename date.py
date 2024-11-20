from datetime import datetime


def main():
    # Pobranie aktualnej daty i godziny
    now = datetime.now()

    # Wyświetlenie aktualnej daty i godziny
    print("Aktualna data i godzina:", now.strftime("%Y-%m-%d %H:%M:%S"))

    # Obliczenie UNIX timestamp
    unix_timestamp = int(now.timestamp())

    # Wyświetlenie UNIX timestamp
    print("UNIX timestamp:", unix_timestamp)


if __name__ == "__main__":
    main()