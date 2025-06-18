import streamlit as st
import sys
import os

# Fix import issue: Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.calendar import get_available_days
from utils.stripe_connect import create_checkout_session

# Authentication check
if not st.session_state.get("authenticated"):
    st.error("Please login first.")
    st.stop()

st.title(f"{st.session_state['role']} Dashboard")

# Boat Owner View
if st.session_state["role"] == "Boat Owner":
    st.markdown("### Book a Service")
    services = ["Crane", "Trucking", "Launch"]
    selected = st.multiselect("Select Services", services)
    if selected:
        available = get_available_days(selected)
        st.write("Available Dates for All Selected Services:")
        st.json(available)

    amount = st.number_input("Estimated Total ($)", value=300)
    if st.button("Proceed to Payment"):
        session_url = create_checkout_session(int(amount * 100))
        st.markdown(f"[Click here to pay]({session_url})")

# Vendor View
elif st.session_state["role"] == "Vendor":
    st.markdown("### Vendor Tools")
    st.markdown("Connect Stripe to receive payouts:")
    st.markdown("[Connect with Stripe](https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_xxxxxx&scope=read_write)")

    # Link to vendor calendar manager
    st.page_link("pages/vendor_calendar.py", label="Manage Availability")

# Marina Admin View
elif st.session_state["role"] == "Marina Admin":
    st.markdown("### Admin Tools")
    st.markdown("You can manage vendors, set required fees, and monitor bookings.")
