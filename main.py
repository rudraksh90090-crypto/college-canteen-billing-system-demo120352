# College Canteen Billing System

print("=" * 45)
print("       WELCOME TO COLLEGE CANTEEN")
print("=" * 45)

# Food menu
menu = {
    1: ("Burger", 80),
    2: ("Pizza", 120),
    3: ("Sandwich", 70),
    4: ("Momos", 60),
    5: ("French Fries", 90),
    6: ("Cold Drink", 40),
    7: ("Coffee", 50),
    8: ("Combo Meal", 200)
}

cart = []
subtotal = 0

# Display menu
print("\nMENU")
print("-" * 45)

for number, (item, price) in menu.items():
    print(f"{number}. {item:<20} ₹{price}")

print("-" * 45)

# Taking orders
while True:
    try:
        choice = int(input("\nEnter item number (0 to finish): "))

        if choice == 0:
            break

        if choice not in menu:
            print("Invalid item number. Please try again.")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        item_name, price = menu[choice]
        item_total = price * quantity

        cart.append((item_name, quantity, item_total))
        subtotal += item_total

        print(f"{item_name} x {quantity} added to your order.")
        print(f"Item total: ₹{item_total}")

    except ValueError:
        print("Please enter a valid number.")

# Check whether an order was placed
if subtotal == 0:
    print("\nNo items were ordered.")
    print("Thank you for visiting the College Canteen!")
    exit()

# Ask whether customer is ordering during peak college hours
peak_hours = input(
    "\nAre you ordering during peak college hours? (yes/no): "
).strip().lower()

# Ask whether customer has ordered a combo
combo_order = input(
    "Did you order a combo? (yes/no): "
).strip().lower()

# Calculate discounts
discount_10 = 0
peak_discount = 0
voucher_discount = 0

# 10% discount if bill is greater than ₹500
if subtotal > 500:
    discount_10 = subtotal * 0.10

# Additional 3% discount during peak college hours
if peak_hours == "yes":
    peak_discount = subtotal * 0.03

# Combo voucher discount
if combo_order == "yes":
    voucher_discount = 50

total_discount = discount_10 + peak_discount + voucher_discount
final_amount = subtotal - total_discount

# Offers
cold_coffee = False
gift = False

# Cold coffee offer for ₹500–₹1500
if 500 <= subtotal <= 1500:
    cold_coffee = True

# Combo customer gets a gift
if combo_order == "yes":
    gift = True

# Make sure final amount doesn't become negative
if final_amount < 0:
    final_amount = 0

# Print final bill
print("\n")
print("=" * 45)
print("             FINAL BILL")
print("=" * 45)

for item_name, quantity, item_total in cart:
    print(f"{item_name:<20} x {quantity:<3} ₹{item_total}")

print("-" * 45)
print(f"Subtotal:                         ₹{subtotal:.2f}")

if discount_10 > 0:
    print(f"10% Discount:                    -₹{discount_10:.2f}")

if peak_discount > 0:
    print(f"Peak Hour Discount (3%):        -₹{peak_discount:.2f}")

if voucher_discount > 0:
    print(f"Combo Voucher Discount:          -₹{voucher_discount:.2f}")

print("-" * 45)
print(f"FINAL AMOUNT:                     ₹{final_amount:.2f}")
print("=" * 45)

# Display offers
print("\nSPECIAL OFFERS")

if cold_coffee:
    print("✓ Congratulations! You get a FREE Cold Coffee!")

if gift:
    print("✓ Combo Offer: You receive a FREE GIFT!")

if not cold_coffee and not gift:
    print("No complimentary offers on this order.")

print("\nThank you for visiting the College Canteen!")
print("Have a great day!")
