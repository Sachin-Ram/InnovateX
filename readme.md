# WanderHub  

**WanderHub** is a comprehensive travel planning application built using Python Flask. It aims to provide users with a seamless experience in planning trips by fetching the best flight deals, suggesting preferred hotel stays, managing expenses, and offering weather checks for destinations.  

## Features  

### 1. **Plan a Trip**  
- Skip the hassle of searching for flights and hotels! Simply provide your travel details, and WanderHub will fetch the best deals for you. Choose your preferred plan, get the total cost, and enjoy stress-free planning!

### 2. **User-Preferred Stay**  
- Find the perfect place to stay! Enter your preferences, and WanderHub will recommend hotels based on your ratings, location, and budget. Easy booking at your fingertips! 

### 3. **Expense Management**  
- Manage your trip expenses effortlessly by categorizing them into food, stay, entertainment, and more. Keep track of your budget as you go! 

### 4. **Weather Updates**  
- Make sure you're prepared for any weather! Get real-time weather forecasts for your destination, helping you pack and plan accordingly.  


## Project Structure  

### `controllers`  
- Handles all the routes separately and acts as a controller for every service.  
- Responsible for managing HTTP endpoints and routing user requests to the appropriate logic in the `services` layer.  

### `services`  
- Contains files responsible for making API calls and performing the business logic required to fetch and process data.  
- Acts as the layer where core operations and external integrations are implemented.  

### `app.py`  
- The main entry point of the application.  
- Registers all the routes defined in the `controllers` folder and initializes the Flask app.  

Follow the steps below to set up **WanderHub** on your local machine.

### Prerequisites  

Before you start, make sure you have the following installed:  

- **Python** (version 3.8 or higher)  
- **pip** (Python's package installer)  

If you don’t have **Python** and **pip** installed, here’s how you can do it:

1. **Install Python**  
   Go to [Python's official website](https://www.python.org/downloads/) and download the latest version for your operating system. Follow the installation instructions.

2. **Verify Python and pip installation**  
   Once installed, open a terminal and run:
```sh
   python --version
   pip --version
```
You should see the Python version (3.8 or higher) and pip version printed in the terminal.

3. Clone the Repository

```bash
git clone https://github.com/shivamksharma/DevBrute.git
```
2. Install the Dependencies :

```bash
cd InnovateX
python3 -m pip install -r requirements.txt
```
3. Create a .env file 
```bash
touch .env
```
Add all the necessary environmental variables like api keys and database keys


4. Run app.py

```bash
python3 app.py 
```

The app should now be live at http://127.0.0.1:5000.
  