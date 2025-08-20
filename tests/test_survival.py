import numpy as np
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core_model import survival_criterion

def test_survival_criterion():
    # Test case that should survive
    S_topo = 135.0
    alpha = np.array([0.0])
    beta = np.array([0.0])
    S_mbeta = 134.27
    
    survives, D_alpha = survival_criterion(S_topo, alpha, beta, S_mbeta)
    assert survives == True
    assert D_alpha > 0
    print("✓ Survival test passed")

def test_non_survival():
    # Test case that should not survive
    S_topo = 134.0
    alpha = np.array([0.0])
    beta = np.array([1.0])
    S_mbeta = 100.0
    
    survives, D_alpha = survival_criterion(S_topo, alpha, beta, S_mbeta)
    assert survives == False
    print("✓ Non-survival test passed")

if __name__ == "__main__":
    test_survival_criterion()
    test_non_survival()
    print("All tests passed! ✅")
