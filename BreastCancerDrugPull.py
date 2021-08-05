from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv

list_of_agents = []
data_output = []
space = " "
with open('list of agents.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        list_of_agents.append(row)

def func(name):
    original_name = name
    drug_name = name
    if space in drug_name:
        drug_name = drug_name.replace(" ", "%20")
    URL = 'https://ndclist.com/?s=' + drug_name
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(URL,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    links = []
    NDC_Num = []
    cor_ndc_num = []
    print(drug_name)
    if soup.find_all('p', string="No results found"):
        write = str(drug_name + " was blank!")
        blank_entry = ["00000000000", write]
        data_output.append(blank_entry)
        pass
    else:
        for tr in soup.find_all('tr')[1:]:
            tds = tr.find_all('td')[1:6]
            alink = tds[0].find('a', href=True)
            if alink.text:
                links.append(alink['href'])

        for x in links:
            URLz = x
            reqz = Request(URLz, headers=hdr)
            pagez = urlopen(reqz)
            soupz = BeautifulSoup(pagez, 'html.parser')
            for product_pack in soupz.find('ul', id="product-packages"):
                Ndcnum = product_pack.text
                NDC_Num.append(Ndcnum)

        for x in NDC_Num:
            split_num = x.split("-")
            one = split_num[0]
            two = split_num[1]
            three = split_num[2]
            if len(one) != 5:
                one = str("0" + one)
            elif len(two) != 4:
                two = str("0" + two)
            elif len(three) != 2:
                three = str("0" + three)
            else:
                print("Error in converting NDC from 10 digits to 11 digits")
            new_num = one + two + three
            if len(new_num) != 11:
                print(new_num)
                print("Error, new_num not 11")
            else:
                cor_ndc_num.append(new_num)

        for x in cor_ndc_num:
            new_entry = [x, original_name]
            data_output.append(new_entry)

for x in list_of_agents:
    print("running " + x)
    func(x)
    print("finished "+ x)

print(data_output)

with open('data_output.csv', 'a+', newline="") as output_file:
    fieldnames = ["NDC NUMBER", "DRUG NAME"]
    writer = csv.writer(output_file)
    writer.writerow(fieldnames)
    writer.writerows(data_output)

#need to make this 1) check the NDC code for 11 digit format (5-4-2)
#2) if the NDC is incorrect then it will count the first group, fix it if it is wrong
#3) if the first part of the NDC is correct then it will check the second group


"""<p class="text-info gi-1-5x">Search results for <em>Fam-trastuzumab Deruxtecan-nxki</em></p>
<p>No results found</p>"""




