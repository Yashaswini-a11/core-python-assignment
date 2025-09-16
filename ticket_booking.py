def book_seat(booked_seats, seat_number, total_seats):
    if seat_number < 1 or seat_number > total_seats:
        print(f"Seat {seat_number} is out of range.")
        return
    if seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    else:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} booked successfully.")

def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} cancelled successfully.")
    else:
        print(f"Seat {seat_number} is not currently booked.")

def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def main():
    total_seats = 10
    booked_seats = [2, 5, 7]
    print(f"Initial booked seats: {booked_seats}")
    book = input("Enter seat number to book: ").strip()
    cancel = input("Enter seat number to cancel: ").strip()
    if book.isdigit():
        book_seat(booked_seats, int(book), total_seats)
    else:
        print("Invalid input for booking.")
    if cancel.isdigit():
        cancel_seat(booked_seats, int(cancel))
    else:
        print("Invalid input for cancellation.")
    available = get_available_seats(total_seats, booked_seats)
    print(f"\nAvailable seats: {available}")
if __name__ == "__main__":
    main()
