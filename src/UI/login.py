import os
import sys
from pathlib import Path
import flet as ft

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if src_path not in sys.path:
    sys.path.append(src_path)

from core import session
from core.image_utils import get_image_src

def main(page: ft.Page, on_success=None):
    page.clean()
    page.title = "studyos | login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.TRANSPARENT
    page.padding = 0

    bg_src = get_image_src("bg-0.jpg")

    title = ft.Text(
        "Good to see you again!",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700
    )

    subtitle = ft.Text(
        value="Fill out the fields below to log in",
        size=14,
        color=ft.Colors.GREY_600
    )

    txt_user = ft.TextField(
        label="Username",
        hint_text="awkwardDuck1704",
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

    alert_msg = ft.Text(
        value="", 
        color=ft.Colors.RED_600, 
        size=12
    )

    # returns true if the length of the given field is over eight characters and returns false otherwise.
    def verify_length(f: str) -> bool:
        return len(f) > 8


    # changes the alert_msg element's value to the given message.
    # displays the given message in red text.
    def alert(message):
        alert_msg.value = message
        alert_msg.color = ft.Colors.RED_600 # is this even needed if the elements color is this by default?
        page.update()

    def login_click(e):
        stripped_user = txt_user.value.strip()
        stripped_password = txt_password.value.strip()

        if not stripped_user:
            alert("Please fill in the username field.")
            return None

        if not stripped_password:
            alert("Please fill in the password field.")
            return None

        if not verify_length(stripped_user):
            alert("")
            return None

        if not verify_length(stripped_password):
            alert("Your password must be at least eight characters.")
            return None

        alert_msg.value = "Logging in..."
        alert_msg.color = ft.Colors.BLUE_700
        page.update()

        result = session.login(stripped_user, stripped_password)

        if isinstance(result, tuple) and len(result) >= 2 and result[0] and result[1]:
            alert_msg.value = "Logged in!"
            alert_msg.color = ft.Colors.GREEN_700
            page.update()
            if on_success is not None:
                on_success(result)
            return result

        alert("Invalid username or password.")
        return result

    btn_next = ft.Button(
        content=ft.Row(
            [
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
        [
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
        [
            background_image,
            ft.Container(
                content=form_container,
                alignment=ft.alignment.Alignment.CENTER,
                padding=ft.padding.Padding.all(30),
                expand=True,
            )
        ],
        expand=True,
    )

    page.add(login_stack)
    return None

