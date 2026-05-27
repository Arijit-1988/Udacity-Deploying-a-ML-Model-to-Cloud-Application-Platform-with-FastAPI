"""Basic sanity checks for API test coverage.

Checks:
- Presence of at least one GET root API test.
- Presence of at least two POST predict tests.
- Presence of both output labels in API tests.
"""

from pathlib import Path


def main():
    test_file = Path(__file__).resolve().parent / "tests" / "test_api.py"
    content = test_file.read_text(encoding="utf-8")

    issues = []

    if "client.get(\"/\")" not in content and "client.get('/')" not in content:
        issues.append("Missing GET / test call.")

    post_count = content.count('client.post("/predict"') + content.count("client.post('/predict'")
    if post_count < 2:
        issues.append("Expected at least 2 POST /predict test calls.")

    if '"<=50K"' not in content and "'<=50K'" not in content:
        issues.append("Missing <=50K expected output test.")

    if '">50K"' not in content and "'>50K'" not in content:
        issues.append("Missing >50K expected output test.")

    if issues:
        print("Sanity check: FAILED")
        for item in issues:
            print(f"- {item}")
        raise SystemExit(1)

    print("Sanity check: PASSED")


if __name__ == "__main__":
    main()
