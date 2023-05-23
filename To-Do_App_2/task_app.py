from flet import *
from time import ctime
import re


def check_value(value):
    pattern = re.compile('\S')
    return bool(pattern.findall(value))


if __name__ == '__main__':
    # trial of the check value function
    s = ''
    ss = '      '
    sss = '          s     '
    s4 = '     se2'
    print(check_value(s), check_value(ss), check_value(sss), check_value(s4))


class TaskApp(UserControl):
    def build(self):
        self.__type_area = TextField(
            text_style=TextStyle(
                size=18,
                weight=FontWeight.W_500,
            ),
            hint_text='What should be done?',
            width=390,
            hint_style=TextStyle(
                size=18,
                weight=FontWeight.W_400
            ),
            shift_enter=True,
            max_lines=2,
            max_length=50,
            autofocus=True,
            capitalization=TextCapitalization.SENTENCES
        )
        self.__add_button = FloatingActionButton(
            icon=icons.ADD_OUTLINED,
            on_click=self.__add_task,
            bgcolor='#99D98C',
            tooltip='add task'
        )

        self.__tasks = Column(
            auto_scroll=True,
            scroll=ScrollMode.ADAPTIVE,

        )

        view = Column(
            controls=[
                Row(
                    controls=[
                        self.__type_area,
                        self.__add_button
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=CrossAxisAlignment.START

                ),
                self.__tasks
            ]
        )
        return view

    def __add_task(self, e):
        if not self.__type_area.value or check_value(self.__type_area.value) == False:
            self.__type_area.error_text = 'Task cannot be empty!'
            self.__type_area.value = ''
            # self.update()
        else:
            task = Task(self.__type_area.value.strip(), self.__delete_task)
            self.__tasks.controls.append(task)
            self.__type_area.value = ''
            self.__type_area.error_text = ''
        self.update()

    def __delete_task(self, task):
        self.__tasks.controls.remove(task)
        self.update()


class Task(UserControl):
    def __init__(self, input_text, delete_task):
        super().__init__()
        self.input_text = input_text
        self.delete_task = delete_task

    def build(self):
        self.display_task = Checkbox(
            label=self.input_text,
            # tooltip='mark done' if self.display_task.value == False else 'mark undone',
            value=False,
            check_color='#29bf12',
            fill_color={
                MaterialState.SELECTED: '#f2e8cf'
            }
        )
        self.edit_input = TextField(
            capitalization=TextCapitalization.SENTENCES,
            max_length=50,
            width=390
        )
        self.time_display = Text(
            value=f'Created time: {ctime()}',
            italic=True,
            size=10,
            weight=FontWeight.W_400,
            text_align=TextAlign.END,
            # color='#000000'
        )
        self.view_display = Column(
            controls=[
                Row(
                    controls=[
                        self.display_task,
                        Row(
                            controls=[
                                IconButton(
                                    icon=icons.EDIT_OUTLINED,
                                    on_click=self.edit_task,
                                    tooltip='edit task',
                                    icon_color='#168AAD'

                                ),
                                IconButton(
                                    icon=icons.DELETE_OUTLINED,
                                    tooltip='delete task',
                                    icon_color='#e63946',
                                    on_click=self.open_delete_dialog
                                )
                            ]
                        ),

                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                self.time_display
            ],
            horizontal_alignment=CrossAxisAlignment.END
        )

        self.edit_display = Row(
            visible=False,
            controls=[
                self.edit_input,
                IconButton(
                    icon=icons.DONE_OUTLINED,
                    icon_size=30,
                    icon_color='#99D98C',
                    tooltip='save edit',
                    on_click=self.save_edit
                )
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN
        )

        # def close(e):
        #     self.delete_dialog.open = False
        #     # self.delete()
        #     self.update()

        self.delete_dialog = AlertDialog(
            title=Text(value='Please confirm'),
            content=Text(value='Do you really want to delete this task?'),
            actions_alignment=MainAxisAlignment.END,
            actions=[
                TextButton(
                    text='Yes',
                    on_click=self.delete
                    # on_click=(lambda x, e:x, (x for x in [
                    #           self.delete, self.close_dialog]))
                ),
                TextButton(
                    text='No',
                    on_click=self.close_dialog
                ),
                TextButton(
                    text='Cancel',
                    on_click=self.close_dialog
                )
            ],
        )
        return Column(
            controls=[
                self.view_display,
                self.edit_display,
                self.delete_dialog
            ]
        )

    def open_delete_dialog(self, e):
        self.delete_dialog.open = True
        self.update()

    def close_dialog(self, e):
        self.delete_dialog.open = False
        self.update()

    def edit_task(self, e):
        self.view_display.visible = False
        self.edit_display.visible = True
        self.edit_input.value = self.display_task.label
        self.edit_input.autofocus = True
        self.update()

    def save_edit(self, e):
        if not self.edit_input.value or check_value(self.edit_input.value) == False:
            self.edit_input.error_text = 'Task cannot be empty!'
            self.edit_input.value = ''
        else:
            self.edit_display.visible = False
            self.view_display.visible = True
            self.display_task.label = self.edit_input.value
            self.time_display.value = f'Modified time: {ctime()}'
        self.update()

    def delete(self, e):
        self.delete_dialog.open = False
        self.delete_dialog.clean()
        # self.update()
        self.delete_task(self)
        self.update()

    # def cause_deletion(self, e):
    #     if self.delete_dialog.actions[0].on_click == True:
    #         self.delete_dialog.actions[0].on_click = self.close_dialog
    #         self.delete_dialog.visible = False
    #     else:
    #         # self.delete_dialog.update()
    #         self.delete_dialog.actions[0].on_click = self.close_dialog
    #         self.delete_dialog.open = False
    #         self.update
