import pandas as pd
import math
pizza_files='data/pizzas.csv' 
pizza_data=pd.read_csv(pizza_files)
print(pizza_data)
pizza_data['Area'] = ((pizza_data['Size'] / 2) ** 2 * math.pi)
pizza_data['Price_Per_SqInch'] = (pizza_data['Price'] / pizza_data['Area'])
df = pd.DataFrame(pizza_data)
pizza_data_df = df.sort_values(by=['Price_Per_SqInch'], ascending=True)
print(pizza_data_df)
