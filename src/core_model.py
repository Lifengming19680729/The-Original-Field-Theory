
---

#### 🌌 库二：原始场理论 — `The-Original-Field-Theory`

这是一个Python研究库。

**请按以下结构在您的 `The-Original-Field-Theory` 仓库中创建文件：**

**1. 核心模型：创建 `src/core_model.py`**
```python
import numpy as np

# 核心常数 (Duole-Axiom)
ZETA_CRITICAL = 5.60e-19
TOPOLOGICAL_ENTROPY_CRITICAL = 134.270
VIOLENT_DERIVATION_LAMBDA = 1.2e18

# 树级耦合常数
COUPLING_CONSTANTS = {
    'U1': 0.358,
    'SU2': 0.646,
    'SU3': 0.734
}

def violent_derivation_operator(zeta):
    """暴烈衍生算子 (Ûζ)"""
    if zeta < ZETA_CRITICAL:
        beta = 1.0
        exponent = -beta / (ZETA_CRITICAL - zeta)
        return np.exp(VIOLENT_DERIVATION_LAMBDA * exponent)
    else:
        entropy_values = [5.32, 5.29, 5.25]
        return sum(np.exp(s) for s in entropy_values)

def survival_criterion(S_topo, alpha, beta, S_mbeta):
    """幸存判据 (𝒟α > 0)"""
    distance = np.linalg.norm(alpha - beta)
    log_term = np.log2(1 + np.exp(-distance) * S_mbeta / TOPOLOGICAL_ENTROPY_CRITICAL)
    D_alpha = S_topo - TOPOLOGICAL_ENTROPY_CRITICAL + log_term
    return D_alpha > 0, D_alpha

def gauge_group_connection(group_id, density_center, density_fluctuation):
    """规范群联络形式 (A_μ^(i))"""
    kappa_i = np.sqrt(np.pi/8) / COUPLING_CONSTANTS[group_id]
    return kappa_i * density_center, kappa_i * density_fluctuation

def running_coupling(i, mu, mu0, g0, Delta_D_alpha, b_i):
    """跑动耦合常数 (带混沌修正)"""
    term1 = 1 / (g0 ** 2)
    term2 = (b_i / (8 * np.pi**2)) * np.log(mu / mu0)
    gamma_i = b_i / (8 * np.pi**2 * TOPOLOGICAL_ENTROPY_CRITICAL)
    term3 = gamma_i * Delta_D_alpha
    return 1 / (term1 + term2 + term3)
