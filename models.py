from pydantic import BaseModel
from typing import List
from decimal import Decimal

class Card(BaseModel):
    card_number: str
    expiration_date: str
    cvv: str
    balance: Decimal  # Saldo do cartão

class User(BaseModel):
    name: str
    cpf: str  # CPF como identificador único
    email: str
    cards: List[Card] = []
