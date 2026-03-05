# Cyber Keystroke Analytics Dashboard

An educational Python project that visualizes keyboard activity inside a GUI application.
This program demonstrates **keystroke analytics, event logging, and data visualization** using a modern dashboard-style interface.

⚠️ **Important:**
This program only records keys typed **inside the application’s text box**. It does **not capture system-wide keystrokes** and is designed purely for **educational and cybersecurity learning purposes**.

---

## Features

* Dark themed **cyber-style GUI dashboard**
* Real-time **keystroke monitoring**
* **Typing speed analysis**
* **Key frequency tracking**
* **Interactive charts using Matplotlib**
* Live **event log with timestamps**
* Ability to **reset analytics data**

---

## Technologies Used

* **Python 3**
* **Tkinter** (GUI framework)
* **Matplotlib** (data visualization)
* **Collections.Counter** (frequency analysis)

---

## Installation

1. Clone the repository or download the project files.

2. Install required dependencies:

```bash
pip install matplotlib
```

3. Run the program:

```bash
python keyloz.py
```

---

## How It Works

1. Launch the application.
2. Type inside the **text input box**.
3. The dashboard will:

   * Track total keystrokes
   * Calculate typing speed
   * Record unique keys used
4. Use the buttons to display analytics charts.

Available charts:

* **Key Frequency Chart** – shows which keys are pressed most often.
* **Typing Speed Chart** – visualizes the time between keystrokes.

---

## Example Use Cases

This project can be used for learning:

* Keyboard event handling
* Behavioral analytics
* Security monitoring concepts
* Data visualization
* GUI development with Python

It is particularly useful for **cybersecurity students and developers** exploring how user behavior can be analyzed.

---

## Project Structure

```
project-folder
│
├── keyloz.py
├── README.md
```

---

## Disclaimer

This project is provided **strictly for educational purposes**.
It does **not implement system-level monitoring or surveillance functionality**.

Always respect **user privacy, ethical guidelines, and local laws** when working with monitoring software.

---

## Author

Cybersecurity learning project created for educational demonstrations and blog tutorials.