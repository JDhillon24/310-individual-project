import wikipediaapi
import time

def wikiarticle():
    wiki = wikipediaapi.Wikipedia('en')
    while True:
        time.sleep(1.2)
        query = str(input("What would you like to learn about?"))
        time.sleep(1.2)
        print("Here is a brief summary on", query)
        query.replace(" ", "_")
        page_py = wiki.page(query).summary
        time.sleep(2)
        lines = page_py.split(". ")
        for x in lines:
            print(x)

        time.sleep(1.2)

        yesno = str(input("Would you like to learn anything else? (yes/no)"))

        if yesno == "yes":
            continue
        else:
            break



if __name__ == '__main__':
    wikiarticle()
