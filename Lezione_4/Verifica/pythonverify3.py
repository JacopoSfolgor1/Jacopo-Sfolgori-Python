def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    # cancella pass e scrivi il tuo codice
    for n in sorted(original_set):
        if n in elements_to_remove:
            original_set.remove(n)
    return original_set
print(remove_elements({5, 6, 7}, [7, 8, 9]))