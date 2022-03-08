import sys,os

from mmgui import App,BrowserWindow,Menu,MenuSeparator,run_on_ui_thread

win = None

def open_file():
    file = win.show_file_dialog_for_file("打开文件", "*.txt;*.jpg;*.webm")
    print(file[0])
    str = open_f(file)
    return str

def open_f(msg):
    file = os.path.normpath(msg[0])
    filetype = file.split(".")[-1]
    print(filetype)
    if filetype == "txt":
        file = os.path.normpath(msg[0])
        if file and len(file) > 0:
            f = open(file, 'r')
            con = f.read()
            str = ["txt",file, con]
            f.close()
            return str
        else:
            return None

    elif filetype == "jpg":
        str = ["jpg",msg[0]]
        return str
    elif filetype == "webm":
        str = ["webm",msg[0]]
        return str
    else:
        str = ["no_filetype"]
        return str

def save_file(msg):
    data = msg[1]
    file = os.path.normpath(msg[0])
    with open(file,'w',encoding="utf-8") as f:
        if f.write(data):
            f.close()
            return 1
        else:
            f.close()
            return None

def send_message(msg):
    if msg == "open":
        win.webview.send_message_to_js("open")
    if msg == "save":
        win.webview.send_message_to_js("save")

def on_create(ctx):

    menu = Menu()
    file_menu = Menu(title="file")
    file_menu.append(Menu(title="open file",on_click=lambda e: send_message("open")))
    file_menu.append(MenuSeparator())
    file_menu.append(Menu(title="save file",on_click=lambda e: send_message("save")))
    file_menu.append(MenuSeparator())
    file_menu.append(Menu(title="exit", on_click=lambda e: app.exit()))
    menu.append(file_menu)


    global win

    win = BrowserWindow({
        "title": "openFileDemo",
        "height": 600,
        "width": 800,
        "dev_move": True,
        "menu": menu
    })
    win.webview.bind_function("open_file",open_file)
    win.webview.bind_function("open",open_f)
    win.webview.bind_function("save_file",save_file)
    win.webview.load_file(os.path.join(os.path.dirname(os.path.abspath(__file__)),"openFileDemo.html"))
    win.show()

def main():
    app = App(headless=False)
    global win
    win = None
    app.on("create",on_create)
    app.run()

main()






