
import tkinter as tk
from tkinter import messagebox

from operacoes import Soma, Subtracao, Multiplicacao, Divisao


class CalculadoraApp:
    def __init__(self, calculadora):
        self.calculadora = calculadora

        self.janela = tk.Tk()
        self.janela.title("Calculadora POO")
        self.janela.geometry("430x570")
        self.janela.resizable(False, False)

        self._criar_interface()

    def _criar_interface(self):

        tk.Label(
            self.janela,
            text="CALCULADORA POO",
            font=("Arial", 18, "bold")
        ).pack(pady=18)

        tk.Label(
            self.janela,
            text="Primeiro número"
        ).pack()

        self.entrada1 = tk.Entry(
            self.janela,
            justify="center",
            font=("Arial", 13)
        )
        self.entrada1.pack(pady=6)

        tk.Label(
            self.janela,
            text="Segundo número"
        ).pack()

        self.entrada2 = tk.Entry(
            self.janela,
            justify="center",
            font=("Arial", 13)
        )
        self.entrada2.pack(pady=6)

        botoes = tk.Frame(self.janela)
        botoes.pack(pady=12)

        operacoes = [
            ("Somar +", Soma, "+"),
            ("Subtrair -", Subtracao, "-"),
            ("Multiplicar *", Multiplicacao, "*"),
            ("Dividir /", Divisao, "/")
        ]

        for texto, classe, simbolo in operacoes:
            tk.Button(
                botoes,
                text=texto,
                width=16,
                height=2,
                command=lambda c=classe, s=simbolo:
                    self._calcular(c, s)
            ).pack(pady=3)

        self.resultado = tk.Label(
            self.janela,
            text="Resultado:",
            font=("Arial", 14, "bold")
        )
        self.resultado.pack(pady=12)

        acoes = tk.Frame(self.janela)
        acoes.pack(pady=5)

        tk.Button(
            acoes,
            text="Limpar campos",
            command=self._limpar_campos
        ).pack(side="left", padx=5)

        tk.Button(
            acoes,
            text="Limpar histórico",
            command=self._limpar_historico
        ).pack(side="left", padx=5)

        tk.Label(
            self.janela,
            text="Histórico de cálculos",
            font=("Arial", 11, "bold")
        ).pack(pady=(14, 4))

        quadro = tk.Frame(self.janela)
        quadro.pack(fill="both", expand=True, padx=18)

        self.lista = tk.Listbox(
            quadro,
            height=8,
            font=("Consolas", 10)
        )

        barra = tk.Scrollbar(
            quadro,
            orient="vertical",
            command=self.lista.yview
        )

        self.lista.configure(
            yscrollcommand=barra.set
        )

        self.lista.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

    def _calcular(self, classe_operacao, simbolo):
        try:
            primeiro = float(
                self.entrada1.get().replace(",", ".")
            )

            segundo = float(
                self.entrada2.get().replace(",", ".")
            )

            operacao = classe_operacao(primeiro, segundo)

            resultado = self.calculadora.calcular(
                operacao,
                simbolo
            )

            self.resultado.config(
                text=f"Resultado: {resultado:g}"
            )

            self._atualizar_historico()

        except ValueError as erro:
            mensagem = str(erro)

            if "zero" in mensagem.lower():
                messagebox.showerror("Erro", mensagem)
            else:
                messagebox.showerror(
                    "Entrada inválida",
                    "Digite dois números válidos."
                )

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Ocorreu um erro: {erro}"
            )

    def _atualizar_historico(self):
        self.lista.delete(0, tk.END)

        for registro in self.calculadora.obter_historico():
            self.lista.insert(tk.END, registro)

    def _limpar_campos(self):
        self.entrada1.delete(0, tk.END)
        self.entrada2.delete(0, tk.END)

        self.resultado.config(
            text="Resultado:"
        )

    def _limpar_historico(self):
        self.calculadora.limpar_historico()
        self._atualizar_historico()

    def executar(self):
        self.janela.mainloop()
