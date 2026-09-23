"""
Módulo: Tradutor e Comparador de Vocabulário Suíço-Alemão
Autor: Marcella Bongiolo
Descrição: Script que compara termos do Alemão Padrão (Hochdeutsch) 
           com suas equivalências no Suíço-Alemão (Schwiizertütsch).
"""

class ComparadorDialetoSuico:
    """Gerencia um dicionário de tradução entre o alemão padrão e o suíço-alemão."""
    def __init__(self):
        self.dicionario = {
            "Guten Tag": {
                "suico": "Grüezi (Zürich / Região Central)",
                "uso": "Cumprimento formal/geral"
            },
            "Kartoffel": {
                "suico": "Härdöpfel",
                "uso": "Batata"
            },
            "Mädchen": {
                "suico": "Meitschi",
                "uso": "Menina / Garota"
            },
            "Parkplatz": {
                "suico": "Parkplatz (mas usam muito 'Autopark')",
                "uso": "Estacionamento"
            },
            "Samstag": {
                "suico": "Samschtig",
                "uso": "Sábado"
            }
        }

    def traduzir_para_suico(self, termo_alemao: str) -> str:
        """Busca o termo em alemão padrão e retorna a versão suíça correspondente."""
        termo_limpo = termo_alemao.strip()
        
        if termo_limpo in self.dicionario:
            info = self.dicionario[termo_limpo]
            return (
                f"🇩🇪 Alemão Padrão: {termo_limpo}\n"
                f"🇨🇭 Suíço-Alemão: {info['suico']}\n"
                f"📖 Significado/Contexto: {info['uso']}"
            )
        else:
            return f"⚠️ O termo '{termo_alemao}' não foi encontrado no banco de dados do dialeto."

def main():
    print("=" * 60)
    print(" 🏔️ SWISS GERMAN LAB: DIALETO E CULTURA SUÍÇA 🇨🇭")
    print("=" * 60)

    comparador = ComparadorDialetoSuico()

    # Testando termos comuns
    termos_teste = ["Guten Tag", "Kartoffel", "Mädchen", "Samstag"]

    for termo in termos_teste:
        print(f"\nConsultando: '{termo}'")
        print(comparador.traduzir_para_suico(termo))
        print("-" * 40)

    print("=" * 60)

if __name__ == "__main__":
    main()
  Add Swiss German vocabulary comparator script
