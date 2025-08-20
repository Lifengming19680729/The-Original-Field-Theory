
### **第二个库：原始场理论（ChaosField-Theory）—— Python库**  


#### 1. 核心模型文件（`src/core_model.py`）  
```python
import numpy as np
from scipy.integrate import trapz
from DynamicIntervals import DInt  # 假设已安装DIM库

# 核心参数（论文精要版）
ζc = 5.60e-19       # 临界参数（Duole-Axiom 2）
Sc = 134.270         # 临界拓扑熵（Duole-Axiom 3）
λ_暴烈 = 1.2e18      # 暴烈算子指数系数
g_tree = {           # 树级耦合常数（规范群）
    'U1': 0.358,
    'SU2': 0.646,
    'SU3': 0.734
}

def 暴烈衍生算子(ζ):
    """论文2.2节：暴烈衍生算子"""
    if ζ < ζc:
        # ζ < ζc时的指数形式
        exponent = -1 / (ζc - ζ)  # β=1简化
        return np.exp(λ_暴烈 * exponent)
    else:
        # ζ ≥ ζc时分岔形式（简化版）
        S = [5.32, 5.29, 5.25]  # 拓扑熵
        return np.sum(np.exp(S))

def 幸存判据(S_topo, α, β, S_mβ):
    """论文2.3节：幸存判据𝒟_α > 0"""
    d = np.linalg.norm(α - β)  # 距离d(α,β)
    term = np.log2(1 + np.exp(-d) * S_mβ / Sc)
    Dα = S_topo - Sc + term
    return Dα > 0

def 规范群联络(i, ρ, δρ):
    """论文3.1节：规范群联络形式A_μ^(i)"""
    # ρ: 场密度中心值，δρ: 密度偏差（动态区间）
    κ = np.sqrt(np.pi / 8) / g_tree[i]
    b_ρ = ρ  # 中心值
    δ_ρ = δρ  # 偏差
    return (κ * b_ρ, κ * δ_ρ)  # (中心值, 偏差)

def 跑动耦合(i, μ, μ0, Dα, Dα0):
    """论文3.2节：跑动耦合常数"""
    # 简化版：含混沌修正
    b = {'U1': 1, 'SU2': 2, 'SU3': 3}  # 假设的β函数系数
    term1 = 1 / (g_tree[i] ** 2)
    term2 = (b[i] / (8 * np.pi **2)) * np.log(μ / μ0)
    γ = (b[i] / (8 * np.pi** 2 * Sc))  # 混沌修正系数
    term3 = γ * (Dα / Dα0)
    return 1 / (term1 + term2 + term3)
