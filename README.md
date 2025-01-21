# Real-Time Flight Prices Scraper - Google Flights

This project is a Python program that uses the **Selenium** library to scrape data from **Google Flights**, collecting real-time information about flight ticket prices.

## 🚀 Features

- Fetches flight ticket prices for specific routes.
- Filters flights by date and airline.
- Saves the scraped data into **CSV** files for analysis.

## 🛠️ Technologies Used

- **Python 3.8+**
- **Selenium**
- **Google Chrome** and **ChromeDriver**

## 📋 Requirements

Before running the project, ensure you have the following installed:

1. Python 3.8 or later.
2. Google Chrome.
3. The ChromeDriver version matching your browser.
4. Required Python libraries:
   ```bash
   pip install selenium
   
📂 Project Structure
web-scraping-google-flights/
│
├── main.py              # Main script for running the program
├── utils.py             # Auxiliary functions for processing
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── output/              # Directory for storing generated CSV files

🔧 Setup and Execution
1. Clone this repository:
   git clone https://github.com/borges12matheus/Selenium-Web-Scrapping.git
   cd Selenium-Web-Scrapping
   
3. Install the dependencies:
   pip install -r requirements.txt

4. Download ChromeDriver and configure the path in the main.py file:
   driver_path = "PATH/TO/CHROMEDRIVER"

5. Run the program:
   python main.py

⚠️ Legal Disclaimer
The use of scraping tools must comply with the Terms of Service of Google Flights.
Scraping automated data can violate site policies and may result in IP bans. Use this project responsibly.

🖊️ Author
Developed by Matheus.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
