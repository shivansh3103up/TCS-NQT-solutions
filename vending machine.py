menu = {
    'C': {
        '1': 'Espresso Coffee',
        '2': 'Cappuccino Coffee',
        '3': 'Latte Coffee',
    },
    'T': {
        '1': 'Plain Tea',
        '2': 'Assam Tea',
        '3': 'Ginger Tea',
        '4': 'Cardamom Tea',
        '5': 'Masala Tea',
        '6': 'Lemon Tea',
        '7': 'Green Tea',
        '8': 'Organic Darjeeling Tea',
    },
    'S': {
        '1': 'Hot and Sour Soup',
        '2': 'Veg Corn Soup',
        '3': 'Tomato Soup',
        '4': 'Spicy Tomato Soup',
    },
    'B': {
        '1': 'Hot Chocolate Drink',
        '2': 'Badam Drink',
        '3': 'Badam-Pista Drink',
    },
}
main_menu = input("Enter the first letter to select the main menu (C/T/S/B): ").upper()
sub_menu = input("Enter the code to select the sub-menu: ")
if sub_menu in menu[main_menu]:
        selected_item = menu[main_menu][sub_menu]
        print("Welcome to CCD!")
        print("Enjoy your", selected_item)
else:
        print("Invalid sub-menu selection.")
