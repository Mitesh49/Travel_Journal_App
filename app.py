import streamlit as st
import pandas as pd
import os

# Function to store user details in the login Excel sheet
def store_user_credentials(username, password):
    data = {
        "Username": [username],
        "Password": [password]
    }
    df = pd.DataFrame(data)
    
    try:
        # Check if the sheet already exists
        with pd.ExcelFile("login.xlsx") as xls:
            if 'User_Credentials' in xls.sheet_names:
                existing_df = pd.read_excel(xls, sheet_name='User_Credentials')
                # Concatenate the new data if the sheet has existing data
                df = pd.concat([existing_df, df], ignore_index=True)

    except FileNotFoundError:
        pass  # File doesn't exist yet, no need to concatenate

    # Write the data to the sheet
    with pd.ExcelWriter("login.xlsx", mode='w', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='User_Credentials')


# Function to check if the entered credentials match those in the login Excel sheet
# Function to authenticate user
def authenticate_user(username, password):
    try:
        df = pd.read_excel("login.xlsx", sheet_name='User_Credentials')
        user_credentials = df.set_index('Username').to_dict()['Password']
        if username in user_credentials and user_credentials[username] == password:
            return True
        else:
            return False
    except FileNotFoundError:
        return False



# Function to create a login page
def login_page():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.is_authenticated = True
            st.session_state.username = username  # Store username in session state
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

# Function to create a signup page
def signup_page():
    st.subheader("Signup if you are new")
    new_username = st.text_input("Enter a new username")
    new_password = st.text_input("Enter a new password", type='password')
    if st.button("Signup"):
        store_user_credentials(new_username, new_password)
        st.success("Signup successful! Please login.")

def store_user_details(username, travel_date, destination, activities, memorable_moments, photos):
    data = {
        "Username": username,
        "Travel Date": travel_date,
        "Destination": destination,
        "Activities": activities,
        "Memorable Moments": memorable_moments,
        "Photos": str(photos)  # Convert to string for easier handling
    }
    df = pd.DataFrame(data, index=[0])
    try:
        existing_df = pd.read_excel("data.xlsx")
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass  # File doesn't exist yet, no need to concatenate
    df.to_excel("data.xlsx", index=False)
# Function to display previous trips
def view_previous_trips():
    try:
        df = pd.read_excel("data.xlsx")
        # Remove unnamed columns
        df = df.loc[:, [col for col in df.columns if not col.startswith('Unnamed')]]
        st.subheader("Previous Trips")
        st.write(df)
    except FileNotFoundError:
        st.error("No previous trips found.")



# Main page functionality
def main_page():
    st.title("Travel Journal App")
    st.subheader("Welcome to the Travel Journal App")

    st.subheader("Record Your Trip")
    username = st.session_state.username
    travel_date = st.date_input("Travel Date")
    destination = st.text_input("Destination")
    activities = st.text_area("Activities")
    memorable_moments = st.text_area("Memorable Moments")
    photos = st.file_uploader("Upload Photos", accept_multiple_files=True)

    if st.button("Save Details"):
        store_user_details(username, travel_date, destination, activities, memorable_moments, photos)
        st.success("Details saved successfully!")
        
    if st.button("View Previous Trips"):
        try:
            df = pd.read_excel("data.xlsx")
            st.write(df)
        except FileNotFoundError:
            st.error("No previous trips found.")

# Check if the user is logged in
if 'is_authenticated' not in st.session_state:
    st.session_state.is_authenticated = False

# Render login page if the user is not logged in
if not st.session_state.is_authenticated:
    login_page()
    signup_page()  # Render signup page below login

# If user is logged in, display the main page
if st.session_state.is_authenticated:
    main_page()
