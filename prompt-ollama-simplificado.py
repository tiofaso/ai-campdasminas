import requests
import json
import sys

resp = requests.post("http://localhost:11434/api/generate",
    json={"model": "deepseek-r1:1.5b", "prompt": "Explain what is artificial intelligence in one phrase."},
    stream=True)

for line in resp.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))  # transforma em dict
        if "response" in data:
            # imprime aos poucos, sem quebrar linha
            sys.stdout.write(data["response"])
            sys.stdout.flush()

print("\n\n--- Fim da resposta ---")
