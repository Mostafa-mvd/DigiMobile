import requests, bs4, os


txt_file_path = os.path.dirname(__file__) + r"\phones_name.txt"
phones_list = []
swap = True
page_number = 1


while swap:
    try:
        req = requests.get("https://www.digikala.com/search/category-mobile-phone/?pageno={}&sortby=4".format(page_number))
        page_number += 1

        if req.status_code == 200:
            soup = bs4.BeautifulSoup(req.text, "html.parser")

            ul_tags = soup.find_all("ul", attrs={"class": "c-listing__items"})
            li_tags = ul_tags[0].find_all("li")

            for li_tag in li_tags:
                div_tag = li_tag.find("div")

                if div_tag != None:
                    phone_name = div_tag.get("data-title-en")
                    phones_list.append(phone_name)
        else:
            print(req.status_code)
            swap = False
    except IndexError: #index error means we are in the last page of site
        swap = False


with open(txt_file_path, "w") as txt_file:
    txt_file.write("lenght of list is: " + str(len(phones_list)) + "\n")

    for idx, phone in enumerate(phones_list):
        txt_file.write(str(idx + 1) + " : " + phone + "\n")





