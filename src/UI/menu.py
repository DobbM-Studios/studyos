import os
import sys
from pathlib import Path
import flet as ft

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if src_path not in sys.path:
    sys.path.append(src_path)

from core import session

def main(page: ft.Page):
    page.clean()
    page.title = "studyos | register"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.TRANSPARENT
    page.padding = 0

    bg_path = Path(__file__).resolve().parents[2] / "images" / "bg-1.jpg"
    bg_src = str(bg_path)
    
    title = ft.Text(
        value="Menu Coming Soon", 
        size=40, 
        weight=ft.FontWeight.BOLD, 
        color=ft.Colors.BLUE_700
    )
    
    subtitle = ft.Text(
        value="Want to collaborate? Open a PR!", 
        size=14, 
        color=ft.Colors.GREY_600
    )

    background_image = ft.Image(
        src=bg_src,
        fit=ft.BoxFit.COVER,
        width=page.width,
        height=page.height,
        expand=True,
    )

    text = ft.Column(
        controls=[
            title,
            subtitle,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    login_stack = ft.Stack(
        expand=True,
        controls=[
            background_image,
            ft.Container(
                content=text,
                alignment=ft.alignment.Alignment.CENTER,
                padding=ft.padding.Padding.all(30),
                expand=True,
            )
        ],

    )

    page.add(login_stack)

