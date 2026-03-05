import tkinter as tk
from tkinter import ttk
from collections import Counter
import matplotlib.pyplot as plt
import time
from datetime import datetime

class CyberKeyDashboard:

    def __init__(self, root):

        self.root = root
        self.root.title("Cyber Keystroke Analytics Dashboard")
        self.root.geometry("1000x600")
        self.root.configure(bg="#0f172a")

        self.key_counts = Counter()
        self.timestamps = []

        self.total_keys = 0
        self.start_time = time.time()

        self.build_ui()

    def build_ui(self):

        title = tk.Label(
            self.root,
            text="CYBER KEYSTROKE ANALYTICS",
            font=("Consolas", 22, "bold"),
            fg="#22c55e",
            bg="#0f172a"
        )
        title.pack(pady=10)

        subtitle = tk.Label(
            self.root,
            text="Educational Keyboard Event Visualizer",
            font=("Consolas", 11),
            fg="#94a3b8",
            bg="#0f172a"
        )
        subtitle.pack()

        main_frame = tk.Frame(self.root, bg="#0f172a")
        main_frame.pack(pady=20)

        input_frame = tk.Frame(main_frame, bg="#1e293b")
        input_frame.grid(row=0, column=0, padx=20)

        tk.Label(
            input_frame,
            text="Type Here",
            fg="white",
            bg="#1e293b",
            font=("Consolas", 12)
        ).pack(pady=5)

        self.text_box = tk.Text(
            input_frame,
            height=6,
            width=40,
            bg="#020617",
            fg="#38bdf8",
            insertbackground="white",
            font=("Consolas", 12)
        )
        self.text_box.pack(padx=10, pady=10)

        self.text_box.bind("<Key>", self.key_pressed)

        stats_frame = tk.Frame(main_frame, bg="#1e293b")
        stats_frame.grid(row=0, column=1, padx=20)

        self.total_label = tk.Label(
            stats_frame,
            text="Total Keys: 0",
            font=("Consolas", 14),
            fg="#22c55e",
            bg="#1e293b"
        )
        self.total_label.pack(pady=10)

        self.speed_label = tk.Label(
            stats_frame,
            text="Typing Speed: 0 keys/sec",
            font=("Consolas", 14),
            fg="#38bdf8",
            bg="#1e293b"
        )
        self.speed_label.pack(pady=10)

        self.unique_label = tk.Label(
            stats_frame,
            text="Unique Keys: 0",
            font=("Consolas", 14),
            fg="#f59e0b",
            bg="#1e293b"
        )
        self.unique_label.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#0f172a")
        button_frame.pack(pady=20)

        ttk.Button(
            button_frame,
            text="Key Frequency Chart",
            command=self.show_frequency_chart
        ).grid(row=0, column=0, padx=10)

        ttk.Button(
            button_frame,
            text="Typing Speed Chart",
            command=self.show_speed_chart
        ).grid(row=0, column=1, padx=10)

        ttk.Button(
            button_frame,
            text="Clear Data",
            command=self.clear_data
        ).grid(row=0, column=2, padx=10)

        log_frame = tk.Frame(self.root, bg="#1e293b")
        log_frame.pack(pady=10)

        tk.Label(
            log_frame,
            text="Live Event Log",
            fg="white",
            bg="#1e293b",
            font=("Consolas", 12)
        ).pack()

        self.log_box = tk.Text(
            log_frame,
            height=10,
            width=100,
            bg="#020617",
            fg="#22c55e",
            font=("Consolas", 10)
        )
        self.log_box.pack(padx=10, pady=10)

    def key_pressed(self, event):

        key = event.keysym

        self.total_keys += 1
        self.key_counts[key] += 1
        self.timestamps.append(time.time())

        self.update_stats()

        timestamp = datetime.now().strftime("%H:%M:%S")

        log = f"[{timestamp}] Key Pressed → {key}\n"

        self.log_box.insert(tk.END, log)
        self.log_box.see(tk.END)

    def update_stats(self):

        self.total_label.config(text=f"Total Keys: {self.total_keys}")

        elapsed = time.time() - self.start_time

        if elapsed > 0:
            speed = self.total_keys / elapsed
            self.speed_label.config(text=f"Typing Speed: {speed:.2f} keys/sec")

        self.unique_label.config(text=f"Unique Keys: {len(self.key_counts)}")

    def show_frequency_chart(self):

        if not self.key_counts:
            return

        keys = list(self.key_counts.keys())
        counts = list(self.key_counts.values())

        plt.style.use("dark_background")

        plt.figure(figsize=(8,5))
        plt.bar(keys, counts, color="cyan")

        plt.title("Key Frequency")
        plt.xlabel("Key")
        plt.ylabel("Count")

        plt.xticks(rotation=45)

        plt.show()

    def show_speed_chart(self):

        if len(self.timestamps) < 2:
            return

        intervals = []

        for i in range(1, len(self.timestamps)):
            intervals.append(self.timestamps[i] - self.timestamps[i-1])

        plt.style.use("dark_background")

        plt.figure(figsize=(8,5))
        plt.plot(intervals, color="lime")

        plt.title("Time Between Keystrokes")
        plt.xlabel("Keystroke Event")
        plt.ylabel("Seconds")

        plt.show()

    def clear_data(self):

        self.key_counts.clear()
        self.timestamps.clear()
        self.total_keys = 0
        self.start_time = time.time()

        self.log_box.delete("1.0", tk.END)

        self.update_stats()


def main():

    root = tk.Tk()
    app = CyberKeyDashboard(root)
    root.mainloop()


if __name__ == "__main__":
    main()