import json
import requests
from googletrans import Translator
from PIL import Image
import pytesseract
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import speech_recognition as sr
from pydub import AudioSegment

class Assistant:
    def __init__(self):
        self.translator = Translator()
        self.recognizer = sr.Recognizer()

    def translate_from_json(self, json_file, target_language='es'):
       
        try:
            #Load the JSON file
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            #Save the translated data in a dictionary
            translated_data = {}
            #Translate each key-value pair in the JSON file
            for key, value in data.items():
                translated_value = self.translator.translate(value, dest=target_language).text
                translated_data[key] = translated_value
            
            return translated_data
        except Exception as e:
            return f"An error occurred: {e}"

    def download_image(self, image_url, save_path):
       
        try:
            # Send an HTTP request to the image URL
            response = requests.get(image_url)
            response.raise_for_status()

            # Save the image to the specified file path
            with open(save_path, 'wb') as file:
                file.write(response.content)

            print(f"Image successfully downloaded and saved to {save_path}")
        except Exception as e:
            print(f"An error occurred while downloading the image: {e}")

    def solve_math_from_image(self, image_path):
      
        try:
            # Open the image using Pillow
            image = Image.open(image_path)
            
            # Use pytesseract to extract text from the image
            math_text = pytesseract.image_to_string(image, config='--psm 6')
            print(f"Extracted Math Problem: {math_text}")
            
            # Eliminar el signo "=" al final
            if math_text.endswith('\n'):
                math_text = math_text[:-1]
            if math_text.endswith('='):
                math_text = math_text[:-1]

            # Parse and solve the math problem using sympy
            math_expr = parse_expr(math_text)
            solution = sp.simplify(math_expr)
            
            return f"Solution: {solution}"
        except Exception as e:
            return f"An error occurred while solving the math problem: {e}"

    def transcribe_audio(self, audio_path):
    
        try:
            # Convert MP3 to WAV if necessary
            if audio_path.endswith('.mp3'):
                audio = AudioSegment.from_mp3(audio_path)
                audio_path = audio_path.replace('.mp3', '.wav')
                audio.export(audio_path, format='wav')
            
            # Use SpeechRecognition to transcribe the audio
            with sr.AudioFile(audio_path) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data)
            
            return f"Transcribed Text: {text}"
        except Exception as e:
            return f"An error occurred while transcribing the audio: {e}"

assistant = Assistant()     

def show_menu():
    print("\n--- How can I help you? ---")
    print("1. Translate from a json file")
    print("2. Download an image from a URL")
    print("3. Solve a math problem from an image")
    print("4. Transcribe an audio file")
    print("5. Exit")
    

def main():
    while True:
        show_menu()
        choice=input("Enter your choice: ")

        if choice == "1":            
            json_file = input("Enter the JSON file path: ")
            target_language = input("Enter the target language (e.g., es): ")
            translated_text = assistant.translate_from_json(json_file, target_language)
            print("Translated Text:", translated_text)

        elif choice == "2":
            image_url = input("Enter the image URL: ")
            save_path = input("Enter the save path: ")
            assistant.download_image(image_url, save_path)

        elif choice == "3":
            image_path = input("Enter the image path: ")
            solution = assistant.solve_math_from_image(image_path)
            print(solution)

        elif choice == "4":
            audio_path = input("Enter the audio path: ")
            transcription = assistant.transcribe_audio(audio_path)
            print(transcription)
            
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Write the number from the options.")


if __name__ == "__main__":
    main()
