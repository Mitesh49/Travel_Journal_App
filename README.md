# Travel_Journal_App
a basic Front-end dashboard where users can login and document about their trip and upload photos of it.
Travel Journal App

This Streamlit app allows users to record and view their travel experiences. Users can log in, sign up if they are new users, record details of their trips including travel date, destination, activities, memorable moments, and upload photos. The app also enables users to view their previous trips.

File Structure:
- app.py: The main Python script containing the Streamlit app code.
- login.xlsx: Excel file used to store user credentials (username and password).
- data.xlsx: Excel file used to store details of the recorded trips.

Functionality:
1. Authentication and Signup:
   - Users can log in using their existing username and password.
   - New users can sign up by providing a username and password. The credentials are stored securely in the login.xlsx file.

2. Recording Trip Details:
   - Once logged in, users can record details of their trips, including the travel date, destination, activities, memorable moments, and upload photos.
   - The details are stored in the data.xlsx file.

3. Viewing Previous Trips:
   - Users can view their previous trips recorded in the data.xlsx file.
   - The app displays the trip details in a tabular format.

Instructions:
1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the app using `streamlit run app.py`.
4. Log in with your existing credentials or sign up if you are a new user.
5. Record details of your trips and view your previous trips.

Dependencies:
- Streamlit: For building the interactive web app.
- Pandas: For data manipulation and handling Excel files.
- os: For file operations like checking file existence.

Note: Ensure that you have the required permissions to read and write to the login.xlsx and data.xlsx files.
