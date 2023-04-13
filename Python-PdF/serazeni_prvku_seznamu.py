def vyskytI(text):
    return text.count("i")

seznam = ["digitalizace", "multiplex", "kvantování", "PCM signalizace", "optika"]

print("\nVýpis seznamu:\n")
print(seznam)

print("\nVýpis seznamu seřazeného podle abecedy (velká písmena mají přednost):\n")
print(sorted(seznam))

print("\nVýpis seznamu seřazeného podle abecedy pozpátku:\n")
print(sorted(seznam, reverse=True))

print("\nVýpis seznamu seřazeného podle abecedy s ignorováním velkých písmen:\n")
print(sorted(seznam, key=str.lower)) 

print("\nVýpis seznamu podle délky slova (od nejkratšího po nejdelší):\n")
print(sorted(seznam, key=len))

print("\nVýpis seznamu podle výskytu písmena i (od nejmenšího po největší):\n")
print(sorted(seznam, key=vyskytI))