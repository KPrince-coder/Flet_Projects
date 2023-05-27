"""Date: Friday - Saturday May 27, 2023"""
import flet as ft
from flet import UserControl, Page, Text, Column, Row, TextField, Container
import flet_material as fm
import database
import re
import time


INPUT_WIDTH = 300  # input field width
INPUT_HEIGHT = 52  # input field height
PRIMARY = 'indigo'  # general color layout
fm.Theme.set_theme(theme=PRIMARY)


def num_of_spaces(string: str) -> int:
    """Returns the number of spaces in the provided string parameter value"""
    pattern = re.compile('\s')
    return len(pattern.findall(string))


if __name__ == '__main__':
    print(bool(num_of_spaces('')))
    print(num_of_spaces(''))


class InputField(UserControl):
    def __init__(self, field_name: str, password: bool):
        super().__init__()

        self.input: ft.Control = TextField(
            width=INPUT_WIDTH,
            height=INPUT_HEIGHT,
            text_style=ft.TextStyle(
                color=ft.colors.BLACK54,
                size=18
            ),
            label=field_name,
            label_style=ft.TextStyle(
                size=16,
                color=ft.colors.with_opacity(0.6, fm.Theme.bgcolor)
            ),
            password=password,
            border=ft.InputBorder.OUTLINE,
            border_radius=ft.border_radius.all(5),
            border_color=fm.Theme.bgcolor,
            autofocus=True,
            focused_border_color=PRIMARY,
            focused_border_width=1.5,
            cursor_color=PRIMARY,
            cursor_radius=8,
            content_padding=ft.padding.symmetric(
                horizontal=16,
                vertical=6
            ),
            cursor_width=1.5,
            # error_style=,
            on_focus=lambda e: self.input_focus(self.input.label),
            on_blur=lambda e: self.input_blur(),
            # on_submit=lambda e: self.submit(self.input_label, self.input.value)
        )

        self.input_box: ft.Container = Container(
            content=self.input,
            shadow=None,
            animate=ft.Animation(100, 'easeIn'),
        )

    def input_focus(self, input_label):
        """It shows different contents upon focus on each input field

        Args:
            input_label (str): The display of the content of the field is depended on this parameter
        """
        if input_label == 'User Name':
            self.input.capitalization = ft.TextCapitalization.WORDS
            # self.input.error_text = None
            self.input.hint_text = 'first name and last name'
            self.input.hint_style = ft.TextStyle(
                size=16,
                color=ft.colors.with_opacity(0.4, fm.Theme.bgcolor)
            )
            self.input.update()

        if input_label == 'Email':
            self.input.suffix_text = '.com'
            # self.input.err
            self.input.suffix_style = ft.TextStyle(
                size=18,
                color=ft.colors.BLACK54,
            )
            self.input.update()

        if input_label == 'Password':
            self.input.can_reveal_password = True
            self.input.update()

        self.input.label_style.color = PRIMARY
        self.input.update()
        self.input_box.shadow = ft.BoxShadow(
            spread_radius=3,
            blur_radius=3,
            color=ft.colors.with_opacity(0.025, ft.colors.BLACK12),
            offset=ft.Offset(6, 4)
        )

        self.input.error_text = None

        self.update()

    def input_blur(self):
        """Closes the contents showed when focus was on the input field. It fires only when the input field losses focus
        """

        # user name
        self.input.helper_text = None
        self.input.helper_style = None
        self.input.update()

        # password
        self.input.can_reveal_password = False

        # general
        self.input.label_style.color = ft.colors.with_opacity(
            0.5, fm.Theme.bgcolor)
        self.input_box.shadow = None

        self.update()

    def build(self):
        return self.input_box


