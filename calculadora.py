
from historico import Historico


class Calculadora:
    def __init__(self):
        self._historico = Historico()

    def calcular(self, operacao, simbolo):
        resultado = operacao.executar()

        expressao = (
            f"{operacao.primeiro:g} {simbolo} "
            f"{operacao.segundo:g} = {resultado:g}"
        )

        self._historico.adicionar(expressao)

        return resultado

    def obter_historico(self):
        return self._historico.listar()

    def limpar_historico(self):
        self._historico.limpar()
