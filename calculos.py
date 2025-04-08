def calcular_fluxo_luminoso_total(N, Emed, area, U, FM, FFL):
    return (Emed * area) / (U * FM * FFL)

def calcular_potencia_estimativa(params, eficacia_luminosa=100):
    fluxo_total = calcular_fluxo_luminoso_total(
        params["N"], params["Emed"], params["area"],
        params["U"], params["FM"], params["FFL"]
    )
    fluxo_por_luminaria = fluxo_total / params["N"]
    potencia_por_luminaria = fluxo_por_luminaria / eficacia_luminosa
    return {
        'fluxo_total': fluxo_total,
        'fluxo_por_luminaria': fluxo_por_luminaria,
        'potencia_estimativa_W': potencia_por_luminaria
    }
