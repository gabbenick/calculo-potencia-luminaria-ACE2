def get_input_with_default(prompt, default):
    user_input = input(f"{prompt} (padrão: {default}): ")
    return float(user_input) if user_input.strip() else default

def coletar_parametros():
    parametros = {
        "N": 1,
        "Emed": 150,
        "area": 30,
        "U": 1,
        "FM": 1,
        "FFL": 1
    }

    print("== Entrada de Dados ==")
    for chave, valor_padrao in parametros.items():
        entrada = get_input_with_default(chave, valor_padrao)
        parametros[chave] = int(entrada) if chave == "N" else float(entrada)

    eficacia_luminosa = get_input_with_default("Eficácia luminosa da lâmpada (lm/W)", 100)
    return parametros, eficacia_luminosa
