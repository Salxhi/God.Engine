puntajes = [78, 95, 62, 88, 71]

puntajes_ascendentes = sorted(puntajes)
puntajes_descendentes = sorted(puntajes, reverse=True)

print(f"De menor a mayor: {puntajes_ascendentes}")
print(f"De mayor a menor: {puntajes_descendentes}")
