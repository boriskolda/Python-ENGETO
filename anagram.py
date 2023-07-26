# V této úloze si vyzkoušíš identifikaci anagramů.

# Anagramy jsou dvě a více slov složených ze stejných znaků. Třeba anglická slova ship a hips.

# Pokud budeš chtít, můžeš se mrknout na tento web, který generuje anagramy.

# Tvoje úloha musí obsahovat tyto kroky:

# Vytvoř funkci je_anagram, která může mít jako vstup libovolně dlouhý tuple,
# z první hodnoty v sekvenci stanoví vzor, jehož písmena seřadí,
# funkce potom projde všechny hodnoty ze vstupu a ověří, jestli nejsou anagram,
# pokud JSOU anagram, vrátí True,
# pokud NEJSOU anagram, vrátí False,
# vyzkoušej funkci spustit podle zadání v ukázce.


def je_anagram(*args):

    vzor = sorted(args[0])
    
    for slovo in args:
        if sorted(slovo) != vzor:
            return False
    else:
        return True
print(
    je_anagram("ship", "hips", "hisp"),
    je_anagram("ship", "hips", "duck"),
    sep="\n"
)