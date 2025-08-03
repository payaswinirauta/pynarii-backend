from fastapi import APIRouter

router = APIRouter()

products = [
    {
        "id": 1,
        "name": "Smartwatch",
        "price": 1999,
        "category": "gadgets",
        "image_url": "assets/images/smartwatch.jpg"
    },
    {
        "id": 2,
        "name": "Wireless Headphones",
        "price": 2499,
        "category": "gadgets",
        "image_url": "assets/images/headphones.jpg"
    },
    {
        "id": 3,
        "name": "Red Casual Shirt",
        "price": 999,
        "category": "fashion",
        "image_url": "assets/images/red-shirt.jpg"
    }
]

@router.get("/products/")
def get_products():
    return products


