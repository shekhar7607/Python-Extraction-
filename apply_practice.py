import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'salary': [25000, 30000, 35000, 40000, 45000]
})



def category(row):
    if row['salary'] <= 30000:
        return "Low"
    else:
        return "High"


# define the category of the salary
df['category'] = df.apply(category, axis=1)

df.to_excel("employees_updated_category.xlsx", index=False)

print(df)
