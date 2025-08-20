import numpy as np
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core_model import violent_derivation_operator, survival_criterion

# 核心常数 (需重复声明以供本文件使用)
ZETA_CRITICAL = 5.60e-19
VIOLENT_DERIVATION_LAMBDA = 1.2e18
TOPOLOGICAL_ENTROPY_CRITICAL = 134.270

PREDICTION_VALUE = 8.221
PREDICTION_ERROR = 0.002

def calculate_muonic_hydrogen_lamb_shift(zeta, S_topo):
    """计算μ子氢兰姆位移"""
    try:
        # 计算混沌涨落 ε(t)
        epsilon = np.exp(-VIOLENT_DERIVATION_LAMBDA * (ZETA_CRITICAL - zeta))
        
        # 应用暴烈算子
        V_zeta = violent_derivation_operator(zeta)
        
        # 幸存判据参数
        alpha = np.array([0.1])
        beta = np.array([0.2])
        S_mbeta = 130.0
        
        # 筛选检查
        survives, D_alpha = survival_criterion(S_topo, alpha, beta, S_mbeta)
        if not survives:
            return None, None, "System did not survive derivation criterion"
        
        # 映射到物理预言
        conversion_factor = 1.2e3
        calculated_value = epsilon * V_zeta * conversion_factor
        calculated_error = abs(epsilon) * conversion_factor * 0.1
        
        return calculated_value, calculated_error, "Success"
    
    except Exception as e:
        return None, None, f"Calculation error: {str(e)}"

if __name__ == "__main__":
    # 测试参数
    zeta_test = 5.59e-19
    S_topo_test = 135.0
    
    value, error, status = calculate_muonic_hydrogen_lamb_shift(zeta_test, S_topo_test)
    
    print(f"Calculation status: {status}")
    if value is not None:
        print(f"Calculated Lamb shift: {value:.6f} ± {error:.6f} meV")
        print(f"Theoretical prediction: {PREDICTION_VALUE} ± {PREDICTION_ERROR} meV")
        discrepancy = abs(value - PREDICTION_VALUE)
        print(f"Discrepancy: {discrepancy:.6f} meV")
        if discrepancy < (error + PREDICTION_ERROR):
            print("✅ Prediction VERIFIED")
        else:
            print("❌ Prediction NOT verified")
