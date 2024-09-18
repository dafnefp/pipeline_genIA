from datetime import date
from pydantic import BaseModel, model_validator

class Dados(BaseModel):
    """
    Modelo de dados para informação de ações.

    Args:
        escolha (Str): código da ação
        data_inicio (date): data inicial do período das informações
        data_fim (date): data final do período das informações
    """

    escolha: str
    data_inicio: date
    data_fim: date

    @model_validator (mode='after')
    def check_date(self):
        if self.data_inicio >= self.data_fim:
            raise ValueError('A data inicial precisa ser anterior a data final')
        elif self.data_fim > date.today():
            raise ValueError('A data final precisa ser menor ou igual a data atual')
        return self