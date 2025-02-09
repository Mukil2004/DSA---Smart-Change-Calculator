import tkinter as tk
from tkinter import messagebox

def coin_change_ways(coins, target):
    # Initialize dp array and base case
    dp = [0] * (target + 1)
    dp[0] = 1

    # Track combinations of coins for each amount
    combinations = [[] for _ in range(target + 1)]
    combinations[0] = [[]]  # Initialize with an empty combination

    # Fill dp and track combinations
    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]
            for comb in combinations[amount - coin]:
                combinations[amount].append(comb + [coin])

    return dp[target], combinations[target]

def solve_coin_change():
    try:
        # Get user inputs
        target = int(target_entry.get())
        coin_values = list(map(int, coins_entry.get().split()))

        # Solve the coin change problem
        ways, combinations = coin_change_ways(coin_values, target)

        # Display results
        if ways == 0:
            result_label.config(text="No solution possible with given denominations.")
            ways_text.delete(1.0, tk.END)
        else:
            result_label.config(text=f"💰 Number of ways to make change: {ways} 💰")
            ways_text.delete(1.0, tk.END)
            for comb in combinations:
                ways_text.insert(tk.END, "💵 " + ", ".join(map(str, comb)) + " 💵\n\n")  # Add money emojis and spacing
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for the target and coin denominations.")

# Create the main GUI window
window = tk.Tk()
window.title(" Smart Change Calculator ")
window.geometry("500x500")
window.configure(bg="#f7f3e9")

# Header label
header_label = tk.Label(window, text="💵 Smart Change Calculator 💵", font=("Arial", 16, "bold"), bg="#4682b4", fg="white", pady=10)
header_label.pack(fill="x")

# Input fields
tk.Label(window, text="Enter target amount:", font=("Arial", 12), bg="#f7f3e9", fg="#3a3a3a").pack(pady=5)
target_entry = tk.Entry(window, font=("Arial", 12), width=20, bg="#ffffff", fg="#000000", relief="solid")
target_entry.pack(pady=5)

tk.Label(window, text="Enter coin denominations (space-separated):", font=("Arial", 12), bg="#f7f3e9", fg="#3a3a3a").pack(pady=5)
coins_entry = tk.Entry(window, font=("Arial", 12), width=30, bg="#ffffff", fg="#000000", relief="solid")
coins_entry.pack(pady=5)

# Solve button
solve_button = tk.Button(window, text="💰 Solve 💰", font=("Arial", 12, "bold"), bg="#4682b4", fg="white", command=solve_coin_change)
solve_button.pack(pady=10)

# Output display
result_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="#f7f3e9", fg="#1e5128")
result_label.pack(pady=5)

ways_text = tk.Text(window, height=12, width=50, font=("Arial", 12), bg="#e6f7ff", fg="#3a3a3a", wrap="word", padx=10, pady=10, relief="solid")
ways_text.pack(pady=10)

# Footer
footer_label = tk.Label(window, text="💵 Happy Saving! 💵", font=("Arial", 10), bg="#4682b4", fg="white", pady=5)
footer_label.pack(side="bottom", fill="x")

# Start the Tkinter main loop
window.mainloop()


