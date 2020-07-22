import sqlite3


class swtor_eroberung():
    def __init__(self):
        self.chars = []
        self.eroberung_finished = False
        self.db = "swtor.db"
        
    def add_names_to_database(self):
        print("[Console]: Wenn alle Chars eingetragen wurden die Taste (b) drücken... ")
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        while True:
            eingabe = input("[Console]: Name eintragen :")
            if eingabe == "b":
                print("[Console]: Sind das alle Chars die eingetragen werden sollen?")
                print(self.chars)
                abbruch = input("[Console]: [j/n] ?")
                if abbruch == "j":
                    print("[Console]: füge chars zur datenbank hinzu...")
                    for i in range(len(self.chars)):
                        char = self.chars[i]
                        print("[Console]: trage: {} in Datenbank ein...".format(char))
                        c.execute("INSERT INTO eroberung VALUES (:Name, :done)", {"Name": char, "done": False })
                        c.execute("INSERT INTO meister_weekly VALUES (:Name, :done)", {"Name": char, "done": False})
                        c.execute("INSERT INTO vet_weekly VALUES (:Name, :done)", {"Name": char, "done": False})

                    conn.commit()
                    conn.close()
                    print("[Console]: chars erfolgreich eingetragen...")
                    break
                else:
                    pass
            else:
                if eingabe!="":
                    self.chars.append(eingabe)
                else:
                    print("Enter drücken hilft nicht immer...")

    def add_eroberung_done(self,char):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        try:
            c.execute("UPDATE eroberung set done = ? where name=?",[1,char])
        except Exception as e:
            print("[Exception]: {}".format(e))
        conn.commit()
        conn.close()
    
    def add_meister_weekly_done(self,char):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        try:
            c.execute("UPDATE meister_weekly set done = ? where name=?",[1,char])
        except Exception as e:
            print("[Exception]: {}".format(e))
        conn.commit()
        conn.close()
    
    def add_vet_weekly_done(self,char):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        try:
            c.execute("UPDATE vet_weekly set done = ? where name=?",[1,char])
        except Exception as e:
            print("[Exception]: {}".format(e))
        conn.commit()
        conn.close()
    
    
    def show_eroberung_done(self):
        punkte = 0
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute("SELECT * FROM eroberung")
        liste = c.fetchall()
        print("--------------------<Eroberungs Liste>--------------------")
        check_done = False
        check_open = False
        for i in range(len(liste)):
            char = liste[i]
            if char[1] == True:
                check_done = True
            if char[1] == False:
                check_open = True
        if check_open:
            print("-----------<Offen>-----------")
            for i in range(len(liste)):
                char = liste[i]
                if char[1]== False:
                    print("{}".format(char[0]))
            print("-----------------------------")
        if check_done:
            print("-------<Abgeschlossen>-------")
            for i in range(len(liste)):
                char = liste[i]
                if char[1]== True:
                    print("{}".format(char[0]))
                    punkte = punkte + 50000
        print("-----------------------------")
        print("Du hast min. {} Eroberungs Punkte gemacht".format(punkte))
        print("---------------------------------------------------------")
        conn.close()
    
    def show_vet_weekly_done(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute("SELECT * FROM vet_weekly")
        liste = c.fetchall()
        print("----------------------<Vet Liste>----------------------")
        check_done = False
        check_open = False
        for i in range(len(liste)):
            char = liste[i]
            if char[1] == True:
                check_done = True
            if char[1] == False:
                check_open = True
        if check_open:
            print("-----------<Offen>-----------")
            for i in range(len(liste)):
                char = liste[i]
                if char[1]== False:
                    print("{}".format(char[0]))
            print("-----------------------------")
        if check_done:
            print("-------<Abgeschlossen>-------")
            for i in range(len(liste)):
                char = liste[i]
                if char[1]== True:
                    print("{}".format(char[0]))
            print("-----------------------------")
        print("---------------------------------------------------------")
        conn.close()

    def show_meister_weekly_done(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute("SELECT * FROM meister_weekly")
        liste = c.fetchall()
        print("--------------------<Meister Liste>--------------------")
        check_done = False
        check_open = False
        for i in range(len(liste)):
            char = liste[i]
            if char[1] == True:
                check_done = True
            if char[1] == False:
                check_open = True
        if check_open:
            print("-----------<Offen>-----------")
            for i in range(len(liste)):
                char = liste[i]
                if char[1]== False:
                    print("{}".format(char[0]))
            print("-----------------------------")
        if check_done:
            print("-------<Abgeschlossen>-------")
            for i in range(len(liste)):
                char = liste[i]
                if char[1]== True:
                    print("{}".format(char[0]))
            print("-----------------------------")
        print("---------------------------------------------------------")
        conn.close()
    
    def check_char_existing(self,char):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute("select * from eroberung where name = ?",[char])
        char = c.fetchone()
        if char == None:
            return False
        else:
            return True
        conn.close()

    def reset_eroberung(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        print("Setze Eroberung zurück...")
        c.execute("SELECT * FROM eroberung")
        liste = c.fetchall()
        for i in range(len(liste)):
            r_char = liste[i]
            print("setze {} zurück".format(r_char[0]))
            c.execute("UPDATE vet_weekly set done = ? where name=?",[0,r_char[0]])
            c.execute("UPDATE meister_weekly set done = ? where name=?",[0,r_char[0]])
            c.execute("UPDATE eroberung set done = ? where name=?",[0,r_char[0]])
        conn.commit()
        conn.close()
   


    def main_menu(self):
        while True:
            print("--------------------------------------------------------<Menu>----------------------------------------------------------")
            print("")
            print("zum wählen [Taste] druecken")
            print("")
            print("Eroberung liste: [1]")
            print("")
            print("Vet Weekly liste: [2]")
            print("")
            print("Meister Weekly liste: [3]")
            print("")
            print("Char/s hinzufügen: [4]")
            print("")
            print("Char abhaken: [5]")
            print("")
            print("Eroberung zurücksetzen[6]")
            print("")
            print("")
            print(" _   _            _           _          _                       ____   _______          _                           ")
            print("| | / /  ______  |_|         | |      __| |__   ____    ______  |  __| |  ___  |  ____  |_|  _____   ______   ______ ")
            print("| |/ /  |  __  |  _   _____  | |____ |__   __| | ___|  |  __  | | |_   | |   | | |  __|  _  |  ___| |  __  | |  __  |")
            print("| |\ \  | |  | | | | |  _  | |  __  |   | |    |___ |  | |__| | |  _|  | |___| | | |    | | | |___  | |__| | | |  | |")
            print("|_| \_\ |_|  |_| |_| |___  | |_|  |_|   |_|    |____|  |______| |_|    |_______| |_|    |_| |_____| |______| |_|  |_|")
            print("                      ___| |")
            print("                     |_____|")
            print("                            ")
            print("Version 0.1")
            print("------------------------------------------------------------------------------------------------------------------------")
            eingabe = input("[Console]: ")
            
        
            if eingabe == "1":
                self.show_eroberung_done()
                input("[Console]: Enter druecken zum fortfahren...")
            elif eingabe == "2":
                self.show_vet_weekly_done()
                input("[Console]: Enter druecken zum fortfahren...")
            elif eingabe == "3":
                self.show_meister_weekly_done()
                input("[Console]: Enter druecken zum fortfahren...")
            elif eingabe == "6":
                self.reset_eroberung()
            elif eingabe == "4":
                self.add_names_to_database()
            elif eingabe == "5":
                while True:
                    char = input("[Console]: welcher char soll abgehakt werden?")
                    if char == "b":
                        break
                    existing = self.check_char_existing(char)
                    if existing == True:
                        eingabe2 = input("[Console]: Meister[1] Vet[2] Eroberung[3] ")
                        if eingabe2 == "1":
                            result = self.add_meister_weekly_done(char)
                            break
                        elif eingabe2 == "2":
                            result = self.add_vet_weekly_done(char)
                            break
                        elif eingabe2 == "3":
                            result = self.add_eroberung_done(char)
                            break
                        elif eingabe2 == "b":
                            break
                        else:
                            print("[Console]: Diesen Befehl kenne ich nicht!!")
                    else:
                        print("[Console]: '{}' ist nicht in der Datenbank vorhanden...".format(char))
                        








def start_screen():
    print("-------------------------------------------------------<SWTOR>----------------------------------------------------------")
    print("""                                             _______         _______                                                                          
                                            |       |       |       |                                                                          
                                            |   O   |       |   O   |                                                                  
                                            |_______|       |_______|                                                                   
                                             ________________________                                                               
                                            |                        |                                                         
                                            |________________________|                                                             
                                                                                                                                                  
                                          Skript Made By : BestITManSomalia                                                                                                                    
                                                                                                                                                   
                                                                                                      """)
    print("")
    print("")
    print("")
    print("")
    print("")
    input("[Console]: Enter druecken zum starten...")
    



if __name__ == "__main__":
    start_screen()
    x = swtor_eroberung()
    x.main_menu()
        
