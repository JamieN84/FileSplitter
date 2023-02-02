# Splitting a Text File into Multiple Files #
This script will split a large text file into multiple smaller files, each containing a specified number of rows. The input and output folders, output file name, file extension, and the number of rows per output file are all configurable. The script will also add a placeholder row at the beginning of each output file if specified.

## Requirements ##
Python 3.x
Pandas

## Usage ##
1. Place the large text file(s) to be split in the Input folder.
2. Configure the following variables at the top of the script:
    * max_files: The maximum number of output files. Set this to 0 if the number of files should be determined based on the number of rows in the input file.
    * rows_chunk: The number of rows per output file.
    * file_extension: The file extension of the input and output files (e.g. '.txt').
    * input_folder: The name of the folder containing the input file(s).
    * output_folder: The name of the folder where the output files will be written.
    * output_file_name: The name of the output files (e.g. 'chunk').
    * placeholder_row_in_output: Whether to add a placeholder row to each output file (e.g. 'Y' or 'N').
3. Run the script. The output files will be written to the Output folder.

## Limitations ##
The script only processes the first file in the Input folder with the specified file extension.
The script assumes the input file uses the '|' character as a delimiter and skips the first row.

## Example ##
For example, if max_files is set to 2, rows_chunk is set to 1000, and the input file has 2000 rows, the script will generate two output files: chunk_0.txt and chunk_1.txt each with 1000 rows of data from the input file.