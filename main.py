import numpy as np
import matplotlib.pyplot as plt

def print_stats(var, var_name="unnamed_variable"):
    print("{v} has mean = {m} and stdev = {s} ({n} samples)".format(v=var_name, m=var.mean(), s=var.std(), n=len(var)))

def plot_hist(var, var_name="unnamed_variable", bin_count=30):
    count, bins, ignored = plt.hist(var, bin_count, label=var_name)
    plt.plot(bins)
    plt.show()
    
def present_var(var, var_name="unnamed_variable"):
    """Presents one variable only
    """
    print_stats(var, var_name)
    plot_hist(var, var_name)
    
def present_vars(vars, var_names, bin_count=30):
    """Presents multiple variables on a single chart
    """
    map(print_stats, vars, var_names)
    hists = [plt.hist(var, bin_count, alpha=0.5, label=var_name)[1] for var, var_name in zip(vars, var_names)]
    plt.plot(*hists)
    plt.legend(loc='upper right')
    plt.show()

def demo():
    """Demo with formula: y = x^2 + 2*x + 1
    Where x is a random variable that follows normal distribution with mean=0 & sigma=1
    """
    N_SAMPLE = 1000000
    mu, sigma = 0, 1
    print("N_SAMPLE={n}, mu={m}, sigma={s}".format(n=N_SAMPLE, m=mu, s=sigma))
    x = np.random.normal(mu, sigma, N_SAMPLE)   # N_SAMPLE-sized array of random variable x
    y = x**2 + 2*x + 1                          # N_SAMPLE-sized array of deduced variable y
#     present_var(x, "x")
#     present_var(y, "y")
    present_vars((x, y), ("x", "y"))

def calc_pH_by_d11Bcarbonate(mu_d11Bcarbonate, sigma_d11Bcarbonate, N_SAMPLE=1000000):
    # random variable
    d11Bcarbonate = np.random.normal(mu_d11Bcarbonate, sigma_d11Bcarbonate, N_SAMPLE)
    print("calc_pH_by_d11Bcarbonate: N_SAMPLE={n}, mu_d11Bcarbonate={m}, sigma_d11Bcarbonate={s}".format(n=N_SAMPLE, m=mu_d11Bcarbonate, s=sigma_d11Bcarbonate))
    # constants
    pKb = 8.6152
    d11Bsw = 39.61
    alpha = 1.0272
    print("pKb = {k}, d11Bsw = {s}, alpha = {a}".format(k=pKb, s=d11Bsw, a=alpha))
    # formula
    pH = pKb - np.log10((d11Bsw - d11Bcarbonate) / (alpha * d11Bcarbonate - d11Bsw + 1000 * (alpha - 1)))
    present_vars((d11Bcarbonate, pH), ("d11Bcarbonate", "pH"))

if __name__ == "__main__":
    # Run demo
    # Replace with actual formula for real use
#     demo()
    
    calc_pH_by_d11Bcarbonate(17.39, 0.19)