import streamlit as st

st.title("🍔 Two Sisters Fast Food Ordering App")
st.write("Welcome! Select your items and place your order.")

# Initialize session state for cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# --- Function to add items to cart ---
def add_to_cart(item, price, quantity):
    if quantity > 0:
        st.session_state.cart.append({
            "item": item,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        })
        st.success(f"Added {quantity} x {item} to cart!")

# --- Kotas Section ---
st.header("🥪 Kotas")

kota_type = st.selectbox("Select Kota type:", ["R20 Kota", "R30 Kota"])
kota_qty = st.number_input("Quantity", min_value=0, step=1)

# Extra options for R30
extra_ingredients = []
if kota_type == "R30 Kota":
    extra_ingredients = st.multiselect(
        "Add extra ingredients (optional):",
        ["Extra Cheese", "Extra Russian", "Extra Eggs"]
    )

kota_price = 20 if kota_type == "R20 Kota" else 30

if st.button("Add Kota to Cart"):
    item_name = kota_type
    if extra_ingredients:
        item_name += " with " + ", ".join(extra_ingredients)
    add_to_cart(item_name, kota_price, kota_qty)

# --- Chips Section ---
st.header("🍟 Chips")

chip_size = st.selectbox("Select Chips size:", ["Small - R15", "Medium - R25"])
chip_qty = st.number_input("Quantity of Chips", min_value=0, step=1)

chips_price = 15 if chip_size == "Small - R15" else 25

if st.button("Add Chips to Cart"):
    add_to_cart(chip_size, chips_price, chip_qty)

# --- Cart Summary ---
st.header("🛒 Your Cart")

if st.session_state.cart:
    total_price = 0
    for idx, item in enumerate(st.session_state.cart, 1):
        st.write(f"{idx}. {item['quantity']} x {item['item']} = R{item['total']}")
        total_price += item['total']
    st.subheader(f"💰 Total: R{total_price}")

    if st.button("Place Order"):
        st.success(f"✅ Your order has been placed! Total: R{total_price}")
        st.session_state.cart = []  # Clear cart after order
else:
    st.write("Your cart is empty. Add some items!")