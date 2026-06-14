
import pandas as pd

df = pd.read_excel("trip.xlsx")

total_unique_trips = df['trip ID'].nunique()
print(f"Total unique trips: {total_unique_trips}")


print("gender counts:")
print(df["gender"].value_counts())


print(f"Total Employees: {df['empid'].nunique()}")


escort_trips = df[df['escort'] == 'no'].count()['trip ID']
print(f"Total No Escort Trips: {escort_trips}")

female_employee = df[df['escort'] == 'yes'][['empid','name']]

print(female_employee)