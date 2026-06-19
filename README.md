# 🎤 Assistente de Voz Inteligente

Olá! Seja bem-vindo(a) ao meu projeto desenvolvido para a plataforma **DIO**. 

Muitas vezes, interagir com computadores digitando pode ser demorado ou cansativo. Este projeto foi criado para resolver isso: ele funciona como um assistente virtual por voz personalizado, parecido com a Alexa ou o Google Assistente, mas utilizando a inteligência do ChatGPT.

---

### 🤔 Para que serve e onde pode ser usado?

Este sistema serve para automatizar o atendimento e facilitar a comunicação entre humanos e máquinas. Ele pode ser aplicado em diversas situações do dia a dia e do mercado, como:

* **Atendimento ao Cliente**: Criar secretárias virtuais para clínicas, lojas ou lanchonetes que atendem clientes por comandos de voz ou ligações.
* **Acessibilidade**: Ajudar pessoas idosas, com dificuldades motoras ou deficiência visual a utilizarem sistemas de computador apenas falando, sem precisar de teclado ou mouse.
* **Sistemas de Carro ou Casa**: Controlar rotinas e tirar dúvidas rapidamente enquanto você está com as mãos ocupadas (cozinhando ou dirigindo, por exemplo).

---

### ⚙️ Como o projeto funciona por dentro? (Passo a Passo)

O fluxo do programa é muito simples e dividido em 4 etapas automáticas:

1. **Ouvir**: O programa liga o microfone do computador e grava a sua voz por alguns segundos.
2. **Entender**: Ele pega esse arquivo de áudio gravado e o transforma em texto escrito.
3. **Pensar**: Esse texto é enviado para a inteligência artificial do ChatGPT, que analisa a pergunta e cria uma resposta inteligente.
4. **Falar**: O sistema pega a resposta em texto do ChatGPT, transforma em uma voz artificial em português e toca nos alto-falantes para você ouvir.

---

### 🚀 Como testar no seu computador

Se você quiser ver o projeto funcionando na sua máquina:
1. Baixe os arquivos deste repositório.
2. Instale os componentes necessários rodando o comando `pip install -r requirements.txt` no seu terminal.
3. Coloque a sua chave de acesso da OpenAI dentro do arquivo `app.py`.
4. Execute o programa digitando `python app.py` e fale com o seu assistente!


