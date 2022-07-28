from .viz import plot_control_variant_diff
from .stats import bayesian_statement, beta_binomial_abtest


def abtest_plot(control_observations, control_users, variant_observations, variant_users, title = "", tune = 1000, draws = 5000, xlimit = 60, bins = 50):
    """
    Runs the Beta-Binomial model in the background and returns the result plot. 
    """
    plot_control_variant_diff(beta_binomial_abtest(control_observations, control_users, variant_observations, variant_users), title, xlimit, bins)

