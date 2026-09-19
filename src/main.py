from UI import login, register, menu
import flet as ft
from pathlib import Path


def main(page: ft.Page):
    page.clean()
    page.title = "studyos | landing"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.TRANSPARENT
    page.padding = 0

    bg_path = Path(__file__).resolve().parents[1] / "images" / "bg-0.jpg"
    bg_src = str(bg_path)

    title = ft.Text(
        value="Welcome to StudyOS",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700,
    )

    btn_login = ft.Button(
        content=ft.Row(
            controls=[
                ft.Text("Login", weight=ft.FontWeight.BOLD),
                ft.Icon(ft.icons.Icons.ARROW_FORWARD, size=18),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        width=300,
        height=45,
        elevation=2,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
        on_click=lambda e: do_login(),
    )

    btn_register = ft.Button(
        content=ft.Row(
            controls=[
                ft.Text("Create account", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Icon(ft.icons.Icons.CIRCLE, size=18, color=ft.Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        width=300,
        height=45,
        elevation=2,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            bgcolor=ft.Colors.BLUE_700,
            color=ft.Colors.WHITE,
            overlay_color=ft.Colors.BLUE_900,
        ),
        on_click=lambda e: do_register(),
    )

    content = ft.Column(
        controls=[title, btn_login, btn_register],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    background = ft.Image(
        src=bg_src,
        fit=ft.BoxFit.COVER,
        expand=True,
    )

    overlay = ft.Container(
        expand=True,
        alignment=ft.alignment.Alignment.CENTER,
        content=content,
    )

    root = ft.Stack(
        expand=True,
        controls=[background, overlay],
    )

    def resize_root(_):
        background.width = page.width
        background.height = page.height
        overlay.width = page.width
        overlay.height = page.height

    resize_root(None)
    page.on_resize = resize_root
    page.add(root)


    def save_session(result):
        global USERNAME, SESSION_TOKEN
        try:
            if isinstance(result, (tuple, list)) and len(result) >= 2:
                USERNAME, SESSION_TOKEN = result[0], result[1]
                return True
        except Exception:
            pass

        USERNAME, SESSION_TOKEN = (None, None)
        return False

    def do_login():
        def handle_success(result):
            if save_session(result):
                menu.main(page)

        login.main(page, on_success=handle_success)

    def do_register():
        def handle_success(result):
            if save_session(result):
                menu.main(page)

        register.main(page, on_success=handle_success)

if __name__ == "__main__":
    ft.run(main)
