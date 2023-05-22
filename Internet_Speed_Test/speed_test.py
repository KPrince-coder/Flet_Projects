import flet as ft
from flet import Page, Text, LinearGradient, Container, Row, Column, ProgressBar, UserControl
from time import sleep
import random
import test

# Variables
WIDTH = 640
HEIGHT = 655
COLORS = {
    'yellow': '#fcbf30',
    'red': '#d62829',
    'green': '#8ac926',
    'greyish': '#030405',
    'blue': '#0496ff'
}
l = list(range(5))
rand_col_1, rand_col_2 = '#354f52', '#252323'


# class Process(UserControl):
#     def __init__(self, start_container):
#         super().__init__()
#         self.start_container = start_container


#     def build(self):
#         text = Text(
#         value='',
#         weight=14,
#         )
#         self.processing = Column(
#             controls=[
#                 self.text.value = 'hel'
#             ]
#         )

class App(UserControl):
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

    # defining lines of texts
    line_01 = Text(
        value='> press start...',
        italic=True,
        size=14,
        weight=ft.FontWeight.W_600,
        opacity=0.9
    )
    line_02 = Text(
        value='',
        italic=True,
        size=14,
        weight=ft.FontWeight.W_600,
        color=COLORS['green']
    )
    line_03 = Text(
        value='',
        italic=True,
        size=14,
        weight=ft.FontWeight.W_600,
        color=COLORS['green'],
        visible=False
    )
    line_04 = Text(
        value='',
        italic=True,
        size=14,
        weight=ft.FontWeight.W_600,
        color=COLORS['yellow']
    )
    line_05 = Text(
        value='',
        italic=True,
        size=14,
        weight=ft.FontWeight.W_600,
        color=COLORS['green']
    )
    line_06 = Text(
        value='',
        italic=True,
        size=14,
        weight=ft.FontWeight.W_600,
        color=COLORS['green']
    )
    line_07 = Text(
        value='',
        italic=True,
        size=14,
        weight=ft.FontWeight.W_600,
        opacity=0.9
    )
    line_08 = Text(
        value='',
        size=14,
        weight=ft.FontWeight.W_600,
        opacity=0.9
    )
    line_09 = Text(
        value='',
        size=14,
        weight=ft.FontWeight.W_600,
        opacity=0.9
    )

    progress_bar_1 = Row(
        controls=[
            Text(value='  '),
            ProgressBar(
                height=500,
                bgcolor=COLORS['blue'],
                visible=False
            )
        ]
    )
    progress_bar_2 = Row(
        controls=[
            Text(value='  '),
            ProgressBar(
                height=500,
                bgcolor=COLORS['blue'],
                visible=False
            )
        ]
    )

    lines_of_texts = Column(
        controls=[
            line_01,
            line_02,
            line_03,
            progress_bar_1,
            line_04,
            line_05,
            line_06,
            progress_bar_2,
            line_07,
            line_08,
            line_09
        ]
    )

    @property
    def __page_header(self):
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
        self.main_frame_container = Container(
            height=100,
            width=200,
            bgcolor=ft.colors.with_opacity(0.7, COLORS['greyish']),
            border_radius=ft.border_radius.all(10),
            padding=ft.padding.all(12),
            animate=ft.animation.Animation(
                duration=1000,
                curve=ft.animation.AnimationCurve.BOUNCE_OUT
            ),
            content=self.lines_of_texts
        )
        return self.main_frame_container

    @property
    def __spacing(self):
        """Provides spacing"""
        return Container(
            padding=5
        )

    def __process_container(self, e):
        self.line_01.value = ''
        self.line_02.value = ''
        self.line_03.value = ''
        self.line_04.value = ''
        self.line_05.value = ''
        self.line_06.value = ''
        # self.line_07.value = ''
        self.main_frame_container.update()
        self.main_frame_container.width = 500
        self.main_frame_container.height = 400
        self.line_01.value = '> calculating download speed, please wait...'
        self.line_02.value = f'> finding the best servers  {test.country}, {test.city} ({test.country_code})'
        # self.line_03.value = f'finding the best possible servers in {random.choice(l)}'
        self.line_03.value = '> connection established, status OK, fetching download speed'
        self.progress_bar_1.visible = True
        sleep(5)
        self.main_frame_container.update()
        self.line_04.value = '> the download speed is {test.download_speed:.2f} Mbps'
        self.line_05.value = '> calculating the upload speed, please wait...'
        self.line_06.value = '> executing the upload script, hold on'
        self.progress_bar_2.visible = True
        sleep(3)
        self.main_frame_container.update()
        self.line_07.value = '> the upload speed is {test.download_speed:.2f} Mbps'
        self.line_08.value = '> task completed successfully\n\n'
        self.line_09.value = '>> app developer: Anointing'
        self.main_frame_container.update()

    def build(self):
        main_container = Container(
            width=WIDTH,
            height=HEIGHT,
            margin=ft.margin.all(-10),
            gradient=self.gradient_generator(rand_col_1, rand_col_2),
            alignment=ft.alignment.center,
            content=Container(
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=-54),
                content=Column(
                    width=HEIGHT,
                    height=HEIGHT,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        self.__page_header,
                        # spacing
                        self.__spacing,
                        self.__on_start_container,
                        # spacing
                        self.__spacing,

                        ft.IconButton(
                            icon=ft.icons.PLAY_CIRCLE_FILL_ROUNDED,
                            tooltip='start',
                            icon_color=COLORS['green'],
                            scale=ft.Scale(2),
                            on_click=self.__process_container

                        )

                    ]
                )
            )
        )

        return main_container


def main(page: Page):
    page.title = 'Internet Speed Test'
    page.window_height = HEIGHT
    page.window_max_height = HEIGHT
    page.window_width = WIDTH
    page.window_max_width = HEIGHT
    # page.window_bgcolor = 'red'
    page.theme_mode = ft.ThemeMode.DARK
    # page.auto_scroll = True
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_maximizable = False
    page.theme = ft.Theme(font_family='Source Code Pro ExtraLight')
    page.update()

    page.add(App())
    page.update()


ft.app(target=main)
