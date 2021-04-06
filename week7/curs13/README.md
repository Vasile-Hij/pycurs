FILE HANDLING
--

Python is opening files with `open()` function.

Assign a variable to open the file with relative address as default input : `f = open("your_file.txt")`.

`"r"` - read - Default value. Opens a file for reading, error if the file does not exist;

`"a"` - append - Opens a file for appending, creates the file if it does not exist;

`"w"` - write - Opens a file for writing, creates the file if it does not exist;

`"x"` - create - Creates the specified file, returns an error if the file exists.

E.g.

`f = open("your_file.txt", 'r')` - read only;

`f = open("your_file.txt", "a")` - writing existing file at the end of the file;

`f = open("your_file.txt", "w")` - write a file. If file is written already, this method will overwrite;

`f = open("your_file.txt", "x")` - create a new file, but return error if file exists.

Returning one line by using `realine()`.

Closing the file with `close()`.

To delete a file. it's necessary to import OS module:
`os.remove("your_file.txt")`.

Avoiding an error it means to check if the file exists
with:
```py
import os 
os.remove('demofile.txt') if os.path.exists('demofile.txt') else print('File is not found')
```