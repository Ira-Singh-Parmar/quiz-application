import pandas as pd

# Creating dictionary of Series
employee_data = {
    'ID': pd.Series([101, 102, 103, 104, 105]),
    'NAME': pd.Series(['Raj', 'Simran', 'Amit', 'Rani', 'Vikram']),
    'SALARY': pd.Series([50000, 55000, 48000, 60000, 52000])
}

# Creating DataFrame
df = pd.DataFrame(employee_data)

# Display all columns separately
print("ID Column:")
print(df['ID'])

print("\nNAME Column:")
print(df['NAME'])

print("\nSALARY Column:")
print(df['SALARY'])
