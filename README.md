# API Dashboard Project

## Overview
API Dashboard Project is a Python GUI application that integrates multiple APIs and displays real-time information. Users can search weather details, cryptocurrency prices, and latest news articles through a simple Tkinter-based interface.

## Features

* Weather Information Search
* Cryptocurrency Price Tracking
* Latest News Search
* JSON Data Parsing
* Search and Filter Functionality
* Graphical User Interface (GUI)
* Error Handling using Try-Except
* Real-Time API Integration

## Technologies Used

* Python
* Tkinter
* Requests
* Pandas

## APIs Used

### Weather API

https://wttr.in

### Crypto API

https://api.coingecko.com

### News API

https://hn.algolia.com

## Project Structure

```text
API-Dashboard-Project/
│
├── api_dashboard.py
├── README.md
└── screenshots/
```

## Installation

Install the required libraries:

```bash
pip install requests pandas
```

## How to Run

```bash
python api_dashboard.py
```

## Sample Inputs

### Weather Search

Input:

```text
Bangalore
```

### Crypto Search

Input:

```text
bitcoin
```

### News Search

Input:

```text
AI
```

## Sample Outputs

### Weather Output

```text
City: Bangalore
Temperature: 28°C
Humidity: 65%
Weather: Partly Cloudy
Wind Speed: 12 km/h
```

### Crypto Output

```text
Crypto Name: Bitcoin
Price: $105000 USD
```

### News Output

```text
Title: Latest AI Developments
Author: John Doe

Title: Future of Artificial Intelligence
Author: David Smith
```

## Screenshots Required

1. Main Application Window
2. Weather API Output
3. Crypto API Output
4. News API Output
5. GitHub Repository Page

## Learning Outcomes

* Working with REST APIs
* Using the Requests Library
* Parsing JSON Data
* Building GUI Applications with Tkinter
* Handling Exceptions
* Displaying Structured Data Using Pandas

## Author

Nagaraj Naik

## License

This project is created for educational and internship purposes.
