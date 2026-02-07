# app.py
import requests

def greet(name: str) -> None:
    print(f"Hello, {name}")

def fetch_example() -> str:
    # Safe: includes a timeout, no secrets, no shell commands
    response = requests.get("https://example.com", timeout=5)
    return response.text

if __name__ == "__main__":
    greet("Callum")
    print(fetch_example())
