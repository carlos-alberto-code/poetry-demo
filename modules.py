from flet import icons as icon
from package_navigation.Module import Module, Section
from inventory_view.view_section import ContentStockSectionShape as ProductSection


Module(
    'Compras',
    icon.SHOPPING_CART,
    Section(label='Proveedores', icon=icon.PEOPLE),
    Section(label='Compras', icon=icon.SHOPPING_BAG),
)

Module(
    'Punto de venta', # Module name
    icon.POINT_OF_SALE_SHARP, # Module icon
    Section(label='Tienda', icon=icon.STOREFRONT),
    Section(label='Inventario', icon=icon.INVENTORY, content=ProductSection()),
    Section(label='Ventas', icon=icon.SAILING_SHARP),
)
