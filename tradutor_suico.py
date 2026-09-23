"""Comparador de vocabulário entre alemão padrão e suíço-alemão.

O projeto é educacional e apresenta exemplos de vocabulário associados ao
alemão suíço. As formas podem variar entre regiões e dialetos.
"""

VOCABULARIO = {
    "Guten Tag": {
        "suico": "Grüezi",
        "uso": "Cumprimento comum/formal",
    },
    "Kartoffel": {
        "suico": "Härdöpfel",
        "uso": "Batata",
    },
    "Mädchen": {
        "suico": "Meitschi",
        "uso": "Menina / garota",
    },
    "Parkplatz": {
        "suico": "Parkplatz",
        "uso": "Estacionamento",
    },
    "Samstag": {
        "suico": "Samschtig",
        "uso": "Sábado",
    },
}


class ComparadorDialetoSuico:
    """Consulta exemplos de vocabulário em alemão suíço."""

    def __init__(self, dicionario=None):
        self.dicionario = dicionario if dicionario is not None else VOCABULARIO.copy()

    def traduzir_para_suico(self, termo_alemao: str) -> str:
        """Retorna uma comparação formatada para um termo conhecido."""
        termo_limpo = termo_alemao.strip()

        if not termo_limpo:
            raise ValueError("O termo não pode estar vazio.")

        info = self.dicionario.get(termo_limpo)
        if info is None:
            return (
                f"O termo '{termo_limpo}' não foi encontrado no banco "
                "de exemplos."
            )

        return (
            f"Alemão Padrão: {termo_limpo}\n"
            f"Suíço-Alemão: {info['suico']}\n"
            f"Contexto: {info['uso']}"
        )


def main() -> None:
    """Executa uma demonstração do comparador."""
    comparador = ComparadorDialetoSuico()
    termos_teste = ["Guten Tag", "Kartoffel", "Mädchen", "Samstag"]

    print("=" * 60)
    print("SWISS GERMAN LAB")
    print("=" * 60)

    for termo in termos_teste:
        print(f"\nConsultando: '{termo}'")
        print(comparador.traduzir_para_suico(termo))
        print("-" * 40)


if __name__ == "__main__":
    main()
