import requests
import tkinter as tk
import json


url = "https://genius-song-lyrics1.p.rapidapi.com/songs/chart"

w = tk.Tk()

w.geometry("500x300")

label = tk.Label(
    text="day, week, month",
    bg="white", 
    fg="black"
)
label.pack()

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

frm_form.pack()


lbl_time = tk.Label(master=frm_form, text="Time:")
ent_time = tk.Entry(master=frm_form, width=50)

lbl_time.grid(row=0, column=0)
ent_time.grid(row=0, column=1)
 
lbl_genre = tk.Label(master=frm_form, text="Genre:")
ent_genre = tk.Entry(master=frm_form, width=50)

lbl_genre.grid(row=1, column=0)
ent_genre.grid(row=1, column=1)

def show():
    get_time = ent_time.get()
    get_genre = ent_genre.get()
    querystring = {"time_period":"{}".format(get_time),
    "chart_genre":"{}".format(get_genre),
    "per_page":"5",
    "page":"1"
    }

    headers = {
        "X-RapidAPI-Key": "ff2c859cf0msh6ab4cd32f934a2dp1a52a8jsn039fdc4a2f6a",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json1 = json.loads(response.text)

    show_songs = json1['response']['chart_items'][0]['item']['full_title']
    text.insert(tk.END, '{}\n'.format(show_songs))
    print(show_songs)

text = tk.Text(width=50, height=9)
text.pack()

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Push", command=show)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

w.mainloop()