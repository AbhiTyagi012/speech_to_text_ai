import flet as ft
from whisper_ui.whisper_app import WhisperApp


def main(page: ft.Page):
    page.title="Developed by Austere Systems Pvt Ltd"
    app = WhisperApp(page)
    page.add(app)
    
ft.app(target=main)


