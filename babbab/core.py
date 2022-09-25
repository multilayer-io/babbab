from .stats import bayesian_statement, beta_binomial_abtest
from .viz import plot_control_variant_diff


def quick_analysis(
    control_observations,
    control_users,
    variant_observations,
    variant_users,
    title="",
    tune=1000,
    draws=5000,
    xlimit=60,
    bins=50,
    variant_label="Variant",
    control_label="Control",
    xlabel="% change",
    confidence_level=0.95,
):
    """
    Runs the Beta-Binomial model in the background and returns the result plot.
    """
    trace = beta_binomial_abtest(
        control_observations, control_users, variant_observations, variant_users
    )
    return (
        plot_control_variant_diff(trace, title, xlimit, bins, xlabel),
        bayesian_statement(
            trace,
            control_observations / control_users,
            variant_label,
            control_label="Control",
            confidence_level=confidence_level,
        ),
        trace,
    )
