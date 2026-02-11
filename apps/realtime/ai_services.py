# AI helpers and anomaly detection placeholders
import numpy as np

class AIService:
    @staticmethod
    def recommend_parameters(time_series):
        # Placeholder: simple heuristic recommendations
        mean = float(np.mean([p.value for p in time_series])) if time_series else 0.0
        return {'suggested_mud_weight': mean}

    @staticmethod
    def detect_anomalies(values, threshold=3.0):
        # Very simple z-score based anomaly detection
        arr = np.array(values)
        if arr.size == 0:
            return []
        z = (arr - arr.mean()) / (arr.std() + 1e-9)
        return list((z > threshold).nonzero()[0])
