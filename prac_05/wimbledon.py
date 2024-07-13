"""
Wimbledon Prac 05
Estimate: 45 mins
Actual 1hour 10 mins
"""

FILENAME = "wimbledon.csv"
INDEX_ORIGIN = 1
INDEX_TENNIS_PLAYER = 2


def main():
    """Reads CSV file and prints the tennis player aswell as countries of origin"""
    records = get_records(FILENAME)
    tennis_player, country_of_origin = process_data_records(records)
    print_results(tennis_player, country_of_origin)


def get_records(filename):
    """Reads CSV file and returns a list of list"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:  # I cant tell if i used this right
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return (records)


def process_data_records(records):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    champion_to_wins = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_ORIGIN])
        try:
            champion_to_wins[record[INDEX_TENNIS_PLAYER]] += 1
        except KeyError:
            champion_to_wins[record[INDEX_TENNIS_PLAYER]] = 1
    return champion_to_wins, countries


def print_results(champion_to_win, countries):
    """Print players and country of origin"""
    print("champions: ")
    for name, count in champion_to_win.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
