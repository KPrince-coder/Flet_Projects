# """Date: Wednesday, April 25, 2023"""
import flet as ft
from time import sleep
from task_app import TaskApp
import os
import sys

# starts splash screen
if getattr(sys, 'frozen', False):
    import pyi_splash


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# closes splash screen
if getattr(sys, 'frozen', False):
    pyi_splash.close()


def main(page: ft.Page):
    page.fonts = {
        'Product-Sans': resource_path('fonts/Product sans.ttf')
    }
    page.title = 'To-Do App'
    page.window_width = 500
    page.window_height = 700
    page.auto_scroll = True
    # page.marg = ft.padding.only(left=30, right=30)
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_bgcolor = ft.colors.WHITE24
    page.window_maximizable = False
    page.window_resizable = False
    # page.window_center()
    page.splash = ft.ProgressBar(visible=False)

    def change_theme(e):
        """Changes the theme of the window

        Args:
            e (on_click): If theme is 'light', changes to 'dark' and vice versa
        """
        page.splash.visible = True
        match page.theme_mode:
            case ft.ThemeMode.LIGHT:
                page.theme_mode = ft.ThemeMode.DARK
                toggle_dark_light.tooltip = 'change to light theme'
            case ft.ThemeMode.DARK:
                page.theme_mode = ft.ThemeMode.LIGHT
                toggle_dark_light.tooltip = 'change to dark theme'

        page.update()
        # delay effect the animation
        sleep(0.5)
        # change the icon dark mode or light mode
        toggle_dark_light.selected = not toggle_dark_light.selected
        # disable the progressbar
        page.splash.visible = False
        page.update()

    toggle_dark_light = ft.IconButton(
        icon=ft.icons.DARK_MODE_OUTLINED,
        selected_icon=ft.icons.WB_SUNNY_OUTLINED,
        tooltip='change to dark mode',
        on_click=change_theme,
        style=ft.ButtonStyle(
            color={
                '': ft.colors.BLACK54, 'selected': ft.colors.WHITE
            },
        )
    )

    page.appbar = ft.AppBar(
        title=ft.Text(
            value='TO-DO LISTS',
            font_family='Product-Sans',
            size=20,
            weight=ft.FontWeight.W_600,
            color=ft.colors.BLUE_GREY_700
        ),
        center_title=True,
        elevation=4,
        bgcolor=ft.colors.ORANGE_100,
        actions=[
            toggle_dark_light
        ]
    )

    app = TaskApp()

    page.add(
        app,
    )
    page.update()


ft.app(target=main, assets_dir='assets')
