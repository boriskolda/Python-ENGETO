# Zadání
# Zapiš uživ. funkci, která ověří zda operační systém na tvém pc je Windows či nikoliv.

# Tvůj zápis musí obsahovat:

# Definici a spuštění uživ. funkce je_os_windows,
# pomocnou knihovny sys s příslušnou metodou na ověření operačního systému,
# uživ. funkce je_os_windows, která vrátí hodnotu True, pokud pracuješ na op. systému windows. Jinak vrátí hodnotu False.

def je_os_windows():
    from sys import platform
    return platform.startswith("win")

print(je_os_windows())