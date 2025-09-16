# Script para se comunicar com o Ollama via REST API

Olá!

Esse é um script simples para demonstrar como se conectar ao Ollama para obter respostas de um modelo de AI (no caso um _Small Language Model - SML_).

Não é nada complexo complexo na parte de conexão. O _core_ do script é esse:

```
resp = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "deepseek-r1:1.5b", "prompt": prompt},
            stream=True,
            timeout=30
```

Todo o restante são as firulinhas que coloquei para permitir que o _streaming_ tivesse outra cor, um micro loading até a AI começar a responder e um looping simples para o usuário poder fazer mais de um prompt até se cansar.

**Importante:** para rodar esse script é preciso ter o [Ollama](https://ollama.com/) instalado em sua máquina. Escolhi o modelo **_[deepseek r1:1.5b](https://ollama.com/library/deepseek-r1:1.5b)_** por ele ser extremamente leve, mas ele só consegue entender inglês. Se quiser algo rodando local e que fale a nossa língua, baixe o [phi3:mini](https://ollama.com/library/phi3:mini) na Microsoft.

Fica aqui o meu super beijo de jujuba!

Tio .faso
