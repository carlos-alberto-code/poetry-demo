# Aquí se maneja la lógica de los eventos de los diferentes componentes de la vista de la compra
# Además se sigue un principio que es es cada componente se modifica en su contexto.
import flet as ft
from controllers.controllers import ProductController
from modules.store_view.ProductCard import ProductCard
from modules.store_view.ProductItem import ProductItem
from modules.store_view.ProductDTO import ProductDTO as Product # Data Transfer Object



# HANDLERS ---------------------------------------------------------------------

def handle_on_tap(event: ft.ControlEvent): # Evento tap de la barra de búsqueda
    searcher.close_view()
    products = _wrap_productDTO_list(product_controller.get_all())
    gird_view.controls = _create_GirdView_product_cards(products)
    gird_view.update()
    
def handle_on_change(event: ft.ControlEvent): # Evento de búsqueda en tiempo real
    results = product_controller.search(str(searcher.value))
    products = _wrap_productDTO_list(results)
    gird_view.controls = _create_GirdView_product_cards(products)
    gird_view.update()

def handle_on_card_button_click(event: ft.ControlEvent): # Evento de click en el botón de la tarjeta
    button = event.control
    form_items.add(button.data)
    product_form.content = ft.Column(
        [create_form_item_cart(product) for product in form_items]
    )
    product_form.update()

def create_form_item(product: Product): # Crea un item del formulario de compra
    return ProductCard(product=product)

def create_form_item_cart(product: Product): # Crea un item del formulario de compra
    return ProductItem(product=product,on_click=remove_form_item_cart)

def remove_form_item_cart(event: ft.ControlEvent):
    button = event.control
    product = button.data
    form_items.remove(product)
    product_form.content = ft.Column(
        [create_form_item_cart(product) for product in form_items]
    )
    product_form.update()

    
# HELPER FUNCTIONS ------------------------------------------------------------

def _wrap_productDTO_list(results: list) -> list[Product]: # Envuelve las instancias en una lista de ProductDTO
    return [
        Product(
            product_id=product.sku,
            unit_name=product.unit,
            category_name=product.category,
            brand_name=product.brand,
            quantity=product.quantity,
            cost_price=product.cost_price,
            selling_price=product.selling_price,
            reorder_level=product.reorder_level
        ) for product in results
    ]


def _create_GirdView_product_cards(products: list[Product]) -> list[ft.Card]: # Crea las tarjetas de productos
    return [
        ProductCard(product=product, on_click=handle_on_card_button_click)
        for product in products
    ]


# CONTEXT ----------------------------------------------------------------------

product_controller = ProductController() # Controlador de productos

products: list[Product] # Lista de productos en la vista

searcher = ft.SearchBar( # Barra de búsqueda
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    on_tap=handle_on_tap,
    on_change=handle_on_change
)

gird_view = ft.GridView( # Vista de productos
    controls=[
        *_create_GirdView_product_cards(_wrap_productDTO_list(product_controller.get_all()))
    ],
    expand=2,
    runs_count=2,
    max_extent=500,
    child_aspect_ratio=5.5,
    spacing=1,
    run_spacing=1,
)

form_items = set()
product_form = ft.Card(
    width=350,
    height=800,
    elevation=10,
)

# SHAPE CONTENT-----------------------------------------------------------------

StoreShape = ft.ResponsiveRow( # Capa general de la vista
    [
        ft.Column( # Capa de búsqueda y productos
            [
                ft.Container( # Capa de búsqueda
                    #width=900,
                    height=50,
                    content=searcher,
                ),
                ft.Container( # Capa de productos
                    # Abarca el resto de la pantalla
                    #width=900,
                    height=800,
                    content=gird_view,
                ),
            ],
            col=8,
        ),
        ft.Container( # Capa de formulario
            #width=350,
            height=900,
            content=product_form,
            col=4,
        ),
    ]
)