import tkinter as tk
from tkinter import ttk, messagebox
import time
import matplotlib.pyplot as plt

def compute_bmi(weight_kg, height_m):
    """Calculate BMI given weight (kg) and height (m)."""
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi_value):
    """Return BMI category."""
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"

def recommended_weight_range(height_m):
    """Return healthy weight range (kg) for given height."""
    return 18.5 * (height_m ** 2), 24.9 * (height_m ** 2)

def on_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight_unit.get() == "lbs":
            weight *= 0.453592
        if height_unit.get() == "feet":
            height *= 0.3048

        if weight <= 0 or height <= 0:
            raise ValueError("Values must be positive.")

        bmi_val = compute_bmi(weight, height)
        category = classify_bmi(bmi_val)
        low_w, high_w = recommended_weight_range(height)

        result_var.set(f"BMI: {bmi_val:.2f} ({category})")
        range_var.set(f"Healthy Weight Range: {low_w:.1f} - {high_w:.1f} kg")

        bmi_history.append(bmi_val)
        user_data.append((weight, height, bmi_val, category))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

def show_history():
    if not user_data:
        messagebox.showinfo("History", "No data recorded yet.")
        return
    history_str = "\n".join(
        f"Weight: {w:.1f}kg | Height: {h:.2f}m | BMI: {b:.2f} ({cat})"
        for w, h, b, cat in user_data
    )
    messagebox.showinfo("BMI History", history_str)

def show_trend():
    if not bmi_history:
        messagebox.showinfo("Trend", "No data to plot.")
        return
    plt.plot(bmi_history, marker='o', color='blue')
    plt.title("BMI Trend")
    plt.xlabel("Entry Number")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.show()

root = tk.Tk()
root.title("BMI Calculator Pro")
root.geometry("500x350")
root.configure(bg="#eef2f3")

main_frame = ttk.Frame(root, padding=15)
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Weight:").grid(row=0, column=0, sticky="w")
weight_entry = ttk.Entry(main_frame, width=10)
weight_entry.grid(row=0, column=1)
weight_unit = tk.StringVar(value="kgs")
ttk.Combobox(main_frame, textvariable=weight_unit, values=("kgs", "lbs"), width=5, state="readonly").grid(row=0, column=2)

ttk.Label(main_frame, text="Height:").grid(row=1, column=0, sticky="w")
height_entry = ttk.Entry(main_frame, width=10)
height_entry.grid(row=1, column=1)
height_unit = tk.StringVar(value="meters")
ttk.Combobox(main_frame, textvariable=height_unit, values=("meters", "feet"), width=5, state="readonly").grid(row=1, column=2)

ttk.Button(main_frame, text="Calculate BMI", command=on_calculate).grid(row=2, column=0, columnspan=3, pady=8)
ttk.Button(main_frame, text="Show History", command=show_history).grid(row=3, column=0, columnspan=3, pady=5)
ttk.Button(main_frame, text="Show Trend", command=show_trend).grid(row=4, column=0, columnspan=3, pady=5)

result_var = tk.StringVar(value="BMI: ")
ttk.Label(main_frame, textvariable=result_var, font=("Arial", 12)).grid(row=5, column=0, columnspan=3, pady=5)

range_var = tk.StringVar(value="Healthy Weight Range: ")
ttk.Label(main_frame, textvariable=range_var, font=("Arial", 10)).grid(row=6, column=0, columnspan=3, pady=3)

bmi_history = []
user_data = []

root.mainloop()






