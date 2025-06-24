# MinePLify

---

## ✨ Co robi?

- Spolszcza konfiguracje pluginów Minecraft (np. `.yml`, `.txt` ale możesz wybrać co chcesz)
- Używa AI, by inteligentnie przetłumaczyć tylko istotne fragmenty – takie jak wiadomości, komunikaty, opisy
- Nie musisz kopiować fragmentów tekstu – wystarczy podać cały plik
- Zapisuje wynik do nowego pliku z końcówką `.pl.txt` (txt, zebyś mógł otworzyc odrazu a nie wybierać czy przez np. vsc)

---

## ⚙️ Jak to działa?

1. Wybierasz plik konfiguracyjny przez okno dialogowe
2. Program przesyła jego treść do modelu AI
3. AI tłumaczy plik, zachowując strukturę i kluczowe nazwy
4. Zapisuje spolszczony plik obok oryginału

---

## 🧠 AI

Tłumaczenia są generowane przez model AI deepseek R1. W zależności od dostawcy (providera) modelu, czas oczekiwania może się różnić – zazwyczaj kilka do kilkunastu sekund.

---

## 🔑 Skąd wziąć API Key?

1. Przejdź na stronę: [https://openrouter.ai](https://openrouter.ai)
2. Zarejestruj się lub zaloguj
3. Przejdź do [https://openrouter.ai/keys](https://openrouter.ai/keys)
4. Wygeneruj nowy klucz API
5. Skopiuj go i wklej w miejsce `API_KEY = "xxxxxxxxx"` w kodzie

---

## 📦 Wymagania

- Python 3.8+
- Biblioteki:
  - `requests`
  - `tkinter` (domyślnie w Pythonie)

Zainstaluj wymagane pakiety, jeśli ich nie masz:
```bash
pip install requests
```

---

## 🧪 Dodatkowe informacje

- Program nie zmienia oryginalnego pliku – zapisuje nowy obok niego

---

## 📁 Przykład użycia

1. Uruchom program
2. Wybierz plik `.yml` z konfiguracją pluginu
3. Poczekaj kilka sekund
4. Otrzymasz nowy plik `{nazwa-pliku}.pl.txt` z tłumaczeniem

---

## 🧑‍💻 Licencja

Projekt: **MinePLify**  
Licencja: MIT

---
