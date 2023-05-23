"""Date Completed: Tuesday, May 23, 2023. It took me about 3-4 days to complete"""
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
    )
    line_04 = Text(
        value='',
        # italic=True,
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
        size=14,
        weight=ft.FontWeight.W_600,
        opacity=0.9,
        color=COLORS['yellow']

    )
    line_08 = Text(
        value='',
        size=14,
        italic=True,
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
            Text(value=' '),
            ProgressBar(
                width=420,
                color='#0466c8',
                bgcolor='#edf2fb',
                visible=False
            )
        ]
    )
    progress_bar_2 = Row(
        controls=[
            Text(value=' '),
            ProgressBar(
                width=420,
                color='#0466c8',
                bgcolor='#edf2fb',
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
        self.line_01.value = 'Loading...'
        self.line_01.color = 'white'
        self.line_01.opacity = 0.9
        self.progress_bar_1.controls[1].visible = True
        self.main_frame_container.update()
        sleep(3)

        # assigns values of various variables to them
        self.progress_bar_1.controls[1].value = 1
        download, upload, cc, city, country = test.run_speed_test()
        if download != None:
            self.progress_bar_1.controls[1].visible = False
            self.progress_bar_1.controls[1].value = None
            self.progress_bar_2.controls[1].visible = False
            self.progress_bar_2.controls[1].value = None

            self.line_01.value = ''
            self.line_02.value = ''
            self.line_03.value = ''
            self.line_04.value = ''
            self.line_05.value = ''
            self.line_06.value = ''
            self.line_07.value = ''
            self.line_08.value = ''
            self.line_09.value = ''
            self.main_frame_container.update()
            self.main_frame_container.width = 550
            self.main_frame_container.height = 400
            self.main_frame_container.update()

            sleep(1)

            self.line_01.value = '> calculating download speed, please wait...'
            self.line_01.color = 'white'
            self.main_frame_container.update()
            sleep(2)

            self.line_02.value = f'> finding the best servers in {city}, {country} ({cc})'
            # self.line_02.value = f'> finding the best possible servers in {random.choice(l)}'
            self.main_frame_container.update()
            sleep(2)

            self.line_03.value = '> connection established, status OK, fetching download speed'
            self.main_frame_container.update()

            self.progress_bar_1.controls[1].visible = True
            self.main_frame_container.update()
            sleep(5)

            self.progress_bar_1.controls[1].value = 1

            self.line_04.value = f'> the download speed is {download:.2f} Mbps'
            self.line_05.value = '> calculating the upload speed, please wait...'
            sleep(2)

            self.line_06.value = '> executing the upload script, hold on'
            self.progress_bar_2.controls[1].visible = True
            self.main_frame_container.update()
            sleep(4)

            self.progress_bar_2.controls[1].value = 1

            self.line_07.value = f'> the upload speed is {upload:.2f} Mbps'
            self.line_08.value = '> task completed successfully\n'
            self.line_09.value = '>> app developer: Kyeremeh Prince (Github: KPrince-coder)'
            # self.line_09.size = 13
            self.main_frame_container.update()
        else:
            self.progress_bar_1.controls[1].visible = False
            self.progress_bar_1.controls[1].value = None
            self.progress_bar_2.controls[1].visible = False
            self.progress_bar_2.controls[1].value = None

            self.line_01.value = ''
            self.line_02.value = ''
            self.line_03.value = ''
            self.line_04.value = ''
            self.line_05.value = ''
            self.line_06.value = ''
            self.line_07.value = ''
            self.line_08.value = ''
            self.line_09.value = ''
            self.main_frame_container.update()
            self.main_frame_container.width = 200
            self.main_frame_container.height = 100
            self.main_frame_container.update()
            self.line_01.value = 'An error has occurred. Please check your internet connection!'
            self.line_01.color = COLORS['red']
            self.line_01.opacity = 0.9
            self.main_frame_container.update()
            print('ERROR::Check your internet connection!')

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
