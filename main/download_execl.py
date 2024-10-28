import openpyxl
from django.http import HttpResponse
import os
from tempfile import NamedTemporaryFile
from product.models import Product


def export_products(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Product List'

    ws.append(['Title', 'Quantity', 'Price', 'Description'])

    products = Product.objects.all()

    for product in products:
        ws.append([product.title, product.qty, product.price, product.description])

    with NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        wb.save(tmp.name)
        tmp.seek(0)

        with open(tmp.name, 'rb') as output:
            response = HttpResponse(
                output.read(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = 'attachment; filename="products.xlsx"'

    os.remove(tmp.name)

    return response
