"""
RentSmart - Sistema de Orcamento de Locacao
R.M Imoveis

Disciplina: Algorithmic Thinking & Introduction to Object-Oriented Programming

Como executar:
    python main.py

O programa pergunta os dados da locacao no terminal, calcula o orcamento
mensal e gera o arquivo 'projecao_12_meses.csv' na pasta atual.
"""

import csv


class Imovel:
    """Classe base que representa um imovel disponivel para locacao."""

    def __init__(self, tipo: str, aluguel_base: float):
        self.tipo = tipo
        self.aluguel_base = aluguel_base

    def calcular_aluguel(self) -> float:
        """Calcula o aluguel mensal com os adicionais do imovel."""
        return self.aluguel_base

    def resumo_adicionais(self) -> str:
        return "Nenhum adicional"


class Apartamento(Imovel):
    """Apartamento: base R$ 700,00. +2 quartos: R$ 200,00.
    Garagem: R$ 300,00. Sem criancas: 5% de desconto sobre o aluguel."""

    ADICIONAL_SEGUNDO_QUARTO = 200.0
    VALOR_GARAGEM = 300.0
    DESCONTO_SEM_CRIANCAS = 0.05

    def __init__(self, quartos: int, garagem: bool, sem_criancas: bool):
        super().__init__("Apartamento", 700.0)
        self.quartos = quartos
        self.garagem = garagem
        self.sem_criancas = sem_criancas

    def calcular_aluguel(self) -> float:
        aluguel = self.aluguel_base
        if self.quartos == 2:
            aluguel += self.ADICIONAL_SEGUNDO_QUARTO
        if self.garagem:
            aluguel += self.VALOR_GARAGEM
        if self.sem_criancas:
            aluguel -= aluguel * self.DESCONTO_SEM_CRIANCAS
        return aluguel

    def resumo_adicionais(self) -> str:
        itens = []
        if self.quartos == 2:
            itens.append(f"2o quarto: +R$ {self.ADICIONAL_SEGUNDO_QUARTO:.2f}")
        if self.garagem:
            itens.append(f"Garagem: +R$ {self.VALOR_GARAGEM:.2f}")
        if self.sem_criancas:
            itens.append("Desconto sem criancas: -5%")
        return "; ".join(itens) if itens else "Nenhum adicional"


class Casa(Imovel):
    """Casa: base R$ 900,00. +2 quartos: R$ 250,00. Garagem: R$ 300,00."""

    ADICIONAL_SEGUNDO_QUARTO = 250.0
    VALOR_GARAGEM = 300.0

    def __init__(self, quartos: int, garagem: bool):
        super().__init__("Casa", 900.0)
        self.quartos = quartos
        self.garagem = garagem

    def calcular_aluguel(self) -> float:
        aluguel = self.aluguel_base
        if self.quartos == 2:
            aluguel += self.ADICIONAL_SEGUNDO_QUARTO
        if self.garagem:
            aluguel += self.VALOR_GARAGEM
        return aluguel

    def resumo_adicionais(self) -> str:
        itens = []
        if self.quartos == 2:
            itens.append(f"2o quarto: +R$ {self.ADICIONAL_SEGUNDO_QUARTO:.2f}")
        if self.garagem:
            itens.append(f"Garagem: +R$ {self.VALOR_GARAGEM:.2f}")
        return "; ".join(itens) if itens else "Nenhum adicional"


class Estudio(Imovel):
    """Estudio: base R$ 1.200,00. Pacote de 2 vagas: R$ 250,00.
    Vaga adicional: R$ 60,00 cada."""

    PACOTE_DUAS_VAGAS = 250.0
    VAGA_ADICIONAL = 60.0

    def __init__(self, vagas: int):
        super().__init__("Estudio", 1200.0)
        self.vagas = vagas  # 0 = sem estacionamento

    def calcular_aluguel(self) -> float:
        aluguel = self.aluguel_base
        if self.vagas > 0:
            aluguel += self.PACOTE_DUAS_VAGAS
            if self.vagas > 2:
                aluguel += (self.vagas - 2) * self.VAGA_ADICIONAL
        return aluguel

    def resumo_adicionais(self) -> str:
        if self.vagas == 0:
            return "Nenhum adicional"
        adicional = self.PACOTE_DUAS_VAGAS + max(0, self.vagas - 2) * self.VAGA_ADICIONAL
        return f"Estacionamento ({self.vagas} vaga(s)): +R$ {adicional:.2f}"


