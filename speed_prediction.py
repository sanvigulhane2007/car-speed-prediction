import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import messagebox

# Load dataset
import os

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "speed_data.csv")

data = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Car-Speed-Prediction\speed_data.csv")

X = data[['Distance', 'Time']]
y = data['Speed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

# GUI
def predict():
    try:
        d = float(entry_distance.get())
        t = float(entry_time.get())

        new_data = pd.DataFrame([[d, t]], columns=['Distance', 'Time'])
        result = model.predict(new_data)

        messagebox.showinfo("Result", f"Predicted Speed: {result[0]:.2f}")
    except:
        messagebox.showerror("Error", "Invalid input!")

root = tk.Tk()
root.title("Speed Predictor")

tk.Label(root, text="Distance").pack()
entry_distance = tk.Entry(root)
entry_distance.pack()

tk.Label(root, text="Time").pack()
entry_time = tk.Entry(root)
entry_time.pack()

tk.Button(root, text="Predict", command=predict).pack()

root.mainloop()