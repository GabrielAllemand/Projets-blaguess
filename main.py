import pyjokes

def tell_joke(lang="en"):
        print(pyjokes.get_joke(language=lang))

if __name__ == "__main__":
	 
        lang = input("Choisissez une langue (en, de, es, it, gl): ")

        lang = input("Choisissez une languet (en, de, es, it, gl): ")
        tell_joke(lang)






	lang = input("Choisissez une langue (en, de, es, it, gl): ")
	joke_type= input("choisissez une catégorie de blagues (neutral, chuck, all): ")
	tell_joke(lang, joke_type)
  master
