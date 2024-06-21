from dataclasses import dataclass, field, asdict
import flet as ft


# TODO: Implementar Strategy para hacer permitir el cambio en tiempo de ejecución

@dataclass
class _LightColorPalette:
    # Colores principales para tema claro
    primary:        str = field(default='#2A2B47')  # azul oscuro
    on_primary:     str = field(default='#F2F2F2')  # blanco grisáceo
    secondary:      str = field(default='#BFA8FF')  # lila
    on_secondary:   str = field(default='#2A2B47')  # azul oscuro
    tertiary:       str = field(default='#FEE6C2')  # melocotón claro
    on_tertiary:    str = field(default='#2A2B47')  # azul oscuro
    # Colores de fondo y superficie para tema claro
    background:     str = field(default='#DFDFDF')  # gris
    on_background:  str = field(default='#2A2B47')  # azul oscuro
    surface:        str = field(default='#F2F2F2')  # blanco grisáceo
    on_surface:     str = field(default='#2A2B47')  # azul oscuro
    # Color de bordes para tema claro
    outline:        str = field(default='#2A2B47')  # azul oscuro
    outline_variant:str = field(default='#BFA8FF')  # lila
    # Color de sombras para tema claro
    shadow:         str = field(default='#DFDFDF')  # gris
    scrim:          str = field(default='#DFDFDF')  # gris
    surface_tint:   str = field(default='#BFA8FF')  # lila


@dataclass
class _DarkColorPalette:
    # Colores principales para tema oscuro
    primary:        str = field(default='#F2F2F2')  # blanco grisáceo
    on_primary:     str = field(default='#2A2B47')  # azul oscuro
    secondary:      str = field(default='#7F5AFF')  # lila oscuro
    on_secondary:   str = field(default='#F2F2F2')  # blanco grisáceo
    tertiary:       str = field(default='#B3845A')  # melocotón oscuro
    on_tertiary:    str = field(default='#F2F2F2')  # blanco grisáceo
    # Colores de fondo y superficie para tema oscuro
    background:     str = field(default='#2A2B47')  # azul oscuro
    on_background:  str = field(default='#DFDFDF')  # gris
    surface:        str = field(default='#2A2B47')  # azul oscuro
    on_surface:     str = field(default='#DFDFDF')  # gris
    # Color de bordes para tema oscuro
    outline:        str = field(default='#F2F2F2')  # blanco grisáceo
    outline_variant:str = field(default='#7F5AFF')  # lila oscuro
    # Color de sombras para tema oscuro
    shadow:         str = field(default='#2A2B47')  # azul oscuro
    scrim:          str = field(default='#2A2B47')  # azul oscuro
    surface_tint:   str = field(default='#7F5AFF')  # lila oscuro


_light_color_palette = asdict(_LightColorPalette())
_dark_color_palette  = asdict(_DarkColorPalette())


_light_text_theme = ft.TextTheme(
    title_large=ft.TextStyle(size=21, font_family="Roboto", color=_LightColorPalette.primary),
    body_medium=ft.TextStyle(size=14, font_family="Lato", color=_LightColorPalette.primary),
)


_dark_text_theme = ft.TextTheme(
    title_large=ft.TextStyle(size=21, font_family="Roboto", color=_DarkColorPalette.primary),
    body_medium=ft.TextStyle(size=14, font_family="Lato", color=_DarkColorPalette.primary),
)


LightTheme = ft.Theme(
    color_scheme=ft.ColorScheme(**_light_color_palette),
    text_theme=_light_text_theme
)



DarkTheme = ft.Theme(
    color_scheme=ft.ColorScheme(**_dark_color_palette),
    text_theme=_dark_text_theme
)
