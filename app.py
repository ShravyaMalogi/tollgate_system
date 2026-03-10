import streamlit as st
import cv2
import numpy as np
from plate_detection import number_plate_detection
from database import get_balance, deduct_toll

st.title("Automatic Toll Gate System")

st.write("Upload a vehicle image to detect number plate and deduct toll.")

uploaded_file = st.file_uploader("Upload Vehicle Image", type=["jpg","png","jpeg"])


if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    img = cv2.imdecode(file_bytes, 1)

    st.image(img, caption="Uploaded Image")

    if st.button("Detect Number Plate"):

        plate = number_plate_detection(img)

        if plate is None:

            st.error("Number plate not detected")

        else:

            st.success(f"Detected Plate: {plate}")

            balance = get_balance(plate)

            if balance is None:

                st.error("Vehicle not registered")

            else:

                st.write(f"Current Balance: ₹{balance}")

                if st.button("Pay Toll (₹20)"):

                    success = deduct_toll(plate)

                    if success:

                        st.success("Toll Paid Successfully")

                    else:

                        st.error("Insufficient Balance")
