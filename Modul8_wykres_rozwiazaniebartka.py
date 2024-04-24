import csv
from datetime import datetime

import matplotlib.pyplot as plt

months = {
    1: 'styczeń',
    2: 'luty',
    3: 'marzec',
    4: 'kwiecień',
    5: 'maj',
    6: 'czerwiec',
    7: 'lipiec',
    8: 'sierpień',
    9: 'wrzesień',
    10: 'październik',
    11: 'listopad',
    12: 'grudzień'
}
income = {}
spent = {}
action = {}
with open("operacje.csv", encoding="utf8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        time = datetime.strptime(row["data"], "%Y-%m-%d").month
        if row["rodzaj operacji"] == "przychód":
            income[months[time]] = income.get(months[time], 0) + int(
                row["kwota operacji"])
        elif row["rodzaj operacji"] == "wydatek":
            spent[months[time]] = spent.get(months[time], 0) + int(
                row["kwota operacji"])

        action[months[time]] = action.get(months[time], 0) + 1

month = list(income.keys())
income_month = [
    income - spent for income, spent in zip(income.values(), spent.values())
]
action_per_month = list(action.values())

fig, ax = plt.subplots()
ax.set_xlabel("months")

ax.set(ylabel="income", title="income by month")
y_values = range(1000, 5000, 250)
ax.set_yticks(y_values)

ax.bar(month, income_month)
plt.savefig("podsumowanie.png")

ax.set_xlabel("months")
ax.set(ylabel="action", title="action by month")
y_values = range(1, 20, 1)
ax.set_yticks(y_values)
ax.bar(month, action_per_month)
plt.savefig("ilosc_operacji.jpg")

print(income)
print(spent)