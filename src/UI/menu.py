import os
import sys
import flet as ft

from UI.account import main as account_main

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if src_path not in sys.path:
    sys.path.append(src_path)

from core import session
from core.image_utils import get_image_src
from main import main as app_main

USERNAME, TOKEN = "", ""

def main(page: ft.Page):
    page.clean()
    page.title = "StudyOS | register"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.TRANSPARENT
    page.padding = 0

    bg_src = get_image_src("bg-0.jpg")
    
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

    text = ft.Column(
        controls=[
            title,
            subtitle
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    def goto_account(e):
        account_main(page)

    go_account = ft.Button(
        content=ft.Row(
            [
                ft.Text("My Account", weight=ft.FontWeight.BOLD),
                ft.Icon(ft.icons.Icons.EDIT, size=18)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        width=300,
        height=45,
        elevation=2,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
        on_click=goto_account
    )

    background_image = ft.Image(
        src=bg_src,
        fit=ft.BoxFit.COVER,
        width=page.width,
        height=page.height,
        expand=True,
    )

    login_stack = ft.Stack(
        expand=True,
        controls=[
            background_image,
            ft.Container(
                content=ft.Column(controls=[text, go_account]),
                alignment=ft.alignment.Alignment.CENTER,
                padding=ft.padding.Padding.all(30),
                expand=True,
            ),
        ],
    )


    page.add(login_stack)
