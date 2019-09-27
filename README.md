# csv-Combiner

# Requirements
 1. Set up a project folder.
 2. Create a wordpad document named Master.CSV inside the folder.
 3. Create a sub folder named "ImportData"
 4. Download CSV_combiner.py and put it in the project folder.

# Prepare Master.CSV File
 1. Open Master.CSV
 2. Delete all data
 3. Add header row with names for columns (The combiner script will not copy over column headers.)
 4. Add final header row of FileName
        Example: If your files contain 3 columns with names "Log", "Time" and "Test, then your Master.CSV file should read as follows:             Log,Time,Test,FileName

Move Import Data into Folder
	1. Put all files to be combined into ImportData folder
	2. Make sure each file is uniquely named
	3. This script is intended to be used with files that have the same number of columns in each file

Run CSV_combiner.py

All files should now be migrated into the Master.CSV file. Move, rename, enjoy!
