import arviz as az
import pymc as pm


def beta_binomial_abtest(
    control_observations,
    control_users,
    variant_observations,
    variant_users,
    tune=1000,
    draws=5000,
    prior_a_control=1,
    prior_b_control=1,
    prior_a_variant=1,
    prior_b_variant=1,
):
    """
    Beta-Binomial Bayesian AB test
    """
    with pm.Model():
        pm.Binomial(
            "control_bin",
            n=control_users,
            p=pm.Beta("control", prior_a_control, prior_b_control),
            observed=control_observations,
        )
        pm.Binomial(
            "variant_bin",
            n=variant_users,
            p=pm.Beta("variant", prior_a_variant, prior_b_variant),
            observed=variant_observations,
        )
        trace = pm.sample(return_inferencedata=True, tune=tune, draws=draws)

    return trace


def _calc_ci_perc(ci_point, control_mean):
    return round((float(ci_point) - control_mean) / control_mean * 100, 1)


def bayesian_statement(
    trace, control_mean, variant_label, control_label="Control", confidence_level=0.95
):
    ci = az.hdi(trace, hdi_prob=confidence_level)["variant"]
    return (
        f"There is a {confidence_level*100:.0f}% chance that the difference between "
        f"{variant_label} and {control_label} is between {_calc_ci_perc(ci[0], control_mean)}%"
        f" and {_calc_ci_perc(ci[1], control_mean)}%"
    )
