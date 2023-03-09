from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.data_formatada()

    def mes_cadastro(self):
        meses_do_ano =["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
                       "outubro", "novembro", "dezembro"]
        mes_castro = self.momento_cadastro.month
        return meses_do_ano[mes_castro-1]
    def dia_semana(self):
        dia_da_semana = ["segunda", "terça","quarta", "quinta", "quinta", "sexta","sabado","domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dia_da_semana[dia_semana]
    
    def data_formatada(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro