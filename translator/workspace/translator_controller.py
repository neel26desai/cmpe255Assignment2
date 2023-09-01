class TranslatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.root.bind('<Return>', self.translate_text)
        self.view.root.bind('<Control-z>', self.undo_translation)
        #bind the button to the translate_text method
        self.view.translate_button.bind('<Button-1>', self.translate_text)
        

    def translate_text(self, event):
        input_text = self.view.get_input_text()
        #read drop down menu value
        language = self.view.language_options.get()
        #pass the language parameter to the translate_text method
        translated_text = self.model.translate_text(input_text, language)
        self.view.set_output_text(translated_text)

    def undo_translation(self, event):
        self.view.set_output_text('')

    
