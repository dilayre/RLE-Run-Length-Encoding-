<h1> # Run-Length Encoding (RLE) Program </h1>

This is a simple Python project that uses the Run-Length Encoding method.
RLE is a basic way to make text shorter. It counts how many times the same character repeats and writes the character with the number.

Example:

```
AAABBCC → A3B2C2
```

<h2> ## What this program does </h2>

* It looks at all `.txt` files in the same folder.
* It shows these files in a small menu.
* You choose a file by typing a number (1, 2, 3…).
* The program reads the file and compresses the text with RLE.
* It creates a new file with the name:

  ```
  originalname_compressed.txt
  ```

<h2> ## How it works (simple steps) </h2>

1. The program finds all `.txt` files.
2. It prints a list for the user.
3. User chooses a file number.
4. The file is opened and read.
5. The text is compressed with the RLE function.
6. The compressed text is saved to a new file.
7. A message shows that the compression is done.

<h2> ## How to run </h2>

Put your `.txt` files in the same folder and run:

```
python compress.py
```

Then choose a number from the menu.
