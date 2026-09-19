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
    page.title = "studyos | login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.TRANSPARENT
    page.padding = 0

    bg_path = Path(__file__).resolve().parents[2] / "images" / "bg-0.jpg"
    bg_src = str(bg_path)
    
    title = ft.Text(
        value="Good to see you again!", 
        size=40, 
        weight=ft.FontWeight.BOLD, 
        color=ft.Colors.BLUE_700
    )
    
    subtitle = ft.Text(
        value="Introduce your data to continue", 
        size=14, 
        color=ft.Colors.GREY_600
    )
    
    txt_user = ft.TextField(
        label="Username",
        hint_text="MyUsername",
        prefix_icon=ft.icons.Icons.PERSON_PIN,
        width=300
    )
    
    txt_password = ft.TextField(
        label="Password",
        prefix_icon=ft.icons.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=300
    )
    
    alert_msg = ft.Text(value="", color=ft.Colors.RED_600, size=12)

    def login_click(e):
        if not txt_user.value or not txt_password.value:
            alert_msg.value = "Please fill all the fields."
            alert_msg.color = ft.Colors.RED_600
        else:
            session.login(txt_user.value, txt_password.value)
            alert_msg.value = "Logging in..."
            alert_msg.color = ft.Colors.GREEN_700
        
        page.update()

    btn_next = ft.Button(
        content=ft.Row(
            controls=[
                ft.Text("Continue", weight=ft.FontWeight.BOLD),
                ft.Icon(ft.icons.Icons.ARROW_FORWARD, size=18)
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
        on_click=login_click
    )


    form_container = ft.Column(
        controls=[
            title,
            subtitle,
            ft.Container(height=10),
            txt_user,
            txt_password,
            alert_msg,
            ft.Container(height=15),
            btn_next
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
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
                content=form_container,
                alignment=ft.alignment.Alignment.CENTER,
                padding=ft.padding.Padding.all(30),
                expand=True,
            )
        ]
    )

    page.add(login_stack)

