import customtkinter as ctk
from tkinter import messagebox
from tkinter import Tk
from PIL import Image, ImageTk

# Setting up theme of your app
ctk.set_appearance_mode("system")

# Create root window
root = ctk.CTk() 
root.resizable(True, True)
root.title("Dipolog City Water District")
root.geometry("750x500")

# Adding Icon Logo
root.iconbitmap("images/dipcwdImage.ico")

# Adding Header Logo

# Background Image
image_bg = ImageTk.PhotoImage(file="images/header_pic2.png") 

label_bg = ctk.CTkLabel(
    root,
    image=image_bg,
    height=100,
    width=225)
label_bg.pack()

frame = ctk.CTkFrame(
    master=label_bg,
    width=600, 
    height=450)
frame.place(relx=0.5,
    		rely=0.5,
            anchor=ctk.CENTER)	

label_text = ctk.CTkLabel(
    master= frame, 
    text='DIPOLOG CITY WATER DISTRICT KIOSK SYSTEM',
    font=('Century Gothic', 25, "bold"),
    text_color='#000',
    fg_color='skyblue',
    corner_radius=5)
label_text.place(x=25, y=45)



button_input_acc = ctk.CTkButton(
    master= frame, 
    text='Input Account Number', 
    fg_color='skyblue', 
    text_color='#000',
    hover_color='#6666FF')
button_input_acc.place(x=210, y=125)

button_tap_rfid = ctk.CTkButton(
    master= frame, 
    text='Tap Radio-Frequency Identification (RFID)', 
    fg_color='skyblue', 
    text_color='#000',
    hover_color='#6666FF')
button_tap_rfid.place(x=160, y=200)

root.mainloop()
