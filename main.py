import tkinter as tk

class Companion:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Companion")
        self.master.geometry("200x200")
        self.master.overrideredirect(True)
        self.master.wm_attributes("-topmost", True)
        self.master.wm_attributes("-transparentcolor", "white")

        self.canvas = tk.Canvas(self.master, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.canvas, text="🤖", font=("Arial", 50), bg="white")
        self.label.pack(pady=50)

        self.master.bind("<B1-Motion>", self.move)
        self.master.bind("<Button-3>", self.quit)

    def move(self, event):
        x, y = self.master.winfo_pointerxy()
        self.master.geometry(f"+{x-100}+{y-100}")

    def quit(self, event):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Companion(root)
    root.mainloop()