class Contrato:
    """Representa a taxa contratual fixa de R$ 2.000,00, que pode ser
    parcelada em ate 5 vezes. E um custo separado do aluguel mensal."""

    TAXA_CONTRATUAL = 2000.0
    MAX_PARCELAS = 5

    def __init__(self, parcelas: int):
        if not 1 <= parcelas <= self.MAX_PARCELAS:
            raise ValueError("Parcelas devem estar entre 1 e 5.")
        self.parcelas = parcelas

    @property
    def valor_parcela(self) -> float:
        return self.TAXA_CONTRATUAL / self.parcelas


class Orcamento:
    """Monta o orcamento a partir de um imovel e um contrato, exibe o
    resumo detalhado e gera o CSV com a projecao de 12 meses."""

    def __init__(self, imovel: Imovel, contrato: Contrato):
        self.imovel = imovel
        self.contrato = contrato
        self.aluguel_mensal = imovel.calcular_aluguel()
        self.total_12_meses = self.aluguel_mensal * 12 + Contrato.TAXA_CONTRATUAL

    def exibir_resumo(self) -> None:
        print("\n========== ORCAMENTO RENTSMART ==========")
        print(f"Imovel:            {self.imovel.tipo}")
        print(f"Aluguel-base:      R$ {self.imovel.aluguel_base:.2f}")
        print(f"Adicionais:        {self.imovel.resumo_adicionais()}")
        print("-" * 42)
        print(f"ALUGUEL MENSAL:    R$ {self.aluguel_mensal:.2f}")
        print("-" * 42)
        print(f"Taxa contratual:   R$ {Contrato.TAXA_CONTRATUAL:.2f} "
              f"(a parte do aluguel)")
        print(f"Parcelamento:      {self.contrato.parcelas}x de "
              f"R$ {self.contrato.valor_parcela:.2f}")
        print("-" * 42)
        print(f"TOTAL 12 MESES:    R$ {self.total_12_meses:.2f} "
              f"(12x aluguel + taxa)")
        print("=========================================\n")

    def gerar_csv(self, nome_arquivo: str = "projecao_12_meses.csv") -> None:
        """Gera o CSV com a projecao dos 12 meses da locacao."""
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["Mes", "Aluguel (R$)",
                               "Parcela da taxa (R$)", "Total do mes (R$)"])
            for mes in range(1, 13):
                parcela = (
                    self.contrato.valor_parcela if mes <= self.contrato.parcelas
                    else 0.0
                )
                escritor.writerow([mes,
                                   f"{self.aluguel_mensal:.2f}",
                                   f"{parcela:.2f}",
                                   f"{self.aluguel_mensal + parcela:.2f}"])
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso!\n")


# ---------------------- Funções de entrada e validação ----------------------

def perguntar_opcao(msg: str, opcoes_validas) -> str:
    """Pergunta ate o usuario digitar uma opcao valida."""
    while True:
        resposta = input(msg).strip().upper()
        if resposta in opcoes_validas:
            return resposta
        print(f"Opcao invalida. Digite uma das opcoes: {', '.join(opcoes_validas)}")


def perguntar_inteiro(msg: str, minimo: int, maximo: int) -> int:
    """Pergunta ate o usuario digitar um numero inteiro no intervalo."""
    while True:
        try:
            valor = int(input(msg).strip())
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")


def escolher_imovel() -> Imovel:
    """Monta o imovel escolhido pelo usuario, aplicando as regras de cada tipo."""
    tipo = perguntar_opcao(
        "Tipo de imovel - (A)partamento, (C)asa ou (E)studio: ",
        {"A", "C", "E"},
    )

    if tipo in ("A", "C"):
        quartos = perguntar_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)
        garagem = perguntar_opcao("Deseja vaga de garagem? (S/N): ", {"S", "N"}) == "S"
        if tipo == "A":
            sem_criancas = perguntar_opcao(
                "Sem criancas na residencia (5% de desconto)? (S/N): ",
                {"S", "N"},
            ) == "S"
            return Apartamento(quartos, garagem, sem_criancas)
        return Casa(quartos, garagem)

    vagas = perguntar_inteiro(
        "Vagas de estacionamento (0 a 5): ", 0, 5
    )
    return Estudio(vagas)


def main() -> None:
    print("=" * 42)
    print("   RENTSMART - Orcamento de Locacao")
    print("   R.M Imoveis")
    print("=" * 42)

    imovel = escolher_imovel()

    parcelas = perguntar_inteiro(
        "Em quantas parcelas pagar a taxa contratual de R$ 2.000,00 (1 a 5): ",
        1, Contrato.MAX_PARCELAS,
    )
    contrato = Contrato(parcelas)

    orcamento = Orcamento(imovel, contrato)
    orcamento.exibir_resumo()
    orcamento.gerar_csv()


if __name__ == "__main__":
    main()