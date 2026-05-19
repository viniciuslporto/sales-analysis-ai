import csv
import sys
from pathlib import Path
from datetime import datetime
import anthropic

SYSTEM_PROMPT = """Você é um analista de negócios sênior especializado em estratégia comercial e análise de dados de vendas.

Sua função é analisar dados de vendas fornecidos em formato CSV e produzir um relatório estratégico completo em português brasileiro.

O relatório deve conter:
1. **Resumo Executivo** — visão geral do desempenho e principais achados
2. **Análise de Desempenho por Produto** — quais produtos lideram em receita e volume
3. **Tendências Temporais** — evolução das vendas ao longo do período analisado
4. **Produtos em Destaque e em Alerta** — oportunidades e riscos identificados
5. **Recomendações Estratégicas** — ações concretas para aumentar receita e otimizar o portfólio

Seja direto, use linguagem executiva e fundamente cada recomendação nos dados."""


def load_csv(file_path: str) -> tuple[list[dict], str]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expected = {"date", "product", "quantity", "revenue"}
        if not expected.issubset(set(reader.fieldnames or [])):
            raise ValueError(
                f"CSV deve ter as colunas: {', '.join(expected)}. "
                f"Encontradas: {', '.join(reader.fieldnames or [])}"
            )
        for row in reader:
            rows.append(row)

    if not rows:
        raise ValueError("CSV está vazio.")

    # Build a formatted summary for the prompt
    lines = ["date,product,quantity,revenue"]
    total_revenue = 0.0
    for row in rows:
        lines.append(f"{row['date']},{row['product']},{row['quantity']},{row['revenue']}")
        total_revenue += float(row["revenue"])

    summary = "\n".join(lines)
    summary += f"\n\nTotal de registros: {len(rows)}"
    summary += f"\nReceita total bruta: R$ {total_revenue:,.2f}"
    return rows, summary


def analyze(csv_summary: str, client: anthropic.Anthropic) -> None:
    print("\n" + "=" * 60)
    print("  RELATÓRIO DE ANÁLISE ESTRATÉGICA DE VENDAS")
    print("=" * 60 + "\n")

    user_message = (
        "Analise os dados de vendas abaixo e produza o relatório estratégico completo:\n\n"
        f"```csv\n{csv_summary}\n```"
    )

    # Stream the response so long reports don't time out
    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=4096,
        thinking={"type": "adaptive"},
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},  # cache the stable system prompt
            }
        ],
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

    final = stream.get_final_message()
    usage = final.usage
    print("\n\n" + "-" * 60)
    print(f"Tokens de entrada : {usage.input_tokens:,}")
    print(f"Tokens de saída   : {usage.output_tokens:,}")
    if hasattr(usage, "cache_read_input_tokens") and usage.cache_read_input_tokens:
        print(f"Lidos do cache    : {usage.cache_read_input_tokens:,}")
    print("-" * 60)


def main():
    csv_file = sys.argv[1] if len(sys.argv) > 1 else "vendas_exemplo.csv"

    print(f"Carregando dados de: {csv_file}")
    try:
        rows, csv_summary = load_csv(csv_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"{len(rows)} registros carregados. Enviando para análise...")

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment
    analyze(csv_summary, client)


if __name__ == "__main__":
    main()
