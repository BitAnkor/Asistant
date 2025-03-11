# Assistant

This Python file defines a simple assistant program that can perform various tasks using different libraries. The Assistant class includes methods to:

  1- Translate text from a JSON file to a specified target language using the googletrans library.

  2- Download an image from a given URL and save it to a specified path using the requests library.

  3- Solve a math problem extracted from an image using the pytesseract library for text extraction and sympy for solving the math expression.

  4- Transcribe audio from a file (converting MP3 to WAV if necessary) using the speech_recognition library.

The program presents a menu to the user to choose which task to perform, and it continues to run until the user chooses to exit. The main functionality is encapsulated in the main() function, which handles user input and calls the appropriate methods from the Assistant class.
