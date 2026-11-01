import math
from statistics import NormalDist

def ab_test_conversion(control_conversions: int, control_n: int, treatment_conversions: int, treatment_n: int, alpha: float = 0.05) -> dict:
    """
    Returns lift, z, p_value, ci_low, ci_high and significant for a two-proportion z-test.
    """
    # Conversion rates
    p1 = control_conversions / control_n
    p2 = treatment_conversions / treatment_n

    # Absolute lift
    lift = p2 - p1

    # Pooled conversion rate
    pooled = (control_conversions + treatment_conversions) / (control_n + treatment_n)

    # Pooled standard error
    se_pooled = math.sqrt(
        pooled * (1 - pooled) * (1 / control_n + 1 / treatment_n)
    )

    # Z-statistic and two-sided p-value
    if se_pooled == 0:
        z = 0.0
        p_value = 1.0
    else:
        z = lift / se_pooled

        # Two-sided p-value = 2 * P(Z >= |z|)
        p_value = 2 * (1 - NormalDist().cdf(abs(z)))

    # Unpooled standard error for confidence interval
    se_unpooled = math.sqrt(
        p1 * (1 - p1) / control_n +
        p2 * (1 - p2) / treatment_n
    )

    # Critical value for confidence interval
    z_critical = NormalDist().inv_cdf(1 - alpha / 2)

    margin = z_critical * se_unpooled

    ci_low = lift - margin
    ci_high = lift + margin

    return {
        "lift": float(lift),
        "z": float(z),
        "p_value": float(p_value),
        "ci_low": float(ci_low),
        "ci_high": float(ci_high),
        "significant": bool(p_value < alpha)
    }