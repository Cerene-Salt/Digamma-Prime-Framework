# 📘 Glossary

This glossary defines all symbolic terms used in Digamma-Prime.  
Use it to stay consistent across code, docs, and presentations.

---

| Term                  | Description                                      | Symbol / Function     |
|-----------------------|--------------------------------------------------|------------------------|
| **Structural divergence** | Average output difference between functions | φ / `phi(f, g)`        |
| **Rate divergence**       | Difference in slopes or curvature            | Δφ / `delta_phi(f, g)` |
| **Fusion metric**         | Weighted blend of φ and Δφ                   | φ* / `phi_star(f, g)`  |
| **Directional drift**     | Signed mean difference                       | `drift(f, g)`          |
| **Curvature**             | Average second derivative magnitude          | `curvature(f)`         |
| **Symbolic audit**        | Comparing models by functional behavior      | General concept        |
| **Domain**                | Input space over which metrics are evaluated | `domain` parameter     |
| **Bootstrap CI**          | Confidence interval via resampling           | CLI / `dp.compare()`   |
| **Drift verdict**         | Summary label: “drift” or “no drift”         | CLI output             |

---

## 🧠 Usage Tips

- Always introduce symbols with plain language first  
- Use φ and Δφ consistently — don’t switch to “distance” or “warp” mid-doc  
- Link glossary terms in tutorials and notebooks  
- Add new terms here before using them in code or docs

---

## ✳️ Visual Metaphors

- φ → vertical gap between prediction curves  
- Δφ → difference in curvature or slope  
- φ* → symbolic blend of both  
- Drift → arrow showing directional bias  
- Curvature → thickness of curve or second derivative heatmap

