'''TODO: 
1)add user input chunk size 1,000 to 4,000 character range. 
2)add warning "Anything above 2,000 characters requires Discord Nitro"

'''
import tkinter as tk
from tkinter import scrolledtext

def chunk_text(text, chunk_size):
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def show_chunks():
    user_input = entry.get()
    chunk_size = 2000
    chunks = chunk_text(user_input, chunk_size)
    
    popup = tk.Toplevel(root)
    popup.title("Text Chunks")
    
    text_area = scrolledtext.ScrolledText(popup, wrap=tk.WORD, width=40, height=20)
    text_area.pack(fill=tk.BOTH, expand=True)
    
    for i, chunk in enumerate(chunks):
        formatted_chunk = chunk + '\n\n(new 2000 character chunk)\n\n' if i < len(chunks) - 1 else chunk
        text_area.insert(tk.END, formatted_chunk)

root = tk.Tk()
root.title("Text Chunk Separator")

label = tk.Label(root, text="Enter your text:")
label.pack()

entry = tk.Entry(root, width=40)
entry.pack()

button = tk.Button(root, text="Show Chunks", command=show_chunks)
button.pack()

root.mainloop()
