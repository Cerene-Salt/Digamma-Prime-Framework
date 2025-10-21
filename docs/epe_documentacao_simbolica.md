# Documentação Simbólica — Lady Epe

## Introdução
A Lady Epe é um sistema simbólico para auditoria de modelos, capaz de detectar divergência estrutural, curvatura e instabilidade funcional.

## Métricas

| Símbolo | Nome técnico        | Interpretação simbólica |
|--------|---------------------|--------------------------|
| ϝ      | Variação estrutural | Diferença na forma geral da função |
| δϝ     | Variação de taxa     | Diferença na velocidade de mudança |
| δ²ϝ    | Variação de curvatura| Diferença na aceleração da mudança |

## Aplicações

- 🔍 Curvatura: Detecta mudanças de forma mesmo com valores semelhantes
- ⚖️ Justiça: Revela instabilidades que afetam fairness
- 🧱 Estabilidade: Monitora consistência estrutural ao longo do tempo
- 🎓 Ensino: Transforma álgebra funcional em linguagem visual

## Interpretação Pedagógica

- ϝ → distância entre funções
- δϝ → diferença entre velocidades
- δ²ϝ → diferença entre acelerações

## Exemplo Visual

Funções: `f(x) = x`, `g(x) = x²`  
ϝ é pequena, δ²ϝ é grande → g(x) acelera, f(x) não.

## Pipeline

- `metrics.py`: define ϝ e δϝ
- `temporal.py`: define δ²ϝ
- `monitor.py`: aplica alertas
- `benchmark.py`: compara com KS-test
- `run_monitor.py`: roda auditoria com dados reais
- `test_visual_benchmark.py`: gera gráficos comparativos

# 🧠 Resumo Completo — Lady Epe

## Introdução

A Lady Epe é um sistema simbólico para auditoria de modelos, capaz de detectar mudanças estruturais, variações de taxa e curvatura em séries temporais. Ela vai além dos testes estatísticos clássicos, oferecendo uma abordagem funcional, visual e pedagógica.

---

## 🔣 Métricas centrais

| Símbolo | Nome técnico        | Significado |
|--------|---------------------|-------------|
| ϝ      | Variação estrutural | Diferença entre os valores das séries |
| δϝ     | Variação de taxa     | Diferença entre as velocidades (1ª derivada) |
| δ²ϝ    | Variação de curvatura| Diferença entre acelerações (2ª derivada) |

---

## 📐 Fórmulas computacionais

```python
def phi(f, g):
    return np.linalg.norm(f - g)

def delta_phi(f, g):
    df = np.diff(f)
    dg = np.diff(g)
    return np.linalg.norm(df[:min(len(df), len(dg))] - dg[:min(len(df), len(dg))])

def second_order_divergence(f, g):
    d2f = np.diff(np.diff(f))
    d2g = np.diff(np.diff(g))
    return np.linalg.norm(d2f[:min(len(d2f), len(d2g))] - d2g[:min(len(d2f), len(d2g))])

