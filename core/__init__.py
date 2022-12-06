import datetime


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos.'.format(now.hour, now.minute)
        return answer

    def get_data():
        now = datetime.datetime.now()
        answer = "hojé é dia {}, do {} de {}".format(now.day, now.month, now.year)
        return answer


class Pessoa:

    def __init__(self):
        pass

    @staticmethod
    def get_nome():
        answer = 'olá, meu nome é Otto'
        return answer