class FormUI(UserControl):
    def __init__(self, font_medium):
        super().__init__()
        self.font_family_medium = font_medium

        self.user_name = InputField('User Name', 'False')
        self.email = InputField('Email', 'False')
        self.password = InputField('Password', 'True')
        self.confirm_password = InputField('Confirm Password', True)
        self.passwords = Column(
            controls=[self.password, self.confirm_password],

        )
        self.submit_button = ft.ElevatedButton(
            content=Text(
                value='Sign Up',
                size=18,
                font_family=self.font_family_medium,
            ),
            width=INPUT_WIDTH,
            height=INPUT_HEIGHT - 10,
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: PRIMARY,
                    ft.MaterialState.FOCUSED: PRIMARY,
                    ft.MaterialState.DEFAULT: 'white'
                },
                shape=ft.RoundedRectangleBorder(
                    radius=5,
                ),
                # bgcolor=PRIMARY,
                bgcolor={
                    ft.MaterialState.HOVERED: 'white',
                    ft.MaterialState.FOCUSED: 'white',
                    ft.MaterialState.DEFAULT: PRIMARY,
                },
                side={
                    ft.MaterialState.HOVERED: ft.BorderSide(1.5, PRIMARY),
                    ft.MaterialState.FOCUSED: ft.BorderSide(1.5, PRIMARY)
                },
                elevation=5,
                # overlay_color='red',
                # surface_tint_color='yellow',
                animation_duration=500
            ),
            on_click=lambda e: self.submit()
            # animate_opacity=ft.Animation(100, ft.AnimationCurve.BOUNCE_IN ),
        )

        self.log_in = Row(
            width=INPUT_WIDTH,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                Text(
                    value='Have an account?',
                    size=14,
                    font_family=self.font_family_medium,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.colors.with_opacity(0.8, fm.Theme.bgcolor),
                    spans=[
                        ft.TextSpan(
                            text=' Log In',
                            style=ft.TextStyle(
                                color=PRIMARY,
                                font_family=None,
                            ),
                            # on_click=lambda e: self.log_in(),
                            # tool

                        )
                    ]
                )
            ]
        )

    def submit(self):
        username = self.user_name.input
        e_mail = self.email.input
        pas_ = self.password.input
        con_pass_ = self.confirm_password.input

        if not username.value or bool(num_of_spaces(username.value)) or not pas_.value or not con_pass_.value or pas_.value != con_pass_.value or not e_mail.value or bool(num_of_spaces(e_mail.value)) or '@' not in e_mail.value:

            def errors_style(field_name):
                """Defines the error style of the input field and the label text"""
                field_name.label_style = ft.TextStyle(
                    color=ft.colors.with_opacity(0.85, 'red')
                )
                field_name.error_style = ft.TextStyle(
                    size=11,
                    color=ft.colors.with_opacity(0.85, 'red')
                )
                field_name.update()

            # checks for empty fields
            if not username.value or not e_mail.value or not pas_.value or not con_pass_:
                # print('hey')
                for field in [username, e_mail, pas_, con_pass_]:
                    if not field.value:
                        field.error_text = f'{str(field.label).lower()} cannot be empty!'
                        errors_style(field)

                self.update()

            # checks spacing in email and username fields
            if bool(num_of_spaces(e_mail.value)) or num_of_spaces(username.value) > 1 or '@' not in e_mail.value:
                # print('supppppppppp')
                if '@' not in e_mail.value:
                    e_mail.error_text = 'email must contain "@"'
                    errors_style(e_mail)
                    self.update()

                if bool(num_of_spaces(e_mail.value)):
                    e_mail.error_text = 'email cannot contain spaces!'
                    errors_style(e_mail)
                    e_mail.update()

                if num_of_spaces(username.value) > 1:
                    username.error_text = 'name must be only two! check the spaces'
                    errors_style(username)
                    username.update()

            # checks for valid passwords
            if pas_.value:
                if len(pas_.value) < 6:
                    pas_.error_text = 'password must be at least 6 characters long'
                    errors_style(pas_)
                    pas_.update()

                elif pas_.value != con_pass_.value:
                    pas_.error_text = 'passwords do not match!'
                    errors_style(pas_)
                    pas_.update()

                    con_pass_.error_text = 'passwords do not match'
                    errors_style(con_pass_)
                    con_pass_.update()
        # else:
            # time of creation
        if username.value and num_of_spaces(username.value) <= 1 and pas_.value and con_pass_.value and pas_.value == con_pass_.value and e_mail.value and bool(num_of_spaces(e_mail.value)) == False and '@' in e_mail.value:

            # print('ooh heyyyyy')
            date_now = time.strftime('%b-%d-%Y %H:%M:%S')
            # submits record to the database
            print(date_now)
            database.add_record(
                username.value, (e_mail.value + e_mail.suffix_text).lower(), pas_.value, date_now)
            username.value = ''
            e_mail.value = ''
            pas_.value = ''
            con_pass_.value = ''
            username.autofocus = True
            self.update()

    def log_in():
        pass

    def build(self):
        main_container = Container(
            width=340,
            height=650,
            bgcolor='white',
            padding=ft.padding.all(10),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(10),
            shadow=ft.BoxShadow(
                spread_radius=6,
                blur_radius=4,
                color=ft.colors.with_opacity(0.1, 'black'),
                offset=ft.Offset(x=0, y=2)
            ),
            content=Column(
                alignment=ft.CrossAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        src='assets/images/sign_up.png',
                        height=160,
                        fit=ft.ImageFit.COVER,
                        repeat=ft.ImageRepeat.NO_REPEAT

                    ), Column(
                        spacing=24,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value='Welcome to Planner',
                                font_family=self.font_family_medium,
                                size=20,
                                text_align=ft.TextAlign.CENTER,
                                color=fm.Theme.bgcolor,
                                selectable=False,

                            ),
                            Column(
                                # spacing=0,
                                controls=[
                                    self.user_name,
                                    self.email,
                                    self.passwords,
                                    # for spacing,
                                    Container(
                                        padding=ft.padding.only(bottom=4), width=0),
                                    self.submit_button,
                                    Container(padding=ft.padding.only(
                                        bottom=2), width=0),
                                    self.log_in

                                ]
                            )

                        ]
                    ),

                ]
            )
        )
        return main_container


def main(page: Page):
    # font family
    page.fonts = {
        'WorkSans-Light': 'assets/fonts/WorkSans-Light.otf',
        'WorkSans-Regular': 'assets/fonts/WorkSans-Regular.otf',
        'WorkSans-Medium': 'assets/fonts/WorkSans-Medium.otf'
    }

    page.window_width = 600
    page.window_height = 760
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = fm.Theme.bgcolor
    page.theme = ft.Theme(font_family='WorkSans-Regular')
    page.update()
    # page.controls.append(Text('hey', size=35))

    page.add(FormUI('WorkSans-Medium'))
    page.update()


if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")
