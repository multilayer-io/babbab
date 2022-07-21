import pymc as pm

def beta_binomial_abtest(control_observations, control_users, variant_observations, variant_users, tune = 1000, draws = 5000):
    with pm.Model():
        pm.Binomial("control_bin", n=control_users, p=pm.Beta('control', 1, 99), observed=control_observations)
        pm.Binomial("variant_bin", n=variant_users, p=pm.Beta('variant', 1, 99), observed=variant_observations)
        trace = pm.sample(return_inferencedata=True, tune=tune, draws=draws)
        
    return trace

def calc_ci_perc(ci_point, control_mean):
    return round((float(ci_point) - control_mean) / control_mean * 100, 1)

def bayesian_statement(trace, control_mean, variant_label, control_label = "Control", confidence_level = 0.9):
    ci = az.hdi(trace, hdi_prob=confidence_level)["variant"]
    return f"There is a {confidence_level*100:.0f}% chance that the difference for {variant_label} in respect to {control_label} is between {calc_ci_perc(ci[0], control_mean)}% and {calc_ci_perc(ci[1], control_mean)}%"


