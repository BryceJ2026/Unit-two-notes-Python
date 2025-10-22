import numpy as np
import pandas as pd

# Series object is a 1D arra of indexed data
# Like a COLUMN (one category)
month = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
print(month)
# Series have attributes
print(month.values) # looks like a list
print(month.index) # shows the range of nums

# You can set the index explicitly!!!
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
better_month = pd.Series(month_list, index=[1,2,3,4,5,6,7,8,9,10,11,12])

print(f'My birthday is in {better_month[1]}')


# Can also think of Series like a simple dictionary with key:value pairs
birth_months = {'Kevin':'Mar',
                'Jackson':'Aug',
                'Finny':'Jul',
                'Bryce':'Nov',
                'Natalie':'Mar',
                'Paige':'Feb',
                'Maia':'Apr',}
birth_series = pd.Series(birth_months)
print(birth_series)

# Create a DataFrame from a dictionary
df = pd.DataFrame(birth_series, columns= ['Birth Month'])
print(df) #DataFrame objects have column headers

#Create a DataFrame from dictionaries
# Load tabular datat from a CSV file into a DataFrame
pokemon_df = pd.read_csv('pokemon_data.csv')
print(pokemon_df) # [800 rows x 12 cols]
print(pokemon_df.columns)# display col headers

#Column headers can be used to access individual columns
print(pokemon_df['Name'])
#Shortcut using DOT OPERATOR notation
print(pokemon_df.HP)
#Shortcut doees not work for all column names...
print(pokemon_df['Type 1'])

# Add a new column
#Fill values with a calculation
pokemon_df['Attack Ratio'] = pokemon_df['Attack'] / pokemon_df['Sp. Atk']

print(pokemon_df.head(10)) # show first n rows
print(pokemon_df.sample(3)) #show random sample of n rows
print( pokemon_df.shape ) # (rows, cols)
print( pokemon_df. columns) # returns a list of column headers
print( pokemon_df.info() ) # shows non-null count and dtypes
print( pokemon_df.describe() ) # mean, std, min, max
print( pokemon_df['Defense'].describe())# stats for specific col
print( pokemon_df['Type 1'].value_counts() ) #frequency of value counts


#How to locate specific rows
print( pokemon_df.loc[4] ) # gives charmander

#groupby function helps you isolate groups of entries
print ( pokemon_df.groupby('Type 1')[ ['HP', 'Speed']].mean())
print ( pokemon_df.groupby('Type 1').size().sort_values(ascending=False))