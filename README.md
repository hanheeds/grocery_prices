# Grocery Price Index Tracker

A comprehensive web application for tracking and displaying grocery price data from top grocery markets in the United States, with a focus on showing how prices have changed since January 20th, 2025, which marks the end of Biden's Term.

This project was started with the intention of keeping Trump accountable for his words. One of his big campaign promises was to restore the 'economy', in which a big example was increasing grocery prices. While it is known that the president can not directy influence the economy, we want to show if Trump's term can actually lower grocery prices.

## Project Overview

This project aims to create a full website that gathers price data for essential grocery items, calculates changes over time, and displays the data in a user-friendly format. The platform will enable users to see price trends and better understand the cost of essential items.

## Key Features

- **Web Scraping and API Integration**: Collect current grocery price data using web scraping tools like `BeautifulSoup` or integrate with public APIs (e.g., Walmart, Kroger).
- **Database Storage**: Store historical and current price data using databases like PostgreSQL or SQLite.
- **Backend Development**: Utilize Python with frameworks such as Flask or Django to create routes for data fetching and processing.
- **Frontend Development**: Build an interactive user interface using HTML, CSS, and JavaScript. Implement visualizations with libraries like Chart.js or D3.js.

## Project Structure

### 1. Backend (Python using Flask)

Create a Flask app that gathers current grocery prices, stores them, and calculates changes since a specified date.

### 2. Frontend (HTML Template)

Develop the main webpage to display price changes and trends with interactive charts.

### 3. Database Setup

- Use SQLAlchemy or Django ORM to manage price history data.
- Implement scheduled jobs (e.g., using `cron` or `Celery`) for periodic data updates.

## Code Outline

### Backend Code Sample (Python with Flask)
