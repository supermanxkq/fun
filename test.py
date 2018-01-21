import tkinter
from tkinter import ttk
import tkinter.messagebox
import ssl
import json
import binascii
import random
from urllib.parse import quote
from urllib import request
import time
from tkinter import *

ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

with open('source_url.json', 'r') as f:
    config = json.load(f)

key_words = config['key_words']
seed_search_url = config['seed_search_url']


def get_html(site_url):
    req = request.Request(url=site_url, headers=headers)
    return request.urlopen(req).read()

class AddWidget(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        quit()

    def search(self):
        if self.num1_entry.get():
            total = 0
            for key_word in self.num1_entry.get().split(','):
                with open(key_word + '.txt', 'a') as f:
                    for i in range(1):
                        seed_search_url_decode = binascii.a2b_hex(seed_search_url).decode("utf8")
                        html = get_html(seed_search_url_decode + 'list/' + quote(key_word) + '/%d' % (i + 1)).decode(
                            'utf-8')
                        r = r'magnet:\?xt=urn:btih:\w+'
                        re_mp4 = re.compile(r)
                        mp4List = (re.findall(re_mp4, html))
                        mp4List = list(set(mp4List))
                        for url in mp4List:
                            total += 1
                            #tkinter.messagebox.showinfo('提示', str(total))
                            #tkinter.showinfo('写入' + str(total)+'个\n')

                            f.write(url + '\n')
                    time.sleep(random.uniform(2, 2.1))  # 为了保证服务器reset，多延迟一会儿，随机值防 ban
                    self.answer_label['text'] += '写入' + key_word+'的种子完毕！共'+str(total)+'个\n'
                # print('写入', key_word, '的种子完毕！')
            # print('=========共写入' + str(total) + '个种子！======')

    def init_gui(self):
        self.root.title('电影搜索神器')
        self.root.option_add('*tearOff', 'FALSE')

        self.grid(column=0, row=0, sticky='nsew')
        #
        # self.menubar = tkinter.Menu(self.root)
        #
        # self.menu_file = tkinter.Menu(self.menubar)
        # self.menu_file.add_command(label='退出', command=self.on_quit)
        #
        # self.menu_edit = tkinter.Menu(self.menubar)
        #
        # self.menubar.add_cascade(menu=self.menu_file, label='文件')
        # self.menubar.add_cascade(menu=self.menu_edit, label='退出')

        # self.root.config(menu=self.menubar)

        self.num1_entry = ttk.Entry(self, width=45)
        self.num1_entry.grid(column=1, row=2)


        self.calc_button = ttk.Button(self, text='搜索',
                                      command=self.search)
        self.calc_button.grid(column=0, row=3, columnspan=4)

        self.answer_frame = ttk.LabelFrame(self, text='结果',
                                           height=200)
        self.answer_frame.grid(column=0, row=4, columnspan=4, sticky='nesw',padx=10,pady=100)

        self.answer_label = ttk.Label(self.answer_frame, text='')
        self.answer_label.grid(column=0, row=0)

        ttk.Label(self, text='====下载电影====').grid(column=0, row=0,
                                         columnspan=8)
        ttk.Label(self, text='输入关键字').grid(column=0, row=2,
                                          sticky='w')

        ttk.Separator(self, orient='horizontal').grid(column=0,
                                                      row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)


if __name__ == '__main__':
    mainFrame = tkinter.Tk()
    mainFrame.geometry('500x500')
    AddWidget(mainFrame)

    mainFrame.mainloop()