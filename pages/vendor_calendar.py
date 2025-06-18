import streamlit as st
from utils.calendar import load_availability, save_availability

if not st.session_state.get("authenticated") or st.session_state["role"] != "Vendor":
    st.error("Access denied.")
    st.stop()

st.title("Vendor Calendar Management")
services = ["Crane", "Trucking", "Launch"]
service = st.selectbox("Select Service to Manage", services)

date = st.date_input("Select Date to Set Availability")
capacity = st.number_input("Set Capacity for This Day", min_value=0, step=1)

if st.button("Save Availability"):
    avail = load_availability()
    service_data = avail.get(service, {})
    service_data[date.strftime("%Y-%m-%d")] = capacity
    avail[service] = service_data
    save_availability(avail)
    st.success(f"Availability saved for {service} on {date.strftime('%Y-%m-%d')} with capacity {capacity}")

st.divider()
st.subheader("Current Availability Overview")
avail = load_availability()
if avail:
    st.json(avail)
else:
    st.info("No availability set yet.")
