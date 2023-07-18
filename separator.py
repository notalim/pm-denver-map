import pandas as pd

df = pd.read_csv('data.csv')

rows = []  # to store individual rows

# iterating over each row of the dataframe
for idx, row in df.iterrows():
    # splitting the neighborhood column by "|"
    neighborhoods = str(row["Neighborhood"]).split("|")
    for n in neighborhoods:
        # copying the row and replacing the neighborhood with a single neighborhood
        new_row = row.copy()
        new_row["Neighborhood"] = n
        # appending the new row to the list
        rows.append(new_row)

# converting the list of rows to a dataframe
new_df = pd.DataFrame(rows)

# resetting the index of the new dataframe
new_df = new_df.reset_index(drop=True)

# writing the new dataframe to csv
new_df.to_csv("new_data.csv", index=False)
