""" 
Q8.Plot a line chart of marks for 'Amit' across all subjects.a
"""
import pandas as pd
import matplotlib.pyplot as plt

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

    # Plot a line chart of marks for 'Amit' across all subjects.a

    # Filter Amit's row
    Amit_Data = df[df['Name'] == 'Amit'].iloc[0]

    # Extract subjects and his specific marks
    Subjects = ['Math', 'English', 'Science']
    Amit_Marks = [Amit_Data['Math'], Amit_Data['English'], Amit_Data['Science']]

    # Generate Line Chart
    plt.figure(figsize=(10,6))
    plt.plot(
        Subjects,
        Amit_Marks,
        marker ='o',
        linestyle= '-',
        color = "black"
    )

    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit's Marks across subjects")

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()