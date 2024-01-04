import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        # ... other code ...

        # Dark mode toggle button
        self.dark_mode_var = ctk.BooleanVar()
        self.dark_mode_var.set(False)  # Initial state: Light mode
        self.dark_mode_button = ctk.CTkButton(self.navigation_frame, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.grid(row=7, column=0, padx=20, pady=20, sticky="s")

        # Appearance mode menu
        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def toggle_dark_mode(self):
        current_mode = "Dark" if self.dark_mode_var.get() else "Light"
        self.set_appearance_mode(current_mode)

    def change_appearance_mode_event(self, mode):
        # Handle appearance mode changes here, if needed
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
