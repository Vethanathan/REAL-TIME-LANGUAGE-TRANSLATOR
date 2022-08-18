import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1000x100")
app.title("App")

frame1 = customtkinter.CTkFrame()
frame1.grid()


app_name = customtkinter.CTkLabel(text = "WELCCOME", master=frame1, justify=tkinter.LEFT)

app_name.grid(row=0,column=0)

app.mainloop()