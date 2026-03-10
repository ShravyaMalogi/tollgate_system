import pandas as pd
from datetime import date


def get_balance(vehicle):

    df = pd.read_csv("data/balance.csv")

    row = df[df["vehicle_no"] == vehicle]

    if row.empty:
        return None

    return row.iloc[0]["balance"]


def deduct_toll(vehicle):

    df = pd.read_csv("data/balance.csv")

    row = df[df["vehicle_no"] == vehicle]

    if row.empty:
        return False

    balance = row.iloc[0]["balance"]

    if balance < 20:
        return False

    df.loc[df["vehicle_no"] == vehicle, "balance"] -= 20

    df.to_csv("data/balance.csv", index=False)

    add_payment(vehicle)

    return True


def add_payment(vehicle):

    df = pd.read_csv("data/payments.csv")

    new_row = {
        "vehicle_no": vehicle,
        "amount": 20,
        "date": str(date.today())
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_csv("data/payments.csv", index=False)
