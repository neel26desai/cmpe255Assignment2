import tkinter as tk

class TranslatorView:
    def __init__(self, root):
        self.root = root
        self.input_text_box = tk.Text(root, height=10, width=50)
        self.output_text_box = tk.Text(root, height=10, width=50, state='disabled')
        #add a button to the bottom right corner of the window
        self.translate_button = tk.Button(root, text='Translate')
        #create a drop down menu with 2 options french and spanish
        self.language_options = tk.StringVar(root)
       

    def create_view(self):
        #add the input text box to the top of the window
        self.input_text_box.grid(row=0, column=0, padx=10, pady=10)
        #add the output text box to the bottom of the window
        self.output_text_box.grid(row=1, column=0, padx=10, pady=10)
        #add the translate button to the bottom right corner of the window
        self.translate_button.grid(row=2, column=0, sticky='e', padx=10, pady=10)
        #add the drop down menu to the bottom left corner of the window
        self.language_options.set('French')
        self.language_menu = tk.OptionMenu(self.root, self.language_options, 'French', 'Spanish')
        self.language_menu.grid(row=2, column=0, sticky='w', padx=10, pady=10)

    def get_input_text(self):
        return self.input_text_box.get("1.0", 'end-1c')

    def set_output_text(self, text):
        self.output_text_box.config(state='normal')
        self.output_text_box.delete("1.0", tk.END)
        self.output_text_box.insert(tk.END, text)
        self.output_text_box.config(state='disabled')
    
    #create a method to set the values for the drop down menu
    def set_language_options(self, options=['French', 'Spanish']):
        self.language_options.set(options)
    

    