import os
import pandas as pd

max_files = 2  # set the value here, 0 means it will be determined based on the number of rows in the input file
rows_chunk = 1000
file_extension = '.txt'
input_folder = 'Input'
output_folder = 'Output'
output_file_name = 'chunk'
placeholder_row_in_output = 'Y'

# Check if the input folder exists
if not os.path.exists(input_folder):
    print(f"Error: the folder '{input_folder}' does not exist.")
    exit()

# Get the list of all '.txt' files in the 'Input' folder
txt_files = [f for f in os.listdir(input_folder) if f.endswith(file_extension)]

# Read the first '.txt' file in the 'Input' folder using the '|' delimiter and skip the first row
df = pd.read_csv(os.path.join(input_folder, txt_files[0]), delimiter='|', skiprows=1, dtype=str)

if max_files == 0:
    # Determine the number of output files needed
    num_files = len(df) // rows_chunk + (len(df) % rows_chunk > 0)
else:
    # Use the provided value of `max_files` as the number of output files
    num_files = max_files
    
# Check if the Output folder exists, create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Delete all files in the 'Output' folder
for f in os.listdir(output_folder):
    os.remove(os.path.join(output_folder, f))

# Loop through the number of output files needed
for i in range(num_files):
    # Select the next `rows_chunk` rows of data
    df_part = df.iloc[i*rows_chunk:(i+1)*rows_chunk]
    
    # Write the selected data to a new CSV file
    df_part.to_csv(os.path.join(output_folder, f'{output_file_name}_{i}{file_extension}'), index=False, sep='|', header=True)

if placeholder_row_in_output.upper() == 'Y':
    # Loop through all the '.txt' files in the 'Output' folder
    for f in os.listdir(output_folder):
        if f.endswith(file_extension):
            # Open the file and insert "IgnoreRow" at the beginning
            with open(os.path.join(output_folder, f), 'r') as file:
                content = file.readlines()
            content.insert(0, 'PlaceholderRow\n')
            with open(os.path.join(output_folder, f), 'w') as file:
                file.writelines(content)
