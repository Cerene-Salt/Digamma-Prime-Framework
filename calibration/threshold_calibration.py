import numpy as np
from sklearn.cluster import KMeans

def calibrate(metric_log, method="quantile"):
    metric_log = np.array(metric_log)
    if method == "quantile":
        return np.percentile(metric_log, [75, 90])
    elif method == "kmeans":
        km = KMeans(n_clusters=2).fit(metric_log.reshape(-1, 1))
        return sorted(km.cluster_centers_.flatten())
    

if __name__ == "__main__":
    sample = [0.5, 1.2, 2.0, 2.5, 3.1]
    print("Quantile thresholds:", calibrate(sample, method="quantile"))
    print("KMeans thresholds:", calibrate(sample, method="kmeans"))

