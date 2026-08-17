""" 
Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.
"""
import pandas as pd

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

if __name__ == "__main__":
    main()