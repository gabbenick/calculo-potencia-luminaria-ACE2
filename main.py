from entradas import coletar_parametros
from calculos import calcular_potencia_estimativa

def main():
    print("== Cálculo de Potência Estimada da Lâmpada ==")
    parametros, eficacia = coletar_parametros()
    resultado = calcular_potencia_estimativa(parametros, eficacia)

    print("\n== Resultado ==")
    print(f"Fluxo luminoso total necessário: {resultado['fluxo_total']:.2f} lm")
    print(f"Fluxo por luminária: {resultado['fluxo_por_luminaria']:.2f} lm")
    print(f"Potência estimada por luminária: {resultado['potencia_estimativa_W']:.2f} W")

if __name__ == "__main__":
    main()
