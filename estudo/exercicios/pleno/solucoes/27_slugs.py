"""Solucao de pleno/27_slugs.py. Tente resolver o enunciado antes de abrir."""

_ACENTOS = str.maketrans(
    {
        "á": "a",
        "à": "a",
        "ã": "a",
        "â": "a",
        "ä": "a",
        "é": "e",
        "è": "e",
        "ê": "e",
        "ë": "e",
        "í": "i",
        "ì": "i",
        "î": "i",
        "ï": "i",
        "ó": "o",
        "ò": "o",
        "õ": "o",
        "ô": "o",
        "ö": "o",
        "ú": "u",
        "ù": "u",
        "û": "u",
        "ü": "u",
        "ç": "c",
    }
)


def slugificar(texto: str) -> str:
    if not isinstance(texto, str):
        raise ValueError("texto invalido")
    pedacos: list[str] = []
    for caractere in texto.lower().translate(_ACENTOS):
        pedacos.append(caractere if caractere.isalnum() else "-")
    slug = "".join(pedacos)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def slugs_unicos(textos: list[str]) -> list[str]:
    contagem: dict[str, int] = {}
    usados: set[str] = set()
    saida: list[str] = []
    for texto in textos:
        base = slugificar(texto) or "item"
        contagem[base] = contagem.get(base, 0) + 1
        if contagem[base] == 1 and base not in usados:
            escolhido = base
        else:
            numero = contagem[base]
            escolhido = f"{base}-{numero}"
            while escolhido in usados:
                numero += 1
                escolhido = f"{base}-{numero}"
            contagem[base] = numero
        usados.add(escolhido)
        saida.append(escolhido)
    return saida


if __name__ == "__main__":
    from _rodar import rodar

    rodar(slugificar=slugificar, slugs_unicos=slugs_unicos)
