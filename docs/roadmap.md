

## 🧭 `docs/roadmap.md`

```markdown
# 🧭 Roadmap

Digamma-Prime is growing from a symbolic audit tool into a full visual and operational framework.  
This roadmap outlines upcoming features, phases, and contribution opportunities.

---

## 📅 Development Phases

| Phase        | Goal                                      | ETA        |
|--------------|-------------------------------------------|------------|
| Short term   | Visual kit (Matplotlib/Plotly)            | Q4 2025    |
| Mid term     | Interactive dashboard (Streamlit)         | Q1 2026    |
| Long term    | Tensorized φ for embeddings               | Q2 2026    |
| Future       | REST API, Prometheus exporter, AutoML gate| Q3–Q4 2026 |

---

## 🔧 Upcoming Features

- `dp.visuals`: plot φ and Δφ curves, surface comparisons  
- `dp.compare(…, visualize=True)`: toggle visual output  
- `dp.report()`: generate HTML/PDF audit summaries  
- `phi_tensor()`: symbolic divergence for multi-dimensional outputs  
- `phi_posterior()`: uncertainty-aware φ for probabilistic models  
- `dp.dashboard`: Streamlit app for CSV/model uploads and instant drift check

---

## 🤝 Contributing

We welcome contributions in:

- 📘 Tutorials and notebooks  
- 🧪 New metrics and symbolic extensions  
- 🧬 Domain-specific case studies  
- 🧰 CLI improvements and automation scripts  
- 🎨 Visualizations and dashboard components

---

## 🧪 Setup for Contributors

```bash
git clone https://github.com/epe-team/digamma-ep
pip install -e .
pytest
```

Use `docs/style_guide.md` for formatting and terminology rules.

---

## 🌍 Vision

Digamma-Prime aims to become:

- A **symbolic standard** for model comparison  
- A **visual language** for drift and integrity  
- A **trusted tool** for audits, monitoring, and education

Whether you're a researcher, engineer, or student — you can help shape the future of symbolic ML.
