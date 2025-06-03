valor = 21

print('Valor decimal:',valor)  # Exibe o valor original

valor_hexadecimal: str = hex(valor)

print('Valor em hexadecimal:',valor_hexadecimal)  # Exibe o valor hexadecimal do membro_id sem o prefixo '0x'

valor_decinal = int(valor_hexadecimal, 16)

print('Valor decimal novamente:',valor_decinal)  # Exibe o valor decimal convertido de volta

# OU

valor_decinal = int(valor_hexadecimal[2:], 16)

print('Valor decimal novamente:',valor_decinal)  # Exibe o valor decimal convertido de volta