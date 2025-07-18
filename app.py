import customtkinter as ctk
from utils.timer import PomodoroTimer
from utils import audio

# === Theme Configuration ===
ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("green")  # We'll override button colors manually for neon effect

class LofiFocusApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoFi Focus App")
        self.geometry("420x500")
        self.configure(padx=20, pady=20)

        # Neon colors
        self.accent_color = "#39FF14"  # Neon green
        self.accent_hover = "#00FF00"
        self.font_family = ("Segoe UI", 12, "bold")

        self.timer = PomodoroTimer()

        self.timer_label = ctk.CTkLabel(self, text=self.timer.get_time(), font=("Segoe UI", 48, "bold"))
        self.timer_label.pack(pady=(10, 20))

        self.track_label = ctk.CTkLabel(self, text="", font=("Segoe UI", 14), text_color="gray")
        self.track_label.pack(pady=(0, 10))

        self.dropdown = ctk.CTkOptionMenu(
            self,
            values=audio.get_lofi_streams(),
            command=self.change_stream,
            width=250,
            font=("Segoe UI", 12),
            dropdown_font=("Segoe UI", 12),
        )
        self.dropdown.set("LoFi Girl")
        self.dropdown.pack(pady=10)

        # Button shared styling
        button_kwargs = {
            "width": 200,
            "corner_radius": 10,
            "fg_color": self.accent_color,
            "hover_color": self.accent_hover,
            "text_color": "black",
            "font": self.font_family
        }

        # Buttons layout inside a frame
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)

        self.start_work_button = ctk.CTkButton(button_frame, text="Start Focus", command=self.start_work, **button_kwargs)
        self.start_work_button.pack(pady=5)

        self.start_break_button = ctk.CTkButton(button_frame, text="Start Break", command=self.start_break, **button_kwargs)
        self.start_break_button.pack(pady=5)

        self.stop_timer_button = ctk.CTkButton(button_frame, text="Stop Timer", command=self.stop_timer, **button_kwargs)
        self.stop_timer_button.pack(pady=5)

        self.stop_music_button = ctk.CTkButton(button_frame, text="Stop Music", command=audio.stop_stream, **button_kwargs)
        self.stop_music_button.pack(pady=5)

        # Theme switch (Dark / Light)
        self.theme_switch = ctk.CTkSwitch(
            self,
            text="Dark Mode",
            command=self.toggle_theme,
            onvalue="Dark",
            offvalue="Light"
        )
        self.theme_switch.select()  # Default to dark mode
        self.theme_switch.pack(pady=5)

        self.is_dark_mode = True

        self.is_dark_mode = True  # Start in dark mode

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Auto-start default LoFi stream
        self.change_stream("LoFi Girl")
        self.update_track_label()

    def start_work(self):
        self.timer.start()
        self.update_timer()

    def start_break(self):
        self.timer.start_break()
        self.update_timer()

    def stop_timer(self):
        self.timer.stop()
        self.timer_label.configure(text=self.timer.get_time())

    def update_timer(self):
        if self.timer.is_running:
            self.timer.tick()
            self.timer_label.configure(text=self.timer.get_time())
            if self.timer.remaining_seconds > 0:
                self.after(1000, self.update_timer)
            else:
                if self.timer.is_break:
                    self.timer_label.configure(text="Break over!")
                else:
                    self.timer_label.configure(text="Focus session over!")
                self.timer.stop()

    def change_stream(self, name):
        audio.play_stream(name)
        self.update_track_label()

    def update_track_label(self):
        self.track_label.configure(text=f"Now Playing: {audio.get_current_track()}")

    def toggle_theme(self):
        if self.theme_switch.get() == "Light":
            ctk.set_appearance_mode("Light")
            self.is_dark_mode = False
            self.theme_switch.configure(text="Light Mode")
        else:
            ctk.set_appearance_mode("Dark")
            self.is_dark_mode = True
            self.theme_switch.configure(text="Dark Mode")

    def on_close(self):
        audio.cleanup()
        self.destroy()

if __name__ == "__main__":
    app = LofiFocusApp()
    app.mainloop()
