from datetime import date
from pydantic import BaseModel

class Dados(BaseModel):
    escolha: str
    data_inicio: date
    data_fim: date