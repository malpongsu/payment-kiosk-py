import customtkinter
from PIL import Image, ImageTk
import os
import tkinter as tk

class YourApp(customtkinter.CTk):
    def __init__(self):
        # ... (your other initialization code)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "dipcwdImage.png")), size=(26, 26))

        # Create a CTkLabel with the logo image
        self.logo_label = customtkinter.CTkLabel(self, image=self.logo_image)
        self.logo_label.grid(row=0, column=0)

        # Counter for the click events
        self.click_count = 0

        # Bind click event to the logo image
        self.logo_label.bind("<Button-1>", self.logo_click_handler)

    def logo_click_handler(self, event):
        # Increment click count
        self.click_count += 1

        # Check if the click count is 5
        if self.click_count == 5:
            # Exit the application
            self.exit_application()

    def exit_application(self):
        # Your cleanup code here
        # ...

        # Exit the application
        self.master.destroy()

if __name__ == "__main__":
    app = YourApp()
    app.mainloop()
