# 🔗 TrustChain — Autonomous Supplier Sustainability Agent

![Stack](https://img.shields.io/badge/stack-Python%20%7C%20LangGraph%20%7C%20IBM%20Granite-blue)
![Status](https://img.shields.io/badge/status-prototype-success)

> An AI agent that autonomously ingests supplier documents, extracts sustainability evidence (carbon footprint, fair-labor certifications, ESG disclosures), validates it, and generates a **Trust Score**.

---

## The problem

Procurement teams drown in supplier PDFs — ISO certs, carbon reports, labour audit letters, scope-3 disclosures. A human analyst would need days per supplier. TrustChain does it in minutes, **with receipts**: every claim traces back to the paragraph it came from.

---

## How it works

1. **Ingest** — drop in a supplier's document pack (PDFs, emails, images)
2. **Parse** — Docling extracts clean structured content from messy documents
3. **Verify** — IBM Granite cross-references claims against known certifying bodies
4. **Score** — weighted rubric produces a Trust Score (0–100) with subscores for environment, labour, governance
5. **Explain** — every point in the score links back to a source paragraph

---

## Stack

| Component | Tech |
| :--- | :--- |
| Orchestration | LangChain · LangGraph |
| Document parsing | Docling |
| Intelligence | IBM Granite via watsonx.ai |
| Validation | Pydantic |

---

## Quick start

```bash
git clone https://github.com/ChumaMike/TrustChain-agent.git
cd TrustChain-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Configure
cp .env.example .env
# Set WATSONX_API_KEY, WATSONX_PROJECT_ID

# Run on the sample invoice
python main.py --input sample_invoice.md
```

See `sample_invoice.md` for the expected document shape.

---

## Tests

```bash
pytest
```

---

## 🗺️ Roadmap

- [ ] OCR pipeline for scanned certificates
- [ ] Live verification against the South African B-BBEE registry
- [ ] Webhook API for procurement platforms (Ariba, Coupa)
- [ ] Multi-language support (French, Portuguese for African suppliers)

---

## License

MIT · Built by [Chuma Meyiswa](https://github.com/ChumaMike)
