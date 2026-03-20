import glob
import pandas as pd
import numpy as np
import openpyxl
import requests

file_path = "data/test.xlsx"

# new_df = pd.read_excel(
#     file_path,
#     sheet_name='Sales', # Ім'я або номер аркуша
#     usecols='A:D', # Вказуємо, які стовпці читати
#     skiprows=2 # Пропускаємо 2 верхній рядки
# )
#
# print(new_df.head())

# data = {
#     'Product': ['Laptop', 'Mouse', 'Keyboard'],
#     'Price': [1200, 25, 75],
#     'Stock': [30, 150, 80]
# }
#
# df = pd.DataFrame(data)

# print(df)
# print(df[["Price", "Stock"]])
# print(df.iloc[:3])


# df.to_excel(file_path, sheet_name="Sales3", index=False)


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Department': ['HR', 'IT', 'IT', 'HR'],
#     'Salary': [70000, 85000, 92000, 68000]
# }
# employees_df = pd.DataFrame(data)
#
# filtered_employees = employees_df[
#     (employees_df['Department'] == 'IT') & ((employees_df['Salary'] > 70000) | (employees_df['Name'][0] == "B"))
# ]
#
# # print(filtered_employees)
#
# sorted_emplyees = employees_df.sort_values(
#     by=['Department', 'Salary'],
#     ascending=[True, False]
# )
# print(sorted_emplyees)


# numpy потрібен для створення NaN
# Дані з пропусками та дублікатами

# data = {
#     'OrderID': [1, 2, 3, 4, 2],
#     'Product': ['A', 'B', 'A', 'C', 'B'],
#     'Amount': [12, 150, np.nan, 200, 5000]
# }
#
# orders_df = pd.DataFrame(data)

# cleaned_df = orders_df.drop_duplicates(subset="Product")
# cleaned_df = cleaned_df.drop_duplicates(subset="Amount")

# mean_amount = orders_df['Amount'].mean()
# orders_df.fillna({"Amount": mean_amount}, inplace=True)

# data = {
#     'Region': ['North', 'West', 'North', 'South', 'West'],
#     'Sales': [1000, 1500, 1200, 800, 1800]
# }
#
# sales_df = pd.DataFrame(data)
# Групуємо дані за регіоном і рахуємо загальну суму продажів для кожного
# regional_sales = (
#     sales_df.groupby('Region')
#     ['Sales']
#     .sum()
#     .reset_index()
# )
# print(regional_sales)

# df_jan = pd.DataFrame({'Product': ['A', 'B'], 'Sales': [100, 150]})
# df_feb = pd.DataFrame({'Product': ['A', 'C'], 'Sales': [120, 200]})
#
# # Вертикально об'єднуємо два DataFrame
# total_sales = pd.concat([df_jan, df_feb], ignore_index=True)
# print(total_sales)

# Таблиця продажів
# sales = pd.DataFrame({'ProductID': [101, 102, 103], 'Amount': [2, 1, 5]})
# # Довідник продуктів
# products = pd.DataFrame({'ProductID': [101, 102, 104], 'Name': ['Widget', 'Gadget', 'Thingamajig']})
#
# # Об'єднуємо таблиці, щоб додати назви продуктів до продажів
# merged_df = pd.merge(sales, products, how='outer')
# print(merged_df)

# Шлях до папки з файлами
# path = 'data/monthly_reports'
# # Шаблон для пошуку всіх .xlsx файлів у цій
# all_files = glob.glob(path + "/" + "*.xlsx")
#
# li = [pd.read_excel(file, index_col=None, header=0) for file in all_files]
#
# annual_report = pd.concat(li, axis=0, ignore_index=True)
#
# grouped_report = (
#     annual_report.groupby("Week")
#     [["Income", "Expense"]]
#     .sum()
#     .reset_index()
# )

# grouped_report.to_excel(f'{path}/annual.xlsx', index=False)

# data = {
#     'Date': pd.to_datetime(['2023-01-05', '2023-01-05', '2023-01-06', '2023-01-06']),
#     'Region': ['North', 'South', 'North', 'South'],
#     'Sales': [100, 150, 120, 180]
# }
#
# df = pd.DataFrame(data)
#
# formatter = df.style.format({"Sales": "${:,.2f}"})
#
# # Створюємо зведену таблицю:
# # Індекс - дати, стовпці - регіони, значення - сума продажів
# pivot = df.pivot_table(
#     index='Date',
#     columns='Region',
#     values='Sales',
#     aggfunc='sum'
# )
# print(pivot)
#
# pivot.to_excel('data/test.xlsx')


# summary_table = pd.DataFrame({
#     'Product Category': ['Electronics and Gadgets, Electronics and Gadgets, Electronics and Gadgets, Electronics and Gadgets, Electronics and Gadgets', 'Home Appliances'],
#     'Total Revenue Q1': [150000.75, 85000.50]
# })
# output_path = 'data/formatted_summary.xlsx'
#
# with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
#     summary_table.to_excel(writer, sheet_name='Summary', index=False)
#     # Отримуємо доступ до об'єкта аркуша openpyxl
#     worksheet = writer.sheets['Summary']
#
#     # Проходимо по стовпцях і встановлюємо ширину
#     for column_cells in worksheet.columns:
#         length = max(len(str(cell.value)) for cell in column_cells)
#         worksheet.column_dimensions[column_cells[0].column_letter].width = length + 2
# print("Formatted report saved.")

file_path = "data/example2.xlsx"
base_url="https://api.github.com/users/{username}"


def get_github_user_info(username):
    url = base_url.format(username=username)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def write_to_excel(data, file_path):
    if data is None:
        raise ValueError("No data returned from GitHub API.")

    df = pd.json_normalize(data)

    df.to_excel(file_path, sheet_name="GitHub Users", index=False)


if __name__ == "__main__":
    username = input("Enter a GitHub username: ")
    if not username:
        print("Failed to get username")
        exit(1)
    data = get_github_user_info(username)
    write_to_excel(data, "data/github_users.xlsx")