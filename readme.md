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
```plaintext
├── app.py                  # Entry point of the Flask application  
├── controllers             # Handles route logic  
│   ├── authController.py   # Manages user authentication and data  
│   ├── featuredTrip.py     # Handles flight and hotel fetching logic  
│   ├── expenseSplit.py     # Handles expense-splitting functionality  
│   ├──weatherCheck.py     # Handles weather API calls  
├   └──templates   
├── services                # Contains business logic for APIs  
│   ├── Flight_Services.py  # Fetches flight details  
│   ├── Hotel_Recommendation.py # Provides hotel recommendations  
│   └── PaymentService.py   # Manages payment gateway integration  
            # HTML templates for frontend  
├── static                  # Static files like CSS and JavaScript  
├── README.md               # Documentation  
