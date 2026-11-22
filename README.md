# RentSmart — Sistema de Orçamento de Locação

Aplicação em Python (Programação Orientada a Objetos) que calcula orçamentos mensais de locação para a **R.M Imóveis** e gera um arquivo CSV com a projeção dos 12 meses da locação.

## 📋 Requisitos

- Python 3.10 ou superior (não usa bibliotecas externas, apenas a biblioteca padrão `csv`).

## ▶️ Como executar

1. Salve o arquivo `main.py` em uma pasta do seu computador.
2. Abra o terminal nessa pasta.
3. Execute:

```bash
python main.py
```

(Em alguns sistemas: `python3 main.py`.)

4. Responda às perguntas no terminal:

| Pergunta | Valores aceitos |
| --- | --- |
| Tipo de imóvel | A (Apartamento), C (Casa), E (Estúdio) |
| Quartos (apto/casa) | 1 ou 2 |
| Garagem (apto/casa) | S ou N |
| Sem crianças (apto) | S ou N (5% de desconto) |
| Vagas de estacionamento (estúdio) | 0 a 5 |
| Parcelas da taxa contratual | 1 a 5 |

5. Ao final, o programa mostra o resumo do orçamento e gera o arquivo **`projecao_12_meses.csv`** na mesma pasta.

## 🧮 Regras de cálculo

| Item | Valor |
| --- | --- |
| Apartamento 1 quarto | R$ 700,00 |
| Casa 1 quarto | R$ 900,00 |
| Estúdio | R$ 1.200,00 |
| Apartamento 2 quartos | + R$ 200,00 |
| Casa 2 quartos | + R$ 250,00 |
| Garagem (apto/casa) | + R$ 300,00 |
| Estúdio: pacote de 2 vagas | + R$ 250,00 |
| Vaga adicional do estúdio | + R$ 60,00 |
| Apartamento sem crianças | − 5% sobre o aluguel |
| Taxa contratual | R$ 2.000,00, em até 5 parcelas (separada do aluguel) |

## 🏛️ Estrutura de classes

- `Imovel` (classe base): tipo e aluguel-base.
- `Apartamento`, `Casa`, `Estudio`: herdam de `Imovel` e sobrescrevem `calcular_aluguel()` com suas regras (adicionais, garagem, vagas, desconto).
- `Contrato`: taxa contratual de R$ 2.000,00 e parcelamento (1 a 5).
- `Orcamento`: combina imóvel + contrato, exibe o resumo detalhado e gera o CSV dos 12 meses.

## 📄 Exemplo de saída (CSV)

```
Mes,Aluguel (R$),Parcela da taxa (R$),Total do mes (R$)
1,950.00,400.00,1350.00
2,950.00,400.00,1350.00
...
6,950.00,0.00,950.00
...
12,950.00,0.00,950.00
```
```
