import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def update_currency_label_1(event):
    code = base_combobox_1.get()
    name = currencies[code]
    currency_label_1.config(text=name)

def update_currency_label_2(event):
    code = base_combobox_2.get()
    name = currencies[code]
    currency_label_2.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox_1.get()
    if target_code and base_code:
        try:
            result = requests.get(f"https://open.er-api.com/v6/latest/{base_code}")
            result.raise_for_status()
            data = result.json()
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]

                mb.showinfo('Курс обмена',
                            f'Курс '
                            f'  {exchange_rate:.1f}  {target} за 1 {base}')
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')


        except Exception as e:
            mb.showerror('Ошибка', f'error 400 {e}')


currencies = {
    "USD": "Доллар США",
    "EUR": "Евро",
    "CNY": "Юань",
    "RUB": "Российский рубль",
}

pop_curr = ['EUR', 'USD', 'RUB', 'CNY']

root = Tk()
root.title("Курс обмена валют ")
root.geometry("300x350")
Label(text='Базовая валюта').pack(pady=10, padx=10)
base_combobox_1 = ttk.Combobox(values=list(currencies.keys()))
base_combobox_1.pack()
currency_label_1 = ttk.Label()
currency_label_1.pack(pady=10, padx=10)
base_combobox_1.bind("<<ComboboxSelected>>", update_currency_label_1)

Label(text='Вторая базовая валюта').pack(pady=10, padx=10)
base_combobox_2 = ttk.Combobox(values=list(currencies.keys()))
base_combobox_2.pack()
currency_label_2 = ttk.Label()
currency_label_2.pack(pady=10, padx=10)
base_combobox_2.bind("<<ComboboxSelected>>", update_currency_label_2)

Label(text='Целевая валюта').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(currencies))
target_combobox.pack()
currency_label = ttk.Label()
currency_label.pack(pady=10, padx=10)

button = Button(text='Получить курс обмена', command=exchange)
button.pack()
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)
root.mainloop()