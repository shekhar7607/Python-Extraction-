
import pandas as pd

df = pd.read_excel("trip.xlsx")


escort_trip = len(df[df["escort"] == "yes"])

print(f"Number of escort trips: {escort_trip}")

count =0
for name in df['name']:
    if name[:2] == 'sw':
        count += 1


print(f"Number of trips with names starting with 'Sw': {count}")