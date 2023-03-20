import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk

def scrape_and_save(url):
    html=requests.get(url)
    soup = BeautifulSoup(html.content,"html.parser")

    with open('output.csv', mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for element in soup.find_all("a"):
            writer.writerow([element.text])

def main():
    def start_scraping():
        url = url_entry.get()
        scrape_and_save(url)

    root = tk.Tk()
    root.geometry("400x150")
    root.title("スクレイピングアプリ")

    frame1 = tk.Frame(root, padx=10, pady=10)
    frame1.pack(side=tk.TOP)

    label1 = tk.Label(frame1, text="URLを入力してください")
    label1.pack(side=tk.TOP)

    url_entry = tk.Entry(frame1, width=50)
    url_entry.pack(side=tk.TOP)

    button1 = tk.Button(frame1, text="スクレイピング開始", command=start_scraping)
    button1.pack(side=tk.TOP)

    root.mainloop()

if __name__ == '__main__':
    main()
