# WanderHub  

**WanderHub** is a comprehensive travel planning application built using Python Flask. It aims to provide users with a seamless experience in planning trips by fetching the best flight deals, suggesting preferred hotel stays, managing expenses, and offering weather checks for destinations.  

## Features  

### 1. **Featured Trip**  
- Gathers input from users, such as travel dates, locations.  
- Fetches the best flight and hotel deals based on user criteria.  
- Allows users to choose a plan and calculates the total trip cost.  
- Facilitates payment processing through a third-party payment gateway.  

### 2. **User-Preferred Stay**  
- Suggests a wide range of hotels in the user’s preferred destination.  
- Provides customizable hotel booking options based on user preferences like ratings, location, and budget.  
- Ensures a personalized experience for booking accommodations.  

### 3. **Expense Split**  
- Allows users to split expenses across multiple travel requirements.  
- Simplifies managing group travel expenses by dividing costs.  
- Users can define how much to send and to whom for efficient money management.  

### 4. **Weather Check**  
- Helps users check weather conditions before traveling to a specific location.  
- Provides real-time weather data to assist in travel planning and packing decisions.  

## Technologies Used  
- **Backend**: Python Flask for API development and business logic.  
- **Frontend**: (Optional for this project) HTML/CSS/JavaScript templates for user interface.  
- **APIs**:  
  - Flight deals API for fetching flight options.  
  - Hotel recommendation API for personalized stay suggestions.  
  - Weather API for real-time weather updates.  
- **Database**: Local database for user data and booking information.  
- **Payment Gateway**: Integration with third-party services like PayPal, Stripe, or Razorpay.  


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