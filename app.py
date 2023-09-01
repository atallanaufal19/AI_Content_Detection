import tkinter as tk
import tkinter.font as tkFont
from model import Detector

class App:
    def __init__(self, root):
        root.title("Content Detection")
        width = 597
        height = 591
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GLabel_290 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=13)
        self.GLabel_290["font"] = ft
        self.GLabel_290["fg"] = "#333333"
        self.GLabel_290["justify"] = "center"
        self.GLabel_290["text"] = "AI Content Detection"
        self.GLabel_290["relief"] = "flat"
        self.GLabel_290.place(x=110, y=10, width=395, height=30)

        self.GLabel_520 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_520["font"] = ft
        self.GLabel_520["fg"] = "#333333"
        self.GLabel_520["justify"] = "center"
        self.GLabel_520["text"] = "Input text here:"
        self.GLabel_520.place(x=40, y=60, width=87, height=30)

        self.GLineEdit_162 = tk.Text(root, wrap="word")
        self.GLineEdit_162["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_162["font"] = ft
        self.GLineEdit_162["fg"] = "#333333"
        self.GLineEdit_162["wrap"] = "word"
        self.GLineEdit_162.place(x=40, y=90, width=519, height=203)

        self.GLabel_587 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_587["font"] = ft
        self.GLabel_587["fg"] = "#333333"
        self.GLabel_587["justify"] = "center"
        self.GLabel_587["text"] = "result:"
        self.GLabel_587.place(x=40, y=310, width=87, height=25)

        self.GText_590 = tk.Text(root, wrap="word")
        self.GText_590["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GText_590["font"] = ft
        self.GText_590["fg"] = "#333333"
        self.GText_590["wrap"] = "word"
        self.GText_590.place(x=40, y=340, width=519, height=207)

        self.GButton_602 = tk.Button(root)
        self.GButton_602["activebackground"] = "#90ee90"
        self.GButton_602["activeforeground"] = "#90ee90"
        self.GButton_602["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.GButton_602["font"] = ft
        self.GButton_602["fg"] = "#000000"
        self.GButton_602["justify"] = "center"
        self.GButton_602["text"] = "Detect"
        self.GButton_602.place(x=270, y=300, width=70, height=25)
        self.GButton_602["command"] = self.detect_button_pressed

    def detect_button_pressed(self):
        content = self.GLineEdit_162.get("1.0", tk.END)
        if len(content.strip()) >= 100:
            model = Detector()
            results, out = model(content)
            self.GText_590.delete("1.0", tk.END)

            # average perplexity per line
            avg_perplexity_per_line = results["Perplexity per line"]
            out_with_perplexity = f"{out}\nAverage Perplexity: {avg_perplexity_per_line:.2f}"
            self.GText_590.insert(tk.END, out_with_perplexity)
        else:
            self.GText_590.delete("1.0", tk.END)
            self.GText_590.insert(tk.END, "Please input more text (min 100 characters)")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()