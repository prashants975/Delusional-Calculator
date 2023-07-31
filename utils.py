from scipy.stats import norm

working_ratio = {
    "Male": 0.80,
    "Female": 0.20
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

conv_dict = {0.0: '0.00 Lak', 150000.0: '1.50 Lak', 200000.0: '2.00 Lak', 250000.0: '2.50 Lak', 350000.0: '3.50 Lak', 400000.0: '4.00 Lak', 450000.0: '4.50 Lak', 500000.0: '5.00 Lak', 550000.0: '5.50 Lak', 950000.0: '9.50 Lak', 1000000.0: '10.00 Lak', 1500000.0: '15.00 Lak', 2000000.0: '20.00 Lak', 2500000.0: '25.00 Lak', 5000000.0: '50.00 Lak', 10000000.0: '1.00 Cr', 50000000.0: '5.00 Cr', 100000000.0: '10.00 Cr', 250000000.0: '25.00 Cr', 500000000.0: '50.00 Cr', 1000000000.0: '100.00 Cr', 5000000000.0: '500.00 Cr'}
conv_dict_rev = {'0.00 Lak': 0.0,
 '1.50 Lak': 150000.0,
 '2.00 Lak': 200000.0,
 '2.50 Lak': 250000.0,
 '3.50 Lak': 350000.0,
 '4.00 Lak': 400000.0,
 '4.50 Lak': 450000.0,
 '5.00 Lak': 500000.0,
 '5.50 Lak': 550000.0,
 '9.50 Lak': 950000.0,
 '10.00 Lak': 1000000.0,
 '15.00 Lak': 1500000.0,
 '20.00 Lak': 2000000.0,
 '25.00 Lak': 2500000.0,
 '50.00 Lak': 5000000.0,
 '1.00 Cr': 10000000.0,
 '5.00 Cr': 50000000.0,
 '10.00 Cr': 100000000.0,
 '25.00 Cr': 250000000.0,
 '50.00 Cr': 500000000.0,
 '100.00 Cr': 1000000000.0,
 '500.00 Cr': 5000000000.0}