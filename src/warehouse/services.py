from src.warehouse.models import Product


class ListProductsServices:
    def __init__(self):
        self.product_model: Product = Product()


    def list_all_products(self):
        return self.product_model.query.all()