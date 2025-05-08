def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codie
    result: dict[str, list[int]] = {}

    for key,value in tuples:
        if key not in result:
            result[key] = [value]
        else:
            result[key].append(value)

    return result