import requests
import json
import sys
import threading
import time

# Códigos ANSI para cor
COR = "\033[38;5;214m"  # Amarelo
RESET = "\033[0m"
BLACK = "\033[30m"

# Flag para controlar o loading
loading = True

def loading_animation():
    dots = 0
    while loading:
        sys.stdout.write(f"\r{BLACK}aguarde{'.' * dots}{' ' * (3 - dots)}{RESET}")
        sys.stdout.flush()
        dots = (dots + 1) % 4
        time.sleep(0.5)
    # Limpa a linha do loading ao terminar
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

def stream_color_think():
    inside_think = False
    buffer = ""
    first_think = True

    def process_chunk(chunk):
        nonlocal inside_think, buffer, first_think
        global loading
        # Ao receber o primeiro chunk, para o loading
        if loading:
            loading = False
            time.sleep(0.1)  # Pequeno delay para garantir que o loading pare antes de imprimir
        buffer += chunk
        while True:
            if inside_think:
                end = buffer.find("</think>")
                if end == -1:
                    sys.stdout.write(f"{COR}{buffer}{RESET}")
                    sys.stdout.flush()
                    buffer = ""
                    break
                else:
                    sys.stdout.write(f"{COR}{buffer[:end]}{RESET}{BLACK}\n\n--- Início da resposta --- ")
                    sys.stdout.flush()
                    buffer = buffer[end+8:]
                    inside_think = False
            else:
                start = buffer.find("<think>")
                if start == -1:
                    sys.stdout.write(buffer)
                    sys.stdout.flush()
                    buffer = ""
                    break
                else:
                    if first_think:
                        sys.stdout.write(f"{COR}\n\nPensando ---{RESET}")
                        sys.stdout.flush()
                        first_think = False
                    sys.stdout.write(buffer[:start])
                    sys.stdout.flush()
                    buffer = buffer[start+7:]
                    inside_think = True

    return process_chunk

def call_ollama(prompt):
    global loading
    loading = True
    # Inicia o loading em uma thread separada
    t = threading.Thread(target=loading_animation)
    t.start()
    try:
        resp = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "deepseek-r1:1.5b", "prompt": prompt},
            stream=True,
            timeout=30
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        loading = False
        print(f"Erro ao conectar à API: {e}")
        return

    process_chunk = stream_color_think()
    for line in resp.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    process_chunk(data["response"])
            except Exception as e:
                print(f"\nErro ao processar linha: {e}")
    loading = False
    t.join()
    print(f"{RESET}\n\n--- Fim da resposta ---\n\n")

while True:
    user_input = input(f"{BLACK}Escreva o seu prompt ou '/sair': {RESET}")
    if user_input == "/sair":
        break
    call_ollama(user_input)