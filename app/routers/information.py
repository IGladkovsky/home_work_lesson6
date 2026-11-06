from fastapi import APIRouter
from app.dependencies import SettingsDep, ServiceDep

router = APIRouter(tags=["Сервис"])

@router.get("/", summary="Приветственная страница")
async def hello_page(settings: SettingsDep):
    return {"message": f"Приветствую в FastAPI нашей кофейни {settings.app_name}"}

@router.get("/info", summary="Информация о количестве заказов и название сервиса")
async def info_page(service : ServiceDep, settings: SettingsDep):
    return {
        "service_name": settings.app_name,
        "count": service.count_orders(),
    }