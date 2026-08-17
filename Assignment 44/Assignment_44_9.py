""" 
Q.9:Create a DataFrame with missing values and fill them with column mean.
data2 = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [np.nan, 76, 88],
'Science': [91, np.nan, 85]
}
"""
import pandas as pd
import numpy as np

def main():
    Border="-"*50
    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82]
        }

    # Create Dataframe
    df = pd.DataFrame(data)
    print(Border)
    print(df)

    print(Border)   
    print("DataFrame Shape :", df.shape)
    print(Border)    

    print("DataFrame Columns :", df.columns.to_list())
    print(Border)

    print("Data Types :\n", df.dtypes)
    print(Border)

    # Print Descriptive Statistics
    print(df.describe())
    print(Border)

    # Calculate and add "Total" column to the Dataframe
    print("Total Columns Add:")
    df['Total'] = df['Math'] + df['Science'] + df['English']
    print(df)   
    print(Border)

    # Display Student Scoring more than 85 in Science
    Science_Score = df[df['Science'] > 85]
    print("Above 85 Marks obtained Students in science :\n",Science_Score)

    print(Border)
    # Replace 'Pooja' with 'Puja'
    df['Name'] = df['Name'].replace('Pooja', 'Puja')

    print("Replace Pooja Name with Puja :\n", df)

    print(Border)
    
    # Sort by 'Total' marks in descending order

    df_Sorted = df.sort_values(by = 'Total', ascending = False)
    print("Sort by 'Total' marks in descending order :\n", df_Sorted)
    print(Border)

  # Q9. Create a DataFrame with missing values
    data2 = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [np.nan, 76, 88],
        'Science' : [91, np.nan, 85]
        }

    # Create DataFrame
    df2 = pd.DataFrame(data2)

    # Fill missing values with column mean
    df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
    df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

    print("Filled Missing Values with Mean:\n", df2)
    print(Border)


if __name__ == "__main__":
    main()