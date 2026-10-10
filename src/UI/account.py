import json
import os
import sys
import flet as ft

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if src_path not in sys.path:
    sys.path.append(src_path)

from core import session
from core.image_utils import get_image_src
from main import main as app_main

USERNAME, TOKEN = "", ""

def main(page: ft.Page):
    page.clean()
    page.title = "StudyOS | account"
    bg_src = get_image_src("bg-0.jpg")

    background_image = ft.Image(
        src=bg_src,
        fit=ft.BoxFit.COVER,
        width=page.width,
        height=page.height,
        expand=True,
    )

    title = ft.Text(
        value="Manage Your Account", 
        size=40, 
        weight=ft.FontWeight.BOLD, 
        color=ft.Colors.BLUE_700
    )

    def logout_click(_e):
        session.logout(USERNAME, TOKEN)
        app_main(page)

    def goto_menu(e):
        from UI.menu import main as menu_main

        menu_main(page)

    logout = ft.Button(
        content="Logout",
        color=ft.Colors.RED,
        on_click=logout_click,
        width=300,
        height=45,
        elevation=2,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )

    old_input = ft.TextField(
        label="Old password",
        prefix_icon=ft.icons.Icons.ARROW_BACK,
        password=True,
        can_reveal_password=True,
        width=300
    )

    new_input = ft.TextField(
        label="New password",
        prefix_icon=ft.icons.Icons.ARROW_FORWARD,
        password=True,
        can_reveal_password=True,
        width=300
    )

    btn_cancel = ft.Button(
        content=ft.Row(
            [
                ft.Text("Go Back", weight=ft.FontWeight.BOLD),
                ft.Icon(ft.icons.Icons.ARROW_BACK, size=18)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        width=300,
        height=45,
        elevation=2,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            color=ft.Colors.RED_600
        ),
        on_click=goto_menu
    )

    change_password_status = ft.Text(value="", size=12)

    def change_pw(_e):
        global TOKEN

        old_password = (old_input.value or "").strip()
        new_password = (new_input.value or "").strip()

        if not old_password or not new_password:
            change_password_status.value = "Enter both your old and new passwords."
            change_password_status.color = ft.Colors.RED_600
            page.update()
            return

        if len(new_password) <= 8:
            change_password_status.value = "New password must be at least 9 characters."
            change_password_status.color = ft.Colors.RED_600
            page.update()
            return

        status_code, response = session.change_password(
            USERNAME, old_password, new_password, TOKEN
        )

        if 200 <= status_code < 300:
            try:
                new_token = json.loads(response).get("token")
            except (json.JSONDecodeError, AttributeError):
                new_token = None

            if new_token:
                TOKEN = new_token
                change_password_status.value = "Password changed successfully."
                change_password_status.color = ft.Colors.GREEN_700
                old_input.value = ""
                new_input.value = ""
            else:
                TOKEN = ""
                change_password_status.value = (
                    "Password changed, but the session could not be refreshed. "
                    "Please log in again."
                )
                change_password_status.color = ft.Colors.RED_600
        else:
            change_password_status.value = (
                f"Could not change password (HTTP {status_code})."
            )
            change_password_status.color = ft.Colors.RED_600

        page.update()

    change_password = ft.Button(
        content="Change Password",
        color=ft.Colors.GREEN,
        on_click=change_pw,
        width=300,
        height=45,
        elevation=2,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )

    account = ft.Column(
        controls=[
            title,
            old_input,
            new_input,
            change_password,
            change_password_status,
            logout,
            btn_cancel
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    account_stack = ft.Stack(
        expand=True,
        controls=[
            background_image,
            ft.Container(
                content=account,
                alignment=ft.alignment.Alignment.CENTER,
                padding=ft.padding.Padding.all(30),
                expand=True,
            ),
        ],
    )

    page.add(account_stack)