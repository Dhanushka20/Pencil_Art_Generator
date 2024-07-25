import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from PIL import Image, ImageTk
import cv2
import numpy as np

def pencil_sketch(image_path):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Image not loaded correctly. Please check the path.")
        return None

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    return pencil_sketch_image

def open_file():
    global pencil_sketch_img, original_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        original_image_path = file_path
        pencil_sketch_img = pencil_sketch(file_path)
        if pencil_sketch_img is not None:
            display_image(pencil_sketch_img)

def display_image(img_array):
    new_window = Toplevel(root)
    new_window.title("Pencil Sketch Preview")
    img = Image.fromarray(img_array)
    img.thumbnail((500, 500))
    img_tk = ImageTk.PhotoImage(image=img)
    img_label = tk.Label(new_window, image=img_tk)
    img_label.image = img_tk
    img_label.pack()

def save_file():
    if pencil_sketch_img is not None:
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if output_path:
            cv2.imwrite(output_path, pencil_sketch_img)
            messagebox.showinfo("Success", f"Pencil sketch saved at {output_path}")
    else:
        messagebox.showerror("Error", "No image to save. Please generate a pencil sketch first.")

root = tk.Tk()
root.title("Pencil Sketch Generator")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Image convert to pencil sketch", font=("Arial", 14))
label.pack(pady=10)

open_button = tk.Button(frame, text="Open Image", command=open_file, font=("Arial", 12))
open_button.pack(pady=10)

save_button = tk.Button(frame, text="Save Image", command=save_file, font=("Arial", 12))
save_button.pack(pady=10)

pencil_sketch_img = None
original_image_path = None

root.mainloop()
