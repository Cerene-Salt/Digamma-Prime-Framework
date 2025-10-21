import mlflow

def log_to_mlflow(run_id, ϝ, δϝ):
    mlflow.start_run(run_id=run_id)
    mlflow.log_metric("structural_drift", ϝ)
    mlflow.log_metric("rate_instability", δϝ)
    mlflow.end_run()

def symbolic_alerts(ϝ, δϝ, thresholds):
    return {
        "retrain": ϝ > thresholds["ϝ_retrain"],
        "alert": δϝ > thresholds["δϝ_alert"]
    }

if __name__ == "__main__":
    print(symbolic_alerts(ϝ=2.6, δϝ=1.3, thresholds={"ϝ_retrain": 2.5, "δϝ_alert": 1.2}))

