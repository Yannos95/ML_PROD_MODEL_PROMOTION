import os
import json
import sys

ACCURACY_THRESHOLD = float(os.getenv("ACCURACY_THRESHOLD", "0.90"))

def main():
    if not sys.stdin.isatty():
        payload = sys.stdin.read().strip()
    else:
        try:
            payload = sys.argv[1]
        except IndexError:
            print("Usage: echo 'JSON' | python evaluate.py")
            sys.exit(1)
            
    data = json.loads(payload)
    acc = float(data["accuracy"])
    
    passed = acc >= ACCURACY_THRESHOLD
    
    result = {
        "passed": passed,
        "accuracy": acc,
        "threshold": ACCURACY_THRESHOLD,
        "model_version": data.get("model_version"),
        "run_id": data.get("run_id"),
    }
    
    print(json.dumps(result))
    
    if not passed:
        sys.exit(2)

if __name__ == "__main__":
    main()