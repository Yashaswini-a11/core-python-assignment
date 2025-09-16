def calculate_fare(distance):
    return 50 + (10 * distance)
def main():
    trips_input = input("Enter trip distances in km ")
    trips = [int(t.strip()) for t in trips_input.split(',') if t.strip().isdigit()]
    if not trips:
        print("No valid distances entered.")
        return
    total = 0
    for i, d in enumerate(trips, 1):
        fare = calculate_fare(d)
        print(f"Trip {i}: ${fare}")
        total += fare
    print(f"Total Fare: ${total}")
if __name__ == "__main__":
    main()
