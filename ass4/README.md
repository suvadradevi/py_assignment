# This folder contains two python programs:
# task(1):Reading a file and handling errors
- If file is present:
    1. A file named 'sample.txt' is created and it should be present in the same folder as that of the detecting python files.
    2. The reading of the file is mentioned in the try block.
    3. 'file_name' is the variable that open the file in read mode.
    4. 'reading' variable reads the file.
    5. The file is then displayed using 'reading' variable
    6. The file is closed using 'file_name' variable.
  -If file is not present:
    1. In case, the file is not found the FileNotFoundError arises
    2. This error needs to be handled and thus placed in except block.
    3. A message is printed in order to handle it.

---
# task(2) : Writting and appending in a file:
  1. A file named 'output.txt' is created in the same folder as that of the detecting python files.
  2. User imput to write in the file was stored in 'write_text' variable
  3.  User imput to append aditional text in the file was stored in 'append_text' variable
  4.  'file1' variable open the file in write mode.
  5.  'writing' variable writes the content of 'write_text' variable in the file
  6.  'appending' variable appends the content of 'append_text' variable in the file
  7.  'file1'variable open the file in read mode.
  8.  'reading' variable reads the file.
  9.  The file is then displayed using 'reading' variable
  10.  The file is closed using 'file1' variable.
