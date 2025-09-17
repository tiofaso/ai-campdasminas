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

---

## Small Language Models (SLMs) mais populares

**DistilBERT (2019, Hugging Face)**

* Pioneiro em SLMs.
* ~66M parâmetros (bem pequeno).
* Muito usado em NLP clássico (classificação, embeddings, QA simples).

**TinyBERT (2019, Huawei)**
* ~14M – 110M parâmetros.
* Otimizado para dispositivos móveis.
* Foco em eficiência.

**MobileBERT (2020, Google)**
* ~25M parâmetros.
* Versão leve do BERT, feita para rodar em smartphones.

**GPT-Neo / GPT-J (2021, EleutherAI)**
* 1.3B – 6B parâmetros.
* Alternativa aberta ao GPT-3 em tamanho reduzido.

**OPT-6.7B / OPT-13B (2022, Meta)**
* Versões pequenas do OPT (Open Pretrained Transformer).
* Usados como baseline de pesquisa.

**Falcon-7B (2023, TII – Technology Innovation Institute)**
* 7B parâmetros.
* Muito popular pela performance e eficiência open-source.

**Mistral-7B (2023, Mistral AI)**
* 7B parâmetros.
* Um dos mais eficientes e populares SLMs atuais.
* Ótimo custo-benefício para fine-tuning.

**Phi-2 (2023, Microsoft)**
* 2.7B parâmetros.
* Enorme destaque pelo foco em qualidade vs. tamanho.

**Phi-3 (2024, Microsoft)**
3* B, 7B e 14B parâmetros.
* Versões “Mini” (3.8B) ficaram famosas pela performance multilíngue.

**Gemma (2024, Google DeepMind)**
* 2B e 7B parâmetros.
* Lançado para ser leve, ético e open-source.

**DeepSeek distill models (2024, DeepSeek)**
V* ersões reduzidas do DeepSeek R1.
* 1.3B, 2.6B e 7B parâmetros.
* Foco em raciocínio e eficiência.
