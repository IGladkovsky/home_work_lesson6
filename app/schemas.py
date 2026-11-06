from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class SizeEnum(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    BIG = "big"


class StatusEnum(str, Enum):
    PENDING = "pending"
    READY = "ready"
    COMPLETED = "completed"


class OrderCreate(BaseModel):
    drink: str = Field(min_length=1, max_length=100, description="Название напитка", examples=["Espresso", "Latte"])
    size: SizeEnum = Field(description="Размер напитка", examples=["small", "medium", "big"])
    quantity: int = Field(gt=0, lt=100, description="Количество напитков", examples=[1, 5])
    customer_name: Optional[str] = Field(default=None, min_length=1, max_length=100, description="Имя заказчика",
                                         examples=["Customer"])


class Order(BaseModel):
    id: int = Field(description="ID заказа", examples=[1, 2])
    drink: str = Field(min_length=1, max_length=100, description="Название напитка", examples=["Espresso", "Latte"])
    size: SizeEnum = Field(description="Размер напитка", examples=["small", "medium", "big"])
    quantity: int = Field(gt=0, lt=100, description="Количество напитков", examples=[1, 5])
    customer_name: Optional[str] = Field(default=None, min_length=1, max_length=100, description="Имя заказчика",
                                         examples=["Customer"])
    status: StatusEnum = Field(default=StatusEnum.PENDING, description="Статус заказа", examples=["pending", "ready"])
    created_at: datetime = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0),
        description="Время создания заказа", examples=["2026-10-31T10:38:43"]
    )


class OrderUpdate(BaseModel):
    drink: Optional[str] = Field(default=None, min_length=1, max_length=100, description="Название напитка",
                                 examples=["Espresso", "Latte"])
    size: Optional[SizeEnum] = Field(default=None, description="Размер напитка", examples=["small", "medium", "big"])
    quantity: Optional[int] = Field(default=None, gt=0, lt=100, description="Количество напитков", examples=[1, 5])
    customer_name: Optional[str] = Field(default=None, min_length=1, max_length=100, description="Имя заказчика",
                                         examples=["Customer"])
    status: Optional[StatusEnum] = Field(default=None, description="Статус заказа",
                                         examples=["pending", "ready", "completed"])
