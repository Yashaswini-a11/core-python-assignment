def add_item(menu, item):
    if item not in menu:
        menu.append(item)
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
        return True
    return False
def check_item(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

def main():
    initial_menu = input().strip()
    menu = [item.strip() for item in initial_menu.split(",") if item.strip()]
    add_item_name = input("item to add").strip()
    remove_item_name = input("item to remove").strip()
    check_item_name = input("item to check").strip()
    add_item(menu, add_item_name)
    removed = remove_item(menu, remove_item_name)
    print(f"\nUpdated menu: {menu}")
    print(f"Availability: {check_item(menu, check_item_name)}")
if __name__ == "__main__":
    main()
