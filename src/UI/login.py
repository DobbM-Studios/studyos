import os
import sys
import flet as ft

# Configuración de rutas (Mantenido intacto)
ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ruta_src not in sys.path:
    sys.path.append(ruta_src)

from core import session

def main(page: ft.Page):
    page.title = "studyos | login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    
    title = ft.Text(
        value="Welcome!", 
        size=32, 
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
        hint_text="MyUserName",
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

    # CAMBIO AQUÍ: ft.ElevatedButton -> ft.Button
    # Botón Adaptado a Flet 1.0+
    btn_next = ft.Button(
        # 'content' define lo que va dentro del botón. Ponemos fila (Row) con Texto e Icono
        content=ft.Row(
            controls=[
                ft.Text("Continue", weight=ft.FontWeight.BOLD),
                ft.Icon(ft.icons.Icons.ARROW_FORWARD, size=18)
            ],
            alignment=ft.MainAxisAlignment.CENTER, # Centra el contenido internamente
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

    page.add(form_container)

if __name__ == "__main__":
    # Ejecución moderna nativa de Flet 1.0+
    ft.run(main)
