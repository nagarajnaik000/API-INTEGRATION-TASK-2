import requests
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from datetime import datetime

# ==========================================
# CREATE MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("API Dashboard - Weather | Crypto | News")
root.geometry("750x650")
root.resizable(False, False)

# ==========================================
# FUNCTION TO DISPLAY OUTPUT
# ==========================================

def show_output(text):
    output_box.delete(1.0, tk.END)

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    output_box.insert(
        tk.END,
        f"Generated On: {current_time}\n\n{text}"
    )

# ==========================================
# WEATHER API FUNCTION
# ==========================================

def get_weather():

    city = entry_box.get().strip()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = f"https://wttr.in/{city}?format=j1"

    try:

        response = requests.get(url)
        data = response.json()

        current = data['current_condition'][0]

        result = f"""
========== WEATHER DETAILS ==========

City: {city}

Temperature: {current['temp_C']} °C

Humidity: {current['humidity']} %

Weather: {current['weatherDesc'][0]['value']}

Wind Speed: {current['windspeedKmph']} km/h
"""

        show_output(result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ==========================================
# CRYPTO API FUNCTION
# ==========================================

def get_crypto():

    crypto = entry_box.get().lower().strip()

    if crypto == "":
        messagebox.showwarning("Input Error", "Please enter crypto name")
        return

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        'ids': crypto,
        'vs_currencies': 'usd'
    }

    try:

        response = requests.get(url, params=params)
        data = response.json()

        if crypto in data:

            result = f"""
========== CRYPTO DETAILS ==========

Crypto Name: {crypto.title()}

Price: ${data[crypto]['usd']} USD
"""

            show_output(result)

        else:

            show_output("Crypto Not Found")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ==========================================
# NEWS API FUNCTION
# ==========================================

def get_news():

    topic = entry_box.get().strip()

    if topic == "":
        messagebox.showwarning("Input Error", "Please enter a news topic")
        return

    url = f"https://hn.algolia.com/api/v1/search?query={topic}"

    try:

        response = requests.get(url)
        data = response.json()

        articles = data['hits'][:5]

        news_list = []

        for article in articles:

            news_list.append({
                "Title": article.get('title'),
                "Author": article.get('author')
            })

        df = pd.DataFrame(news_list)

        result = "\n========== LATEST NEWS ==========\n\n"
        result += df.to_string(index=False)

        show_output(result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ==========================================
# CLEAR FUNCTION
# ==========================================

def clear_data():
    entry_box.delete(0, tk.END)
    output_box.delete(1.0, tk.END)

# ==========================================
# HEADING
# ==========================================

heading = tk.Label(
    root,
    text="API INTEGRATION DASHBOARD",
    font=("Arial", 20, "bold")
)

heading.pack(pady=20)

# ==========================================
# INPUT LABEL
# ==========================================

input_label = tk.Label(
    root,
    text="Enter City / Crypto / News Topic:",
    font=("Arial", 12)
)

input_label.pack()

# ==========================================
# ENTRY BOX
# ==========================================

entry_box = tk.Entry(
    root,
    width=40,
    font=("Arial", 14)
)

entry_box.pack(pady=10)

# ==========================================
# BUTTON FRAME
# ==========================================

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# ==========================================
# WEATHER BUTTON
# ==========================================

weather_button = tk.Button(
    button_frame,
    text="Weather API",
    font=("Arial", 12),
    command=get_weather,
    width=15
)

weather_button.grid(row=0, column=0, padx=10)

# ==========================================
# CRYPTO BUTTON
# ==========================================

crypto_button = tk.Button(
    button_frame,
    text="Crypto API",
    font=("Arial", 12),
    command=get_crypto,
    width=15
)

crypto_button.grid(row=0, column=1, padx=10)

# ==========================================
# NEWS BUTTON
# ==========================================

news_button = tk.Button(
    button_frame,
    text="News API",
    font=("Arial", 12),
    command=get_news,
    width=15
)

news_button.grid(row=0, column=2, padx=10)

# ==========================================
# CLEAR BUTTON
# ==========================================

clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12),
    command=clear_data,
    width=20
)

clear_button.pack(pady=10)

# ==========================================
# OUTPUT BOX
# ==========================================

output_box = ScrolledText(
    root,
    width=85,
    height=22,
    font=("Consolas", 10)
)

output_box.pack(pady=20)

# ==========================================
# RUN APPLICATION
# ==========================================

root.mainloop()
