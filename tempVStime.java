
import numpy as np
import matplotlib.pyplot as plt #  to plot graph
import tkinter as tk
from tkinter import ttk


# Coefficients bo and b1
def coef(x,y):
   n= np.size(x)
   # mean of x and y
   m_x=np.mean(x)
   m_y=np.mean(y)

   # formula exection is start
   upper=np.sum(x*y)-n*m_x*m_y
   lower=np.sum(x*x)-n*m_x*m_x

   b1=upper/lower
   b0=m_y-b1*m_x
   return b0,b1

# to predict new data
def newdata(x,b1,b0):
    y=b0 + b1*x
    return y



# Sample data: Time of day (in hours) vs. Temperature (in Celsius)
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
y = np.array([5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 28, 26, 24, 22, 20, 18, 16, 14, 10])

# Train the model
b0, b1 = coef(x, y)

# GUI Application
class TempApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Prediction")
        self.geometry("300x200")

        self.label = ttk.Label(self, text="Enter the time of day (0-23):")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(self)
        self.entry.pack(pady=10)

        self.button = ttk.Button(self, text="Predict Temperature", command=self.predict_temperature)
        self.button.pack(pady=10)

        self.result = ttk.Label(self, text="")
        self.result.pack(pady=10)

        self.icon = tk.Label(self)
        self.icon.pack(pady=10)

    def predict_temperature(self):
        try:
            time_of_day = float(self.entry.get())
            predicted_temp = newdata(time_of_day, b1, b0)
            self.result.config(text=f"Predicted Temperature: {predicted_temp:.2f}°C")

            # Update icon based on temperature
            if predicted_temp < 10:
                self.icon.config(text="❄️", font=("Arial", 50))
            elif 10 <= predicted_temp < 20:
                self.icon.config(text="☁️", font=("Arial", 50))
            else:
                self.icon.config(text="☀️", font=("Arial", 50))
        except ValueError:
            self.result.config(text="Please enter a valid number.")

if __name__ == "__main__":
    app = TempApp()
    app.mainloop()
