from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import datetime

app = Flask(__name__)

# Sample function to scrape prices from a grocery API or website
def get_grocery_prices():
    # Replace this with actual API calls or scraping logic
    return {
        'milk': 3.49,
        'bread': 2.99,
        'eggs': 4.19,
        'chicken': 5.99
    }

# Function to calculate price change since a given date
def calculate_price_change(current_prices, historical_prices):
    price_changes = {}
    for item, current_price in current_prices.items():
        if item in historical_prices:
            change = ((current_price - historical_prices[item]) / historical_prices[item]) * 100
            price_changes[item] = round(change, 2)
    return price_changes

# Sample route for the home page
@app.route('/')
def index():
    current_prices = get_grocery_prices()
    # Replace with actual historical data from January 20, 2025
    historical_prices = {
        'milk': 3.00,
        'bread': 2.50,
        'eggs': 3.99,
        'chicken': 5.50
    }
    price_changes = calculate_price_change(current_prices, historical_prices)
    return render_template('index.html', current_prices=current_prices, price_changes=price_changes)

if __name__ == '__main__':
    app.run(debug=True)
