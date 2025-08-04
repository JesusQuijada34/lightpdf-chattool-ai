import os
import requests
import sys
import tkinter as tk
import customtkinter as ctk

# 💠 Configuración de API
API_URL = "https://api.lightpdf.com/v1/docx/create"
API_KEY = "wxegmp9r2xzm8knxq"  # ¡No olvides proteger esto!

# 💠 Carpeta de salida en Linux
DOWNLOAD_DIR = os.path.expanduser("~/PDFLightChat/")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# 💠 Función para crear PDF desde texto
def create_pdf(text, filename="presentacion.pdf"):
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        data = {
            "title": "Presentación Académica",
            "content": text
        }
        response = requests.post(API_URL, headers=headers, json=data)
        if response.ok and "file_url" in response.json():
            url = response.json()["file_url"]
            file_path = os.path.join(DOWNLOAD_DIR, filename)
            r = requests.get(url)
            with open(file_path, "wb") as f:
                f.write(r.content)
            return file_path
        else:
            return None
    except Exception as e:
        print(f"Hubo un error, detalles del error: {e}")

# 💠 GUI con customtkinter
def launch_gui():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("PDF Conversacional")
    app.geometry("500x400")

    def on_submit():
        user_text = entry.get("1.0", "end")
        file = create_pdf(user_text.strip())
        if file:
            status_label.configure(text=f"✅ PDF guardado en: {file}")
        else:
            status_label.configure(text="❌ Error al generar el PDF.")

    entry = ctk.CTkTextbox(app, width=460, height=200)
    entry.pack(pady=20)

    generate_btn = ctk.CTkButton(app, text="Generar PDF", command=on_submit)
    generate_btn.pack()

    status_label = ctk.CTkLabel(app, text="")
    status_label.pack(pady=10)

    app.mainloop()

# 💠 Terminal (ANSI)
def terminal_mode(user_text):
    print("\033[34m💬 Conversando...\033[0m")
    file = create_pdf(user_text)
    if file:
        print(f"\033[32m✅ PDF generado en: {file}\033[0m")
    else:
        print("\033[31m❌ Error al generar el PDF.\033[0m")

# 💠 Main entrypoint
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--chatpdf":
        user_input = " ".join(sys.argv[2:])
        terminal_mode(user_input)
    else:
        launch_gui()

