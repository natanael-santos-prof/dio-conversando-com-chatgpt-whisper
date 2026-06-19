import os
import time
from openai import OpenAI
from gtts import gTTS
import sounddevice as sd
from scipy.io.wavfile import write

# Configuração do cliente OpenAI - COLE SUA CHAVE DE API ABAIXO:
client = OpenAI("SUA_CHAVE_AQUI")

def gravar_audio(nome_arquivo="input.wav", duracao=5, fs=44100):
    """Grava o áudio do microfone por um tempo determinado."""
    print("🎤 Gravando... fale agora!")
    gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(nome_arquivo, fs, gravacao)
    print("✅ Gravação finalizada.")

def transcrever_audio(nome_arquivo="input.wav"):
    """Usa o OpenAI Whisper para transformar áudio em texto."""
    print("🤖 Transcrevendo com Whisper...")
    with open(nome_arquivo, "rb") as arquivo_audio:
        transcricao = client.audio.transcriptions.create(
            model="whisper-1", 
            file=arquivo_audio
        )
    return transcricao.text

def responder_com_chatgpt(texto_usuario):
    """Envia o texto para o ChatGPT e retorna a resposta."""
    print(f"🗣️ Você disse: {texto_usuario}")
    print("🧠 Pensando...")
    
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente virtual prestativo e responde em português de forma concisa."},
            {"role": "user", "content": texto_usuario}
        ]
    )
    return resposta.choices.message.content

def falar_resposta(texto_resposta, nome_saida="output.mp3"):
    """Transforma texto em áudio usando gTTS e abre no player padrão do Windows."""
    print(f"🤖 ChatGPT: {texto_resposta}")
    
    # Gera o arquivo de áudio mp3
    tts = gTTS(text=texto_resposta, lang='pt', tld='com.br')
    tts.save(nome_saida)
    
    # Executa o arquivo usando o player nativo do Windows (Groove, Media Player, etc)
    os.system(f"start {nome_saida}")

# --- Fluxo Principal de Execução ---
if __name__ == "__main__":
    try:
        # 1. Captura a voz do usuário (6 segundos de gravação)
        gravar_audio(duracao=6)
        
        # 2. Transcreve com Whisper
        texto_capturado = transcrever_audio()
        
        # 3. Processa e gera resposta com ChatGPT
        resposta_final = responder_com_chatgpt(texto_capturado)
        
        # 4. Fala a resposta abrindo o arquivo de áudio
        falar_resposta(resposta_final)
        
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")
