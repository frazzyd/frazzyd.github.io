import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image
import re

# Initialize the main application window
class ImageRenamerApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Image Renamer")
        self.geometry("500x400")
        
        # Define UI elements
        self.label = tk.Label(self, text="Drag and drop images here", font=("Arial", 14))
        self.label.pack(pady=20)
        
        self.file_list = []
        
        self.name_scheme_label = tk.Label(self, text="Enter Naming Scheme (use {num} for numbering):")
        self.name_scheme_label.pack(pady=10)
        
        self.name_scheme_entry = tk.Entry(self, width=40)
        self.name_scheme_entry.pack(pady=5)
        
        self.output_folder_btn = tk.Button(self, text="Select Output Folder", command=self.select_output_folder)
        self.output_folder_btn.pack(pady=10)
        
        self.rename_button = tk.Button(self, text="Rename and Save Images", command=self.rename_images)
        self.rename_button.pack(pady=20)
        
        self.output_folder = None
        
        # Enable drag and drop
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.add_files)
    
    def add_files(self, event):
        files = self.tk.splitlist(event.data)
        for file in files:
            if re.match(r'.*\.(jpg|jpeg|png|gif|bmp|tiff)$', file, re.IGNORECASE):
                self.file_list.append(file)
            else:
                messagebox.showerror("Error", f"{file} is not a valid image file.")
        
        messagebox.showinfo("Files Added", f"{len(self.file_list)} images added.")
        
    def select_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder = folder
            messagebox.showinfo("Output Folder", f"Selected folder: {self.output_folder}")
    
    def rename_images(self):
        if not self.file_list:
            messagebox.showerror("Error", "No images to rename. Please add images first.")
            return
        
        if not self.output_folder:
            messagebox.showerror("Error", "No output folder selected. Please select an output folder.")
            return
        
        naming_scheme = self.name_scheme_entry.get()
        if "{num}" not in naming_scheme:
            messagebox.showerror("Error", "Naming scheme must include '{num}' to indicate numbering.")
            return
        
        for i, file in enumerate(self.file_list, start=1):
            try:
                # Set new filename based on naming scheme, with no zero-padding
                new_name = naming_scheme.replace("{num}", str(i))
                ext = os.path.splitext(file)[1]
                new_file_path = os.path.join(self.output_folder, new_name + ext)
                
                # Open and save image with new name
                image = Image.open(file)
                image.save(new_file_path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to rename {file}: {e}")
        
        messagebox.showinfo("Success", f"Renamed and saved {len(self.file_list)} images.")
        self.file_list.clear()

# Run the app
if __name__ == "__main__":
    app = ImageRenamerApp()
    app.mainloop()