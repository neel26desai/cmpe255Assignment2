import tkinter as tk
from translator_model import TranslatorModel
from translator_view import TranslatorView
from translator_controller import TranslatorController

def main():
    root = tk.Tk()
    model = TranslatorModel()
    view = TranslatorView(root)
    view.create_view()
    controller = TranslatorController(model, view)
    root.title('Translator')

    tk.mainloop()
    

if __name__ == "__main__":
    main()
