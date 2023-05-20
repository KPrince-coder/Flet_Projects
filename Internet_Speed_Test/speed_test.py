import flet as ft
from flet import Page, Text, LinearGradient, Container, Row, Column
import random
from time import sleep

# Variables
WIDTH = 640
HEIGHT = 660
COLORS = {
    'yellow': '#fcbf30',
    'red': '#d62829',
    'green': '#8ac926',
    'greyish': '#030405'
}

rand_col_1, rand_col_2 = '#354f52', '#252323'


class App(ft.UserControl):
    @staticmethod
    def gradient_generator(start_col, end_col):
        """Generates gradient colors using the colors passed as parameters

        Args:
            start_col (color_): first color of gradient
            end_col (color): second color of gradient

        Returns:
            gradient_color: A gradient of two colors
        """
        return LinearGradient(
            colors=[start_col, end_col],
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            rotation=4.8
        )

    @property
    def __page_title(self):
        """Returns the header of the page
        """
        return Text(
            value='Internet',
            size=52,
            font_family='Lobster',
            color=COLORS.get('red'),
            spans=[
                ft.TextSpan(
                    text='Speed',
                    style=ft.TextStyle(
                        size=52,
                        color=COLORS['yellow'],
                    )
                )
            ]

        )

    @property
    def __on_start_container(self):
        return Container(
            height=100,
            width=200,
            bgcolor=ft.colors.with_opacity(0.7, COLORS['greyish']),
            border_radius=ft.border_radius.all(10)
        )

    @property
    def __spacing(self):
        """Provides spacing between"""
        return Container(
            padding=5
        )

    def build(self):
        self.__background = Container(
            width=WIDTH,
            height=HEIGHT,
            margin=ft.margin.all(-10),
            gradient=self.gradient_generator(rand_col_1, rand_col_2),
            # animate=ft.animation.Animation(
            #     4, curve=ft.animation.AnimationCurve.EASE_IN_OUT
            # ),
            alignment=ft.alignment.center,
            content=Container(
                alignment=ft.alignment.center,
                content=Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        self.__page_title,
                        # spacing
                        self.__spacing,
                        self.__on_start_container,
                        # spacing
                        self.__spacing,

                        ft.IconButton(
                            icon=ft.icons.PLAY_CIRCLE_FILL_ROUNDED,
                            tooltip='start',
                            icon_color=COLORS['green'],
                            scale=ft.Scale(2)

                        )

                    ]
                )
            )

        )
        return self.__background


def main(page: Page):
    page.title = 'Internet Speed Test'
    page.window_max_height = HEIGHT
    page.window_max_width = WIDTH
    # page.window_bgcolor = 'red'
    page.theme_mode = ft.ThemeMode.DARK
    # page.auto_scroll = True
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_maximizable = False
    page.theme = ft.Theme(font_family='Source Code Pro ExtraLight')
    page.update()

    page.add(App(), Text('hello world', size=54))
    page.update()


ft.app(target=main)
