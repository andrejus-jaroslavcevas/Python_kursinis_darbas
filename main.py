from tkinter import *
import sqlite3
import csv

langas = Tk()
langas.title('Duomenu baze')
langas.geometry("400x600")

conn = sqlite3.connect('zaideju_sarasas.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS komanda (
        vardas text,
        pavarde text,
        pozicija text,
        amzius integer,
        komanda text
        )""")


def ivesti():
    conn = sqlite3.connect('zaideju_sarasas.db')
    c = conn.cursor()
    c.execute("INSERT INTO komanda VALUES(:vardas, :pavarde, :pozicija, :amzius, :komanda)",
              {
                  'vardas': vardas.get(),
                  'pavarde': pavarde.get(),
                  'pozicija': pozicija.get(),
                  'amzius': amzius.get(),
                  'komanda': komanda.get()
              })

    conn.commit()
    conn.close()

    vardas.delete(0, END)
    pavarde.delete(0, END)
    pozicija.delete(0, END)
    amzius.delete(0, END)
    komanda.delete(0, END)


def sarasas():
    conn = sqlite3.connect('zaideju_sarasas.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM komanda")
    irasai = c.fetchall()

    rodyti_sarasa = ''
    for irasas in irasai:
        rodyti_sarasa += str(irasas) + " " + "\n"

    rodyti_irasus = Label(langas, text=rodyti_sarasa)
    rodyti_irasus.grid(row=12, column=0, columnspan=2)

    csv_mygtukas = Button(langas, text="Issaugoti i csv", command=lambda: irasyti_i_csv(irasai))
    csv_mygtukas.grid(row=index+1, column=0)

    conn.commit()
    conn.close()


def istrinti():
    conn = sqlite3.connect('zaideju_sarasas.db')
    c = conn.cursor()
    c.execute("DELETE from komanda WHERE oid = " + istrinimas.get())
    istrinimas.delete(0, END)
    conn.commit()
    conn.close()


def atnaujinti():
    conn = sqlite3.connect('zaideju_sarasas.db')
    c = conn.cursor()

    iraso_id = istrinimas.get()

    c.execute("""UPDATE komanda SET
        vardas = :vardas,
        pavarde = :pavarde,
        pozicija = :pozicija,
        amzius = :amzius,
        komanda = :komanda

        WHERE oid = :oid""",
              {'vardas': vardas_redagavimas.get(),
               'pavarde': pavarde_redagavimas.get(),
               'pozicija': pozicija_redagavimas.get(),
               'amzius': amzius_redagavimas.get(),
               'komanda': komanda_redagavimas.get(),
               'oid': iraso_id
               })
    conn.commit()
    conn.close()

    redagavimas.destroy()


def redaguoti():
    global redagavimas
    redagavimas = Tk()
    redagavimas.title('Atnaujinti duomenis')
    redagavimas.geometry("400x400")
    conn = sqlite3.connect('zaideju_sarasas.db')
    c = conn.cursor()
    iraso_id = istrinimas.get()

    c.execute("SELECT * FROM komanda WHERE oid = " + iraso_id)
    irasai = c.fetchall()

    global vardas_redagavimas
    global pavarde_redagavimas
    global pozicija_redagavimas
    global amzius_redagavimas
    global komanda_redagavimas

    vardas_redagavimas = Entry(redagavimas, width=30)
    vardas_redagavimas.grid(row=0, column=1, padx=20, pady=(10, 0))
    pavarde_redagavimas = Entry(redagavimas, width=30)
    pavarde_redagavimas.grid(row=1, column=1)
    pozicija_redagavimas = Entry(redagavimas, width=30)
    pozicija_redagavimas.grid(row=2, column=1)
    amzius_redagavimas = Entry(redagavimas, width=30)
    amzius_redagavimas.grid(row=3, column=1)
    komanda_redagavimas = Entry(redagavimas, width=30)
    komanda_redagavimas.grid(row=4, column=1, pady=5)

    vardas_label = Label(redagavimas, text="Vardas")
    vardas_label.grid(row=0, column=0, pady=(10, 0))
    pavarde_label = Label(redagavimas, text="Pavarde")
    pavarde_label.grid(row=1, column=0)
    pozicija_label = Label(redagavimas, text="Pozicija")
    pozicija_label.grid(row=2, column=0)
    amzius_label = Label(redagavimas, text="Amzius")
    amzius_label.grid(row=3, column=0)
    komanda_label = Label(redagavimas, text="Komanda")
    komanda_label.grid(row=4, column=0)

    for irasas in irasai:
        vardas_redagavimas.insert(0, irasas[0])
        pavarde_redagavimas.insert(0, irasas[1])
        pozicija_redagavimas.insert(0, irasas[2])
        amzius_redagavimas.insert(0, irasas[3])
        komanda_redagavimas.insert(0, irasas[4])

    mygtukas3 = Button(redagavimas, text="Issaugoti irasa", command=atnaujinti)
    mygtukas3.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


vardas = Entry(langas, width=30)
vardas.grid(row=0, column=1, padx=20, pady=(10, 0))
pavarde = Entry(langas, width=30)
pavarde.grid(row=1, column=1)
pozicija = Entry(langas, width=30)
pozicija.grid(row=2, column=1)
amzius = Entry(langas, width=30)
amzius.grid(row=3, column=1)
komanda = Entry(langas, width=30)
komanda.grid(row=4, column=1, pady=5)
istrinimas = Entry(langas, width=30)
istrinimas.grid(row=9, column=1)

vardas_label = Label(langas, text="Vardas")
vardas_label.grid(row=0, column=0, pady=(10, 0))
pavarde_label = Label(langas, text="Pavarde")
pavarde_label.grid(row=1, column=0)
pozicija_label = Label(langas, text="Pozicija")
pozicija_label.grid(row=2, column=0)
amzius_label = Label(langas, text="Amzius")
amzius_label.grid(row=3, column=0)
komanda_label = Label(langas, text="Komanda")
komanda_label.grid(row=4, column=0)
istrinti_label = Label(langas, text="Pasirinkti ID")
istrinti_label.grid(row=9, column=0, pady=5)

mygtukas = Button(langas, text="Ivesti", command=ivesti)
mygtukas.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

mygtukas1 = Button(langas, text="Rodyti sarasa", command=sarasas)
mygtukas1.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

mygtukas2 = Button(langas, text="Istrinti irasa", command=istrinti)
mygtukas2.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

mygtukas3 = Button(langas, text="Redaguoti irasa", command=redaguoti)
mygtukas3.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

conn.commit()
conn.close()

langas.mainloop()
