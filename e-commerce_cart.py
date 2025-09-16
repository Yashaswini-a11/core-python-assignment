def calculate_total_price(cart):
    total = sum(cart.values())
    return total * 0.9 if len(cart) > 5 else total

def main():
    cart = {}
    print("Enter items.Type done to finish.")
    while True:
        item = input("Item name: ").strip()
        if item.lower() == 'done':
            break
        price = input(f"Price of '{item}': ").strip()
        if not price.replace('.', '', 1).isdigit():
            print("Invalid price, try again.")
            continue
        price = float(price)
        if price < 0:
            print("Price cannot be negative.")
            continue
        cart[item] = price
    print(f"Total Price: {calculate_total_price(cart):.2f}")
if __name__ == "__main__":
    main()
