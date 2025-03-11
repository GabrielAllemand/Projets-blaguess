import pyjokes

def tell_joke(lang="en"):
	print(pyjokes.get_joke(language=lang))

if __name__ == "__main__":
	lang = input("Choisissez une langues (en, de, es, it, gl): ")
	joke_type= input("choisissez une catégorie de blagues (neutral, chuck, all): ")
	tell_joke(lang, joke_type)
