import os
import base64

def gerar_salty(tamanho_bytes: int = 64) -> str:
    """
    Gera um SALTY aleatório, codificado em Base64 URL-safe, com aproximadamente 88 caracteres.
    """
    salty_bytes = os.urandom(tamanho_bytes)  # 64 bytes aleatórios
    salty_str = base64.urlsafe_b64encode(salty_bytes).decode('utf-8')
    return salty_str

# Exemplo de uso
salty = gerar_salty()
print(salty)
print(f"Tamanho: {len(salty)} caracteres")
