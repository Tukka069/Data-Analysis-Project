import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Sale Report.csv')

print((df[df['Stock'] == 5.0]).head() )

numerical_columns = df.select_dtypes(include=['number']).columns
text_columns = df.select_dtypes(include=['object']).columns

for column in numerical_columns:
    df[column].fillna(df[column].mean(), inplace=True)

for column in text_columns:
    most_repeated_value = df[column].mode()[0] 
    df[column].fillna(most_repeated_value, inplace=True)

# stock_by_category = df.groupby('Category')['Stock'].sum()

# stock_by_category.plot(kind='bar', color='skyblue', figsize=(10, 6))
# plt.title('Total Stock by Category')
# plt.xlabel('Category')
# plt.ylabel('Total Stock')
# plt.show()

stock_by_design_number = df.groupby('Design No.')['Stock'].sum()

stock_by_design_number.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Total Stock by Design  number')
plt.xlabel('Design number')
plt.ylabel('Total Stock')
plt.show()

