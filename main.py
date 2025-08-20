from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:63342",
    "http://127.0.0.1:63342",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for testing only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    {"id": 1, "name": "Smartwatch", "price": 1999, "category": "gadgets", "image": "assets/images/smartwatch.jpg"},
    {"id": 2, "name": "Wireless Headphones", "price": 2499, "category": "gadgets", "image": "assets/images/headphones.jpg"},
    {"id": 3, "name": "Red Casual Shirt", "price": 999, "category": "fashion", "image": "assets/images/red-shirt.jpg"},
]

@app.get("/products/")
async def get_products():
    return products


@app.get("/")
async def read_root():
    return {"message": "Pynarii Backend is running successfully!"}
