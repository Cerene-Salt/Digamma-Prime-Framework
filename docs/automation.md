Here we go, Cesar — next up is **`automation.md`**, your guide to making Digamma Prime usable in real-world workflows: CLI, CI pipelines, VS Code, and automated reports. This is where symbolic metrics become operational tools.

---

## ⚙️ `docs/automation.md`

```markdown
# ⚙️ Automation & CLI Guide

Digamma-Prime is designed to be **automatable** — so you can monitor drift, audit models, and trigger alerts without touching the math.

---

## 🧰 Command-Line Usage

Compare two prediction files:

```bash
$ digamma compare --base baseline.csv --new new.csv --out report.json
```

This computes:

- φ (structural divergence)
- Δφ (rate divergence)
- Bootstrap confidence intervals
- Verdict: drift / no drift

---

## 🧪 Example Output

```json
{
  "phi": 10.34,
  "delta_phi": 2.44,
  "phi_bootstrap": { "ci_lo": 8.9, "ci_hi": 11.8 },
  "delta_bootstrap": { "ci_lo": 2.0, "ci_hi": 3.1 },
  "verdict": "significant drift"
}
```

---

## 🧵 VS Code Task

Add this to `.vscode/tasks.json`:

```json
{
  "label": "Run Digamma Audit",
  "type": "shell",
  "command": "python digamma_cli.py --base baseline.csv --new new.csv"
}
```

Now analysts can run audits with one click.

---

## 🔁 GitHub Action Snippet

Use Digamma-Prime as a CI gate:

```yaml
- name: Run Digamma Drift Check
  run: |
    python -m epe_maria.cli compare --base baseline.csv --new new.csv
```

Fail the check if φ exceeds threshold.

---

## 📈 Automated Reports

Every CLI run can generate:

- φ and Δφ values  
- Bootstrap confidence intervals  
- Two plots: φ vs shift, Δφ vs shift  
- Verdict summary  
- Optional PDF or HTML export

---

## 🚨 Thresholding Logic

```python
if phi > 10 or phi_ci['ci_lo'] > 2:
    alert("Model drift detected (φ = {:.2f})".format(phi))
```

Tune thresholds using historical “no-drift” windows.

---

## 🧠 Use Cases

- Daily drift monitoring  
- Retrain audits  
- CI/CD gates  
- Slack/Email alerts  
- Model card snapshots

---

## 🧩 Integration Targets

| Platform     | Integration Type         |
|--------------|---------------------------|
| GitHub       | CI gate for retrains      |
| Airflow      | DAG task for drift check  |
| MLflow       | Custom metric plugin      |
| Prometheus   | Metric exporter           |
| Streamlit    | Interactive dashboard     |

