import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import csv_reader
from openai import OpenAI

client = OpenAI(api_key='KEY')


class PokemonAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Data Analyzer")

        # Combobox for selecting the stat
        ttk.Label(root, text="Select the stat:").pack(pady=10)
        self.attribute_combobox = ttk.Combobox(root,
                                               values=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
        self.attribute_combobox.pack(pady=10)
        self.attribute_combobox.set('HP')  # Set a default value

        # Entry widget for entering the ChatGPT prompt
        ttk.Label(root, text="Enter ChatGPT Prompt:").pack(pady=10)
        self.prompt_entry = ttk.Entry(root)
        self.prompt_entry.pack(pady=10)

        # Button to trigger the create_pokemon_list function
        ttk.Button(root, text="Generate Pokemon List", command=self.generate_pokemon_list).pack(pady=10)

        # Text widget to display ChatGPT response
        ttk.Label(root, text="ChatGPT Response:").pack(pady=10)
        self.response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.response_text.pack(pady=10)

    def generate_chatgpt_response(self, prompt):
        response = client.completions.create(model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=1024)
        return response.choices[0].text.strip()

    def generate_pokemon_list(self):
        attribute = self.attribute_combobox.get()
        csv_reader.create_pokemon_list(attribute)

        # Get the ChatGPT prompt from the entry widget
        prompt = self.prompt_entry.get()

        # Example ChatGPT interaction
        # file_path = '../results/sorted_pokemon_data.txt'  # Update the file path as needed
        # with open(file_path, 'r') as file:
            # file_content = file.read()
        # prompt = f"Can you tell me the first five items listed in :\n{file_content}\n"
        chatgpt_response = self.generate_chatgpt_response(prompt)
        self.response_text.delete(1.0, tk.END)  # Clear previous text
        self.response_text.insert(tk.END, chatgpt_response)

# Define a function to interact with ChatGPT
# def generate_chatgpt_response(prompt):
#     Replace with your OpenAI API key
    # response = client.completions.create(model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=1024)
    # return response.choices[0].text


#def main():
    # print("Hello World!")
    # attribute = input("Enter the type: ")
    # csv_reader.create_pokemon_list(attribute)
    # Example ChatGPT interaction
    # prompt = f"Can you tell me anything interesting about the list of Pokemon in descending order of {attribute}."
    # chatgpt_response = generate_chatgpt_response(prompt)
    # print(chatgpt_response)


if __name__ == "__main__":
    # main()
    root = tk.Tk()
    app = PokemonAnalyzerGUI(root)
    root.mainloop()
