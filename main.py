import os
import tkinter as tk
from tkinter import filedialog
import requests
import json

API_KEY = "xxxxxxxxx"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def select_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title="Wybierz plik config pluginu Minecraft",
                                      filetypes=[("Pliki tekstowe", "*.txt *.yml"), ("Wszystkie pliki", "*.*")])

def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def save_file(path, text):
    out = path + ".pl.txt"
    with open(out, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Zapisano:", out)

def transfemboy(text):
    prompt = (
        "Jesteś AI tłumaczącym konfigurację pluginu Minecraft. "
        "Spolszcz tylko te fragmenty, które rzeczywiście się edytuje (np. wiadomości, komunikaty, nazwy opcji), "
        "zachowując resztę bez zmian. "
        "ZWROC TYLKO POPRAWIONY TEKST – CAŁĄ ZAWARTOŚĆ PLIKU, NIC WIĘCEJ."
    )
    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/xynuk/MinePLify",
        "X-Title": "MinePLify"
    }
    resp = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]

def main():
    file = select_file()
    if not file:
        print("Nie wybrano pliku.")
        return
    configtext = load_file(file)
    out = transfemboy(configtext)
    save_file(file, out)

if __name__ == "__main__":
    main()
