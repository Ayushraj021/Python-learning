import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        output_label.config(text=f"Result: {result}")
    except Exception as e:
        output_label.config(text="Error!")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget for input expression
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    tk.Button(window, text=button, width=5, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Button to calculate result
calculate_button = tk.Button(window, text="Calculate", width=10, command=calculate)
calculate_button.grid(row=row, column=0, columnspan=4, pady=10)

# Label to display output
output_label = tk.Label(window, text="")
output_label.grid(row=row+1, column=0, columnspan=4)

# Run the main event loop
window.mainloop()
