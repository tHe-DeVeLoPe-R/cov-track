from tkinter import *

import matplotlib.pyplot as plt
import requests
import bs4
import threading

count_div = []
readable_data_ww = ""
readable_data_cw = ""
readable_data_cw2 = ""
data_headings = ['Covid-19 Cases', 'Deaths', 'Recoveries']
i = -1
url_world_wide = "https://worldometers.info/coronavirus/"


def worldWideDetail():
    global readable_data_ww, i, data_headings, url_world_wide

    data = requests.get(url_world_wide)
    html_data = bs4.BeautifulSoup(data.text, 'html.parser')
    # print(html_data)

    count_div = html_data.find("div", class_="content-inner").findAll("div", class_="maincounter-number")

    for block in count_div:
        i += 1
        count = block.find("span", class_=None).get_text()
        readable_data_ww += data_headings[i] + " : " + count + '\n' + '\n' + '\n'
    i = -1

    #drawGraph(count_div[1].getText(), count_div[2].getText())

    results.config(text=readable_data_ww, font=("jost", 13, "bold"))
    readable_data_ww = ""


def country_1_Detail():
    global readable_data_cw, i, data_headings

    country = entry1.get()

    try:
        url_country_wise_1 = "https://worldometers.info/coronavirus/country/" + country

        data = requests.get(url_country_wise_1)
        html_data = bs4.BeautifulSoup(data.text, 'html.parser')
        count_div = html_data.find("div", class_="content-inner").findAll("div", class_="maincounter-number")

        for block in count_div:
            i += 1
            count = block.find("span", class_=None).get_text()
            readable_data_cw += data_headings[i] + " : " + count + '\n' + '\n' + '\n'
        i = -1
        dataType_country_1.config(text="Data For " + country, font=("jost", 15, "bold"), fg='purple')
        country1_results.config(text=readable_data_cw, font=("jost", 13, "bold"))
        readable_data_cw = ""
        country = ""

    except AttributeError:
        country1_results.config(text="oops! country name 1 is not available", font=("jost", 13, "bold"))


def country_2_Detail():
    global readable_data_cw2, i, data_headings

    country2 = entry2.get()

    try:
        url_country_wise_2 = "https://worldometers.info/coronavirus/country/" + country2

        data2 = requests.get(url_country_wise_2)
        html_data2 = bs4.BeautifulSoup(data2.text, 'html.parser')
        count_div2 = html_data2.find("div", class_="content-inner").findAll("div", class_="maincounter-number")

        for block in count_div2:
            i += 1
            count = block.find("span", class_=None).get_text()
            readable_data_cw2 += data_headings[i] + " : " + count + '\n' + '\n' + '\n'
        i = -1
        dataType_country_2.config(text="Data For " + country2, font=("jost", 15, "bold"), fg='purple')
        country2_results.config(text=readable_data_cw2, font=("jost", 13, "bold"))
        readable_data_cw2 = ""
        country2 = ""

    except AttributeError:
        country2_results.config(text="oops! country name 2 is not available", font=("jost", 13, "bold"))


def runCountryWideThread():
    t1 = threading.Thread(target=country_1_Detail, args='')
    t2 = threading.Thread(target=country_2_Detail, args='')
    t3 = threading.Thread(target=worldWideDetail, args='')

    t1.start()
    t2.start()
    t3.start()


def drawGraph(x, y):
    # a = x[1:len(x) - 1]
    # b = y[1:len(y) - 1]
    #
    # a = a.replace(',', '')
    # b = b.replace(',', '')
    #
    # a = int(a)
    # b = int(b)
    #
    # a/=10000
    # b/=10000
    pass


root = Tk()

root.geometry("1200x650+20+20")
root.resizable(width=False, height=False)
root.title("Covid Tracker - Live")
bg_img = PhotoImage(file='bgimg.png')
root.iconphoto(False, bg_img)
background = Label(root, image=bg_img, width=800, height=650)
background.place(x=0, y=0)

heading = Label(root, text="Covid-19", fg="red", font=("jost", 25, 'bold'))
heading.place(x=370, y=50)

entryLabel = Label(root, text="Now You Can Check Multiple results in a Single click", font=("jost", 16, "bold"))
entryLabel.place(x=180, y=120)

entry1 = Entry(root, width=40, borderwidth=3, fg="green", font=("jost", 13, "bold"))
entry1.place(x=270, y=200)

entry2 = Entry(root, width=40, borderwidth=3, fg="green", font=("jost", 13, "bold"))
entry2.place(x=270, y=250)

btn1 = Button(root, font=("jost", 10, "bold"), text="Check Results", bg='red', fg='white', command=runCountryWideThread)
btn1.place(x=280, y=300)

dataType = Label(root, text="world-Wide Data", font=("jost", 15, "bold"), fg='purple')
dataType.place(x=200, y=400)

results = Label(root, text=" World wide data will appear here", font=("jost", 15, "bold"), fg='purple')
results.place(x=200, y=450)

dataType_country_1 = Label(root, text=" ", font=("jost", 15, "bold"), fg='purple')
dataType_country_1.place(x=850, y=50)

country1_results = Label(root, text=" ", font=("jost", 15, "bold"), fg='purple')
country1_results.place(x=850, y=110)

separating_line = Label(root, text="----------------------------- ", font=("jost", 15, "bold"), fg='purple')
separating_line.place(x=850, y=290)

dataType_country_2 = Label(root, text=" ", font=("jost", 15, "bold"), fg='purple')
dataType_country_2.place(x=850, y=350)

country2_results = Label(root, text=" ", font=("jost", 15, "bold"), fg='purple')
country2_results.place(x=850, y=410)

root.mainloop()
