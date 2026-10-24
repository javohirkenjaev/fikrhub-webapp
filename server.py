from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI(title="FikrHub API", description="FikrHub platformasi uchun tashqi server", version="1.0")

# Frontend ulanishi uchun CORS ruxsatlari
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Barcha saytlardan ulanishga ruxsat (GitHub Pages uchun)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ma'lumotlar modeli (Do'kon strukturasi)
class Shop(BaseModel):
    id: str = None
    name: str
    category: str
    description: str
    contact: str
    is_vip: bool = False

# Vaqtinchalik ma'lumotlar bazasi (RAM)
db_shops = [
    Shop(id=str(uuid.uuid4()), name="TechMarket Uz", category="Elektronika", description="Eng so'nggi noutbuk va smartfonlar arzon narxlarda.", contact="@tech_admin", is_vip=True),
    Shop(id=str(uuid.uuid4()), name="FastBurger", category="Ovqatlanish", description="Mazali fast-food va tezkor yetkazib berish xizmati.", contact="@burger_uz", is_vip=False)
]

@app.get("/api/shops", response_model=List[Shop])
async def get_all_shops():
    """Barcha do'konlarni qaytaradi, VIP do'konlar birinchi chiqadi"""
    return sorted(db_shops, key=lambda x: x.is_vip, reverse=True)

@app.get("/api/shops/search", response_model=List[Shop])
async def search_shops(query: str):
    """Kiritilgan so'z bo'yicha do'konlarni qidirish"""
    results = [shop for shop in db_shops if query.lower() in shop.name.lower() or query.lower() in shop.description.lower()]
    return results

@app.post("/api/shops", response_model=Shop)
async def create_shop(shop: Shop):
    """Yangi do'kon qo'shish"""
    shop.id = str(uuid.uuid4())
    db_shops.append(shop)
    return shop

if __name__ == "__main__":
    import uvicorn
    # Serverni mahalliy kompyuterda ishga tushirish: python server.py
    uvicorn.run(app, host="0.0.0.0", port=8000)