import numpy as np
from ..core_model import violent_derivation_operator, survival_criterion

PREDICTION_VALUE = 8.221
PREDICTION_ERROR = 0.002

def calculate_muonic_hydrogen_lamb_shift(zeta, S_topo):
    """计算μ子氢兰姆位移"""
    try:
        epsilon = np.exp(-VIOLENT_DERIVATION_LAMBDA * (ZETA_CRITICAL - zeta))
        
        V_zeta = violent_derivation_operator(zeta)
        
        alpha = np.array([0.1])
        beta = np.array([0.2])
        S_mbeta = 130.0
        
        survives, D_alpha = survival_criterion(S_topo, alpha, beta, S_mbeta)
        if not survives:
            return None, None, "System did not survive derivation criterion"
        
        conversion_factor = 1.2e3
        calculated_value = epsilon * V_zeta * conversion_factor
        calculated_error = abs(epsilon) * conversion_factor * 0.1
        
        return calculated_value, calculated_error, "Success"
    
    except Exception as e:
        return None, None, f"Calculation error: {str(e)}"

if __name__ == "__main__":
    zeta_test = 5.59e-19
    S_topo_test = 135.0
    
    value, error, status = calculate_muonic_hydrogen_lamb_shift(zeta_test, S_topo_test)
    
    print(f"Calculation status: {status}")
    if value is not None:
        print(f"Calculated Lamb shift: {value:.6f} ± {error:.6f} meV")
        print(f"Theoretical prediction: {PREDICTION_VALUE} ± {PREDICTION_ERROR} meV")
        discrepancy = abs(value - PREDICTION_VALUE)
        print(f"Discrepancy: {discrepancy:.6f} meV")
