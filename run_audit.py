import argparse
from docs.case_studies.credit_scoring_audit import run_credit_audit
from docs.case_studies.medical_glucose_audit import run_medical_audit
from docs.case_studies.retail_drift_detection import run_retail_audit

def main():
    parser = argparse.ArgumentParser(description="Run symbolic audit by domain")
    parser.add_argument("--domain", choices=["credit", "medical", "retail"], required=True)
    args = parser.parse_args()

    if args.domain == "credit":
        run_credit_audit()
    elif args.domain == "medical":
        run_medical_audit()
    elif args.domain == "retail":
        run_retail_audit()

if __name__ == "__main__":
    main()
