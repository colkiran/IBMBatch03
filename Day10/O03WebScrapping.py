from bs4 import BeautifulSoup

with open("mypage.html", "r") as htmlfile:
    content = htmlfile.read()

    soup = BeautifulSoup(content, "lxml")

    tag = soup.find("h5")
    print(tag)

    print("-" * 60)
    tag = soup.find("h5").text
    print(tag)

    print("-" * 60)
    crdTitle = soup.findAll("h5")
    print(crdTitle)

    print("-" * 60)

    for ctitle in crdTitle:
        print(ctitle.text)

    print("-" * 60)

    cards = soup.findAll("div", class_="card")
    for card in cards:
        crd_title = card.h5.text
        prc = card.a.text.split()[-1]

        print(f"Training on {crd_title} will cost {prc}")