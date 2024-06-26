import flet as ft
from typing import Optional


class IntCounter(ft.Card):

    def __init__(
            self,
            width: Optional[int] = 150,
            elevation: Optional[int] = 0,
            start_value: Optional[int] = 1,
            end_value: Optional[int] = 100,
            readonly: Optional[bool] = True,
            on_counter_change=None,
            # step_increment: Optional[int] = 1,
            # negative_values: Optional[bool] = False,
            
    ):
        super().__init__(
            width=width,
            elevation=elevation,
            # alignment=ft.alignment.center,
             
        )
        self.on_click = on_counter_change
        self._start_value = start_value
        self._end_value = end_value
        # self._step_increment = step_increment
        # self._negative_values = negative_values
        self._txtfld = ft.TextField(
            border=ft.InputBorder.NONE,
            expand=True,
            adaptive=True,
            value=str(start_value),
            text_size=15,
            text_align=ft.TextAlign.CENTER,
            text_vertical_align=ft.VerticalAlignment.START,
            input_filter=ft.NumbersOnlyInputFilter(),
            read_only=readonly,
            on_change=on_counter_change,
            on_blur=self.handle_on_blur,
        )
        self._minus_button = ft.IconButton(
            icon=ft.icons.REMOVE,
            on_click=self.decrement,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10)
            ),
        )
        self._plus_button = ft.IconButton(
            icon=ft.icons.ADD,
            on_click=self.increment,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10)
            ),
        )
        self.content = ft.Row(
            controls=[
                self._minus_button,
                self._txtfld,
                self._plus_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            # height=40,
        )
    
    @property
    def value(self):
        return str(self._txtfld.value)
    
    @value.setter
    def value(self, value: int):
        self._txtfld.value = str(value)
    
    def handle_on_blur(self, event: ft.ControlEvent):
        # Si el valor del campo es mayor que el valor final, se establece el valor final
        if self.value is not None and self._end_value is not None and int(self.value) > int(self._end_value):
            self.value = int(self._end_value)
            self._txtfld.update()

    def increment(self, event):
        if self.value is not None and self._end_value is not None and int(self.value) < int(self._end_value):
            self.value = int(self.value) + 1
        else:
            if self._end_value is not None:
                self.value = int(self._end_value)
        self._txtfld.update()
        if self.on_click is not None:
            self._plus_button.data = self.value
            self.on_click(event)

    def decrement(self, event):
        if self.value is not None and int(self.value) > 0:
            self.value = int(self.value) - 1
        if self.value is not None and self._end_value is not None and int(self.value) > int(self._end_value):
            self.value = int(self._end_value)
        self._txtfld.update()
        if self.on_click is not None:
            self._minus_button.data = self.value
            self.on_click(event)

class FloatCounter(ft.Card):
    def __init__(
            self,
            width: Optional[int] = 150,
            elevation: Optional[int] = 0,
            start_value: Optional[int] = 1,
            end_value: Optional[int] = 100,
            readonly: Optional[bool] = True,
            on_click=None,
            # step_increment: Optional[int] = 1,
            # negative_values: Optional[bool] = False,
    ):
        super().__init__(
            width=width,
            elevation=elevation,
            # alignment=ft.alignment.center,
             
        )
        self.on_click = on_click
        self._start_value = start_value
        self._end_value = end_value
        # self._step_increment = step_increment
        # self._negative_values = negative_values
        self._txtfld = ft.TextField(
            border=ft.InputBorder.NONE,
            expand=True,
            adaptive=True,
            value=str(start_value),
            text_size=15,
            text_align=ft.TextAlign.CENTER,
            text_vertical_align=ft.VerticalAlignment.START,
            input_filter=ft.InputFilter(
                regex_string= r"^\d+(\.\d{0,2})?$"
            ),
            #read_only=readonly,
            #on_change= self.validate_input
        )
        self._minus_button = ft.IconButton(
            icon=ft.icons.REMOVE,
            on_click=self.decrement,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10)
            ),
        )
        self._plus_button = ft.IconButton(
            icon=ft.icons.ADD,
            on_click=self.increment,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10)
            ),
        )
        self.content = ft.Row(
            controls=[
                self._minus_button,
                self._txtfld,
                self._plus_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    
    def validate_input(self, txtfld: ft.TextField):
        value = txtfld.value
        if not value == r"^\d+(\.\d{0,1})?$":
            txtfld.error_text = "Invalid input. Only numbers with up to one decimal place are allowed."
            print(txtfld.error_text)
        else:
            txtfld.error_text = ""

    @property
    def value(self):
        return str(self._txtfld.value)
    
    @value.setter
    def value(self, value: int):
        self._txtfld.value = str(value)
    
    def increment(self, event):
        if self.value is not None and self._end_value is not None and int(self.value) < int(self._end_value):
            self.value = int(self.value) + 1
        else:
            if self._end_value is not None:
                self.value = int(self._end_value)
        self._txtfld.update()
        if self.on_click is not None:
            self._plus_button.data = self.value
            self.on_click(event)

    def decrement(self, event):
        if self.value is not None and int(self.value) > 0:
            self.value = int(self.value) - 1
        if self.value is not None and self._end_value is not None and int(self.value) > int(self._end_value):
            self.value = int(self._end_value)
        self._txtfld.update()
        if self.on_click is not None:
            self._minus_button.data = self.value
            self.on_click(event)
            