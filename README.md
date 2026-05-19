# Sales Analysis Automation with Claude AI

> Transform raw sales data into executive-ready strategic insights in seconds — powered by Anthropic's Claude AI.

---

## What This Project Does

This tool reads a CSV file containing sales records and automatically generates a **full strategic business report** using Claude AI. Instead of spending hours in spreadsheets, business analysts and managers get actionable insights delivered instantly via the command line.

The generated report covers:

- **Executive Summary** — overall performance and key findings
- **Product Performance Analysis** — revenue and volume leaders
- **Temporal Trends** — how sales evolved over the analyzed period
- **Highlights & Alerts** — growth opportunities and risk signals
- **Strategic Recommendations** — concrete actions to increase revenue and optimize the product portfolio

---

## The Problem It Solves

Most small and mid-sized companies have sales data trapped in spreadsheets — valuable raw numbers that never get turned into decisions. Hiring a business analyst is expensive. Building BI dashboards takes weeks.

This project bridges that gap: a single Python script takes a CSV export from any ERP or e-commerce platform and delivers a C-level quality strategic analysis in under 30 seconds, at the cost of a single API call.

---

## Technologies Used

| Technology | Role |
|---|---|
| **Python 3.11+** | Core scripting and CSV processing |
| **Anthropic Claude API** | AI-powered strategic analysis (claude-opus-4-7) |
| **Streaming API** | Real-time output — no waiting for the full response |
| **Prompt Caching** | System prompt cached to reduce latency and token costs on repeated runs |
| **Adaptive Thinking** | Claude reasons step-by-step before writing the report for higher accuracy |

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/viniciuslporto/sales-analysis-claude.git
cd sales-analysis-claude
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
.venv\Scripts\activate          # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set your Anthropic API key**

```bash
export ANTHROPIC_API_KEY="your-api-key-here"   # macOS/Linux
set ANTHROPIC_API_KEY=your-api-key-here        # Windows
```

> Get your API key at [console.anthropic.com](https://console.anthropic.com).

---

## How to Run

**Using the included sample data:**

```bash
python analisar_vendas.py
```

**Using your own CSV file:**

```bash
python analisar_vendas.py path/to/your/sales_data.csv
```

**Required CSV format:**

```csv
date,product,quantity,revenue
2024-01-05,Product Name,12,3599.00
2024-01-08,Another Product,45,445.50
```

The columns `date`, `product`, `quantity`, and `revenue` are required. The script validates the file before sending it to the API and exits with a clear error message if anything is wrong.

---

## Example Output

```
============================================================
  SALES STRATEGIC ANALYSIS REPORT
============================================================

## Executive Summary

In the January–April 2024 period, the portfolio generated R$ 402,541.00 in
total revenue across 26 transactions...

## Product Performance Analysis

Notebook Pro leads with R$ 182,939.00 (45.4% of total revenue) despite
representing only 4 SKUs — a premium concentration risk worth monitoring...

## Temporal Trends

March 2024 was the strongest month at R$ 153,207.00, driven by a 22% surge
in Notebook Pro sales and the full-cycle contribution of Headset Gamer...

## Strategic Recommendations

1. **Protect the Notebook Pro margin** — it drives nearly half of revenue.
   Introduce a protection plan or accessories bundle to increase average ticket.
2. **Accelerate Mouse Sem Fio volume** — fastest-growing SKU by units (45 → 112).
   Consider a bulk discount tier for B2B buyers...

------------------------------------------------------------
Input tokens  : 1,842
Output tokens : 1,205
Cache reads   : 312
------------------------------------------------------------
```

---

## Project Structure

```
.
├── analisar_vendas.py     # Main script
├── vendas_exemplo.csv     # Sample sales data (Jan–Apr 2024)
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Business Value for Companies

### For Sales & Commercial Teams
Eliminate the delay between closing a sales period and understanding what happened. Run an analysis after any export — daily, weekly, or monthly — and walk into every review meeting with data-backed talking points.

### For Operations & Finance
Spot underperforming products before they become a problem. The AI flags items entering a downward trend and recommends reallocation or promotional actions before margin erosion accelerates.

### For Leadership & Executives
Turn a raw spreadsheet into a board-ready narrative in under a minute. No analyst bottleneck, no waiting for the BI team to build a new report, no manual interpretation.

### ROI Snapshot

| Traditional Approach | This Tool |
|---|---|
| 2–4 hours of analyst time | ~30 seconds |
| Manual, subjective interpretation | Data-grounded, consistent AI reasoning |
| Report available next day | Report available immediately |
| Requires BI tool license | Single low-cost API call |

### Adaptability
The system prompt and CSV schema are fully configurable. This same architecture can be adapted to analyze:
- Customer churn data
- Marketing campaign performance
- Inventory turnover
- Support ticket trends

Any structured tabular data can become a strategic report with minimal modifications.

---

## Author

**Vinicius Porto**
Building AI-powered automation tools that turn data into decisions.

- Email: lportovinicius@gmail.com
- GitHub: [github.com/viniciuslporto](https://github.com/viniciuslporto)

---

## License

MIT — free to use, modify, and distribute.
