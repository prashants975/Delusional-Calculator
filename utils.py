from scipy.stats import norm

working_ratio = {
    "Male": 0.75,
    "Female": 0.25
}

height_stats = {
    "Male": [170, 6.35],
    "Female": [158, 5.59]
}


def calculate_cdf(x, mean, std_dev):
    z_score = (x - mean) / std_dev
    cdf = norm.cdf(z_score)
    return cdf

def height_percentage_calc(gender, x_value_min, x_value_max):

    mean = height_stats[gender][0]
    std_dev = height_stats[gender][1]
    
    
    h_percent = calculate_cdf(x_value_max, mean, std_dev) - calculate_cdf(x_value_min, mean, std_dev)
    return h_percent * 100

