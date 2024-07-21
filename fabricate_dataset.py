import pandas as pd
import numpy as np
import random

num_rows = 100

product_names = [f'Product {i}' for i in range(1, num_rows + 1)]
product_prices = np.random.uniform(10.0, 100.0, num_rows).round(2)
total_sales = np.random.randint(1, 1000, num_rows)
cities = random.choices(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], k=num_rows)
ratings = np.random.uniform(1.0, 5.0, num_rows).round(1)
age_groups = random.choices(['18-25', '26-35', '36-45', '46-55', '56+'], k=num_rows)

data = {
    'Name': product_names,
    'Price': product_prices,
    'Total_Sale': total_sales,
    'City': cities,
    'Rating': ratings,
    'Age_Group': age_groups
}

df = pd.DataFrame(data)

output_file = 'fabricated_data.xlsx'
df.to_excel(output_file, index=False)

print(f'Data successfully written to {output_file}')