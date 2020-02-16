# -*- coding: utf-8 -*-
#########################################################################################################################################
####################################### THE HUNGER GAMES SIMULATOR (RELOADED) ###########################################################
############################################### BY AXEL BRUNETTA ########################################################################
################################################# BUILD 0.2.2.6 #########################################################################
#########################################################################################################################################
import tkinter as tk
import random
from PIL import Image, ImageTk

build = '0.2.2.6'

window = tk.Tk()
window.title('The HG Simulator (Build %s)' % (build))
firstframe = tk.Frame(master=window, bg='White')

secondframe = tk.Frame(master=window, bg='White')
secondframe.pack()


img = Image.open("mockingjay3.png")
gamelogo = ImageTk.PhotoImage(img)
logolabel = tk.Label(image=gamelogo, bg='White')
logolabel.image = gamelogo



lbl_hg = tk.Label(master=secondframe, text="Welcome to the Hunger Games simulator (Reloaded)!", font=('Helvetica',10,'bold'),height=5, width=55, bg='White')
lbl_hg.pack()
lbl_hg2 = tk.Label(master=secondframe, text="by Axel Brunetta",font=('Helvetica',10,'bold'), bg='White')
lbl_hg2.pack(pady=40)
logolabel.place(x=197.5, y=54)
bttn_start = tk.Button(master=secondframe, text="Start", fg='White', bg='Black',font=('Helvetica',8,'bold'),height=2, width=10, command=lambda:[logolabel.destroy(),lbl_hg.pack_forget(),lbl_hg2.pack_forget(),bttn_start.pack_forget(), secondframe.pack_forget(),window.quit()])
bttn_start.pack(pady=5)
    
window.mainloop()

firstframe.pack()

nbrofplayers=0

lbl_nbrpersosaffichage = tk.Label(master=firstframe,bg='White',text="Choose the number of players (>6)",height=3, width=45, fg='Black',font=('Helvetica',10,'bold'))
lbl_nbrpersosaffichage.pack()
def increase():
    value = int(lbl_nbrpersos["text"])
    lbl_nbrpersos["text"] = f"{value + 1}"
def decrease():
    value = int(lbl_nbrpersos["text"])
    lbl_nbrpersos["text"] = f"{value - 1}"
def getnumberofplayers():
    global nbrofplayers
    if int(lbl_nbrpersos["text"]) >= 6:
        nbrofplayers = int(lbl_nbrpersos["text"])
    else:
        window.destroy()
    
bttn_increase = tk.Button(master=firstframe, text="+", fg='White', bg='Black',font=('Helvetica',8,'bold'),width=10, command= increase)
bttn_increase.pack(pady=10)
lbl_nbrpersos = tk.Label(master=firstframe, text="0", font=('Helvetica',8,'bold'),width=10, bg='White')
lbl_nbrpersos.pack()
bttn_decrease = tk.Button(master=firstframe, text="-", fg='White', bg='Black',font=('Helvetica',8,'bold'),width=10, command= decrease)
bttn_decrease.pack(pady=10)
bttn_approvenbrofplayers = tk.Button(master=firstframe,width=8, text="Approve", fg='White', bg='Red',font=('Helvetica',8,'bold'), command=getnumberofplayers)
bttn_approvenbrofplayers.pack(pady=5)
bttn_next1 = tk.Button(master=firstframe, text="Next", width=8, fg='White', bg='Green',font=('Helvetica',8,'bold'), command=lambda:[lbl_nbrpersosaffichage.destroy(),bttn_decrease.destroy(),lbl_nbrpersos.destroy(),bttn_increase.destroy(),bttn_approvenbrofplayers.destroy(),bttn_next1.destroy(),firstframe.destroy(),window.quit()])
bttn_next1.pack(pady=5)

window.mainloop()


def essai():
    global g
    g = name_entry.get()
    lbl_name_entry.destroy()
    name_entry.destroy()
    bttn_ok.destroy()
    window.quit()
a=0
x=a+1
frame8 = tk.Frame(master=window,width=20, bg='White')
frame8.pack()
listejoueurs =[]
deadplayers = []
while a != nbrofplayers:
    lbl_name_entry = tk.Label(master=frame8, text="Player %s's name:" % (str(x)),font=('Helvetica',10,'bold'), bg='White',width=55)
    lbl_name_entry.pack(pady=10)
    name_entry = tk.Entry(master=frame8, bg='Grey', fg="White")
    name_entry.pack()
    bttn_ok =tk.Button(master=frame8, text="Ok", bg='Black',fg='White',font=('Helvetica',8,'bold'),command=essai)
    bttn_ok.pack(pady=30)
    window.mainloop()
    exec("player%d = %s" % (int(a), {
            "name": str(g),
            "location": "Cornucopia",
            "status": "Alive",
            "alliance_status": "none",
            "weapon1": "none",
            "weapon2": "none",
            "item1": "none",
            "item2": "none",
            "sponsor_item": "none",
            "killcount": "0"}))
    exec("listejoueurs.append(player%d)" % (int(a)))
    a += 1
    x += 1
    

frame8.pack_forget()
frame9 = tk.Frame(master=window, width=20, bg='White')
frame9.pack()

lbl_starthg = tk.Label(master=frame9, pady=20,text="Please press the button to start the Hunger Games:", bg='White', width=55,font=('Helvetica',10,'bold'))
lbl_starthg.pack()

bttn_starthg = tk.Button(master=frame9, pady=10, text="Start", fg='White', bg='Black',font=('Helvetica',8,'bold'), command=lambda:[lbl_starthg.destroy(),bttn_starthg.destroy(),frame9.destroy(),window.quit()])
bttn_starthg.pack(pady=30)

window.mainloop()

weaponnames = ["wooden sword","sword","pair of cisors","knife","sharp piece of metal","stun gun","baseball bat","spear","bar mace","blowgun","machete","sickle","throwing axe","trident"]
verbnames = ["runs and takes", "picks up", "manages to get","grabs"]
itemnames = ["rope", "pair of binoculars", "bear trap", "bag full of canned food", "bag full of medics and bandages", "camo outfit", "lighter", "flashlight", "survival blanket"]
sponsorshipitemnames = ['foldable ladder', 'hot meal', 'hot chocolate','face cleansing kit','lollipop']
a=0

def randomorder(nbrofplayers):
    listforrandomorder = []
    for x in range(int(nbrofplayers)):
        listforrandomorder.append(str(x))
    random.shuffle(listforrandomorder)
    return listforrandomorder

def getweaponatcornucopia(playerx,listnbr):
    zerooneortwoforweapons = random.randint(0,13)
    if zerooneortwoforweapons == 0: #cas ou le joueur n'a rien
        playername = listejoueurs[x]["name"]
        listepickedweapon[listnbr] = tk.Label(master=frame11, text="%s couldn't get anything, so he/she fled." % (playername), bg='White',font=('Helvetica',10,'bold'))
        listepickedweapon[listnbr].pack()
    elif zerooneortwoforweapons == 2 or zerooneortwoforweapons == 3 or zerooneortwoforweapons == 13: #cas ou le joueur a un objet
        chosenitem1 = str(random.choice(itemnames))
        exec ("listejoueurs[%s][%s] = '%s'" % (str(playerx),"'item1'",chosenitem1))
        randomverb = str(random.choice(verbnames))
        playername = listejoueurs[x]["name"]
        listepickedweapon[listnbr] = tk.Label(master=frame11, text="%s %s a %s." % (playername,randomverb,chosenitem1), bg='White',font=('Helvetica',10,'bold'))
        listepickedweapon[listnbr].pack()
    elif zerooneortwoforweapons == 4 or zerooneortwoforweapons == 5 or zerooneortwoforweapons == 6 or zerooneortwoforweapons == 1: #cas ou le joueur a une arme
        chosenweapon1 = str(random.choice(weaponnames))
        exec ("listejoueurs[%s][%s] = '%s'" % (str(playerx),"'weapon1'",chosenweapon1))
        randomverb = str(random.choice(verbnames))
        playername = listejoueurs[x]["name"]
        listepickedweapon[listnbr] = tk.Label(master=frame11, text="%s %s a %s." % (playername,randomverb,chosenweapon1), bg='White',font=('Helvetica',10,'bold'))
        listepickedweapon[listnbr].pack()
    elif zerooneortwoforweapons == 7 or zerooneortwoforweapons == 8 or zerooneortwoforweapons == 9 or zerooneortwoforweapons == 10 or zerooneortwoforweapons == 11 or zerooneortwoforweapons == 12: #cas ou le joueur a une arme et un objet
        chosenweapon1 = str(random.choice(weaponnames))
        chosenitem1 = str(random.choice(itemnames))
        exec ("listejoueurs[%s][%s] = '%s'" % (str(playerx),"'weapon1'",chosenweapon1))
        exec ("listejoueurs[%s][%s] = '%s'" % (str(playerx),"'item1'",chosenitem1))
        randomverb = str(random.choice(verbnames))
        playername = listejoueurs[x]["name"]
        listepickedweapon[listnbr] = tk.Label(master=frame11, text="%s %s a %s and a %s." % (playername,randomverb,chosenweapon1,chosenitem1), bg='White',font=('Helvetica',10,'bold'))
        listepickedweapon[listnbr].pack()
    
                                                                                                                  
frame11 = tk.Frame(master=window, bg='White')
frame11.pack()

listepickedweapon =[]
listofplayersforfirstrun = randomorder(nbrofplayers)

listnbr = 0

day1 = tk.Label(frame11, width=70, text="Day 1", bg='White',font=('Helvetica',14,'bold'))                                                                        
day1.pack(pady=20)  
space = tk.Label(frame11, width=30, text="", bg='White' )                                                                        
space.pack()  

for x in listofplayersforfirstrun:
    x=int(x)
    exec ("listepickedweapon.append('lbl_pickedweapon%s')" % (str(x)))
    getweaponatcornucopia(x,listnbr)
    listnbr += 1
    bttn_next1 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next1.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
    bttn_next1.pack(pady=10)
    window.mainloop()


locations_list = ["forest","caves","mountains","river"]

zerooneortwo = random.randint(0,6)

def firstrun(nbrofplayers):
    listofplayersforfirstrun = randomorder(nbrofplayers)
    x=0
    while x != len(listofplayersforfirstrun):
        u = int(listofplayersforfirstrun[x])
        global j
        randomvalueforlocationevent = random.randint(0,9)
        
        if listejoueurs[u]["status"] != "dead":
            if randomvalueforlocationevent == 4 or randomvalueforlocationevent == 5 or randomvalueforlocationevent == 6 or randomvalueforlocationevent == 7 or randomvalueforlocationevent == 8 or randomvalueforlocationevent == 9: #run towards location
                
                name = listejoueurs[u]["name"]
                location = random.choice(locations_list)
                lbl_goestolocation = tk.Label(master=frame11, text="%s starts to run towards the %s." % (name, location),font=('Helvetica',10,'bold'), bg='White')
                lbl_goestolocation.pack()
                listejoueurs[u]['location'] = location
                bttn_next2 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next2.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
                bttn_next2.pack(pady=10)
            
            elif randomvalueforlocationevent == 0: #killed in a attempt to escape 
                
                name = listejoueurs[u]["name"]
                killerplayer = name
                killerplayerweapon = 'none'
                killerplayerstatus = "dead"
                while killerplayer == name or killerplayerweapon == 'none' or killerplayerstatus == 'dead':
                    j = random.randint(0,int(len(listejoueurs)-1))
                    killerplayer = listejoueurs[j]['name']
                    killerplayerweapon = listejoueurs[j]['weapon1']
                    killerplayerstatus = listejoueurs[j]['status']
                location = random.choice(locations_list)
                locationkilledsentencerandom = random.randint(0,1)
                if locationkilledsentencerandom == 0:
                    lbl_goestolocation = tk.Label(master=frame11, text="%s started to run towards the %s but was killed by %s using a %s." % (name, location, killerplayer, killerplayerweapon),font=('Helvetica',10,'bold'), bg='White')
                    lbl_goestolocation.pack()
                elif locationkilledsentencerandom == 1:
                    lbl_goestolocation = tk.Label(master=frame11, text="%s attempted to escape to the %s but was killed by %s with a %s." % (name, location,killerplayer, killerplayerweapon),font=('Helvetica',10,'bold'), bg='White')
                    lbl_goestolocation.pack()
                exec("deadplayers.append(listejoueurs[%d])" % (x))
                listejoueurs[j]['killcount'] = str(int(listejoueurs[j]['killcount'])+1)
                listejoueurs[u]["status"] = "dead"
                bttn_next2 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next2.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
                bttn_next2.pack(pady=10)
                
            elif randomvalueforlocationevent == 2 or randomvalueforlocationevent == 3 or randomvalueforlocationevent == 1: #wounded in a attempt to escape 
                
                name = listejoueurs[u]["name"]
                killerplayer = name
                killerplayerweapon = 'none'
                killerplayerstatus = "dead"
                while killerplayer == name or killerplayerweapon == 'none' or killerplayerstatus == 'dead':
                    j = random.randint(0,int(len(listejoueurs)-1))
                    killerplayer = listejoueurs[j]['name']
                    killerplayerweapon = listejoueurs[j]['weapon1']
                    killerplayerstatus = listejoueurs[j]['status']
                location = random.choice(locations_list)
                locationkilledsentencerandom = random.randint(0,1)
                if locationkilledsentencerandom == 0:
                    lbl_goestolocation = tk.Label(master=frame11, text="%s started to run towards the %s but was wounded by %s using a %s." % (name, location, killerplayer,killerplayerweapon),font=('Helvetica',10,'bold'), bg='White')
                    lbl_goestolocation.pack()
                elif locationkilledsentencerandom == 1:
                    lbl_goestolocation = tk.Label(master=frame11, text="%s attempted to escape to the %s but was wounded by %s with a %s." % (name, location,killerplayer, killerplayerweapon),font=('Helvetica',10,'bold'), bg='White')
                    lbl_goestolocation.pack()
                listejoueurs[u]['status'] = 'Wounded'
                listejoueurs[u]['location'] = location
                bttn_next2 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next2.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
                bttn_next2.pack(pady=10)
        x += 1
        window.mainloop()
    
        

if zerooneortwo == 0 or zerooneortwo == 1 or zerooneortwo == 2: #alliances
    randomallianceplayerlist = ['test']
    while len(randomallianceplayerlist) == 1:
        randomallianceplayerlist.remove(randomallianceplayerlist[0])
        alliancenumber = random.randint(2,int(nbrofplayers)-4)
        location = str(random.choice(locations_list))
        for x in range(0,alliancenumber):
            randomallianceplayer = random.randint(0,int(nbrofplayers-1))
            exec ("listejoueurs[%s][%s] = 'Alliance1'" % (str(randomallianceplayer),"'alliance_status'"))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(randomallianceplayer),"'location'", location))
            exec ("player%sname = listejoueurs[%s]['name']" % (str(x),str(randomallianceplayer)))
            exec ("randomallianceplayerlist.append(player%sname)" % (str(x)))
            print(listejoueurs)
        randomallianceplayerlist = list(dict.fromkeys(randomallianceplayerlist))
    alliance1txt = ", ".join('%02s'%x for x in randomallianceplayerlist)
    lbl_alliance1txt = tk.Label(master=frame11, text="%s decide to form an alliance." % (alliance1txt),font=('Helvetica',10,'bold'), bg='White')
    lbl_alliance1txt.pack()
    lbl_alliance1txt = tk.Label(master=frame11, text="They head to the %s." % (location),font=('Helvetica',10,'bold'), bg='White')
    lbl_alliance1txt.pack()
    bttn_next2 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next2.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
    bttn_next2.pack(pady=10)
    window.mainloop() 
    listofplayersforfirstrun = randomorder(nbrofplayers)
    x=0
    while x != len(listofplayersforfirstrun):
        u = int(listofplayersforfirstrun[x])
        if listejoueurs[u]["alliance_status"] != "Alliance1":
            randomvalueforlocationevent = random.randint(0,9)
            
            if listejoueurs[u]["status"] != "dead":
                if randomvalueforlocationevent == 4 or randomvalueforlocationevent == 5 or randomvalueforlocationevent == 6 or randomvalueforlocationevent == 7 or randomvalueforlocationevent == 8 or randomvalueforlocationevent == 9: #run towards location
                    
                    name = listejoueurs[u]["name"]
                    location = random.choice(locations_list)
                    lbl_goestolocation = tk.Label(master=frame11, text="%s starts to run towards the %s." % (name, location),font=('Helvetica',10,'bold'), bg='White')
                    lbl_goestolocation.pack()
                    listejoueurs[u]['location'] = location
                    bttn_next2 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next2.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
                    bttn_next2.pack(pady=10)
                
                elif randomvalueforlocationevent == 0: #killed in a attempt to escape 
                    
                    name = listejoueurs[u]["name"]
                    killerplayer = name
                    killerplayerweapon = 'none'
                    killerplayerstatus = "dead"
                    while killerplayer == name or killerplayerweapon == 'none' or killerplayerstatus == 'dead':
                        j = random.randint(0,int(len(listejoueurs)-1))
                        killerplayer = listejoueurs[j]['name']
                        killerplayerweapon = listejoueurs[j]['weapon1']
                        killerplayerstatus = listejoueurs[j]['status']
                    location = random.choice(locations_list)
                    locationkilledsentencerandom = random.randint(0,1)
                    if locationkilledsentencerandom == 0:
                        lbl_goestolocation = tk.Label(master=frame11, text="%s started to run towards the %s but was killed by %s using a %s." % (name, location, killerplayer, killerplayerweapon),font=('Helvetica',10,'bold'), bg='White')
                        lbl_goestolocation.pack()
                    elif locationkilledsentencerandom == 1:
                        lbl_goestolocation = tk.Label(master=frame11, text="%s attempted to escape to the %s but was killed by %s with a %s." % (name, location,killerplayer, killerplayerweapon),font=('Helvetica',10,'bold'), bg='White')
                        lbl_goestolocation.pack()
                    exec("deadplayers.append(listejoueurs[%d])" % (x))
                    listejoueurs[j]['killcount'] = str(int(listejoueurs[j]['killcount'])+1)
                    listejoueurs[u]["status"] = "dead"
                    bttn_next2 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next2.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
                    bttn_next2.pack(pady=10)
                    
                elif randomvalueforlocationevent == 2 or randomvalueforlocationevent == 3 or randomvalueforlocationevent == 1: #wounded in a attempt to escape 
                    
                    name = listejoueurs[u]["name"]
                    killerplayer = name
                    killerplayerweapon = 'none'
                    killerplayerstatus = "dead"
                    while killerplayer == name or killerplayerweapon == 'none' or killerplayerstatus == 'dead':
                        j = random.randint(0,int(len(listejoueurs)-1))
                        killerplayer = listejoueurs[j]['name']
                        killerplayerweapon = listejoueurs[j]['weapon1']
                        killerplayerstatus = listejoueurs[j]['status']
                    location = random.choice(locations_list)
                    locationkilledsentencerandom = random.randint(0,1)
                    if locationkilledsentencerandom == 0:
                        lbl_goestolocation = tk.Label(master=frame11, text="%s started to run towards the %s but was wounded by %s using a %s." % (name, location, killerplayer,killerplayerweapon),font=('Helvetica',10,'bold'), bg='White')
                        lbl_goestolocation.pack()
                    elif locationkilledsentencerandom == 1:
                        lbl_goestolocation = tk.Label(master=frame11, text="%s attempted to escape to the %s but was wounded by %s with a %s." % (name, location,killerplayer, killerplayerweapon),font=('Helvetica',10,'bold'), bg='White')
                        lbl_goestolocation.pack()
                    listejoueurs[u]['status'] = 'Wounded'
                    listejoueurs[u]['location'] = location
                    bttn_next2 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next2.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
                    bttn_next2.pack(pady=10)
            window.mainloop()
        x += 1


elif zerooneortwo == 3 or zerooneortwo == 4 or zerooneortwo == 5 or zerooneortwo == 6: #go to location
    firstrun(nbrofplayers)



listofplayersforfirstrun = randomorder(nbrofplayers)
x=0
while x != len(listofplayersforfirstrun):
    u = int(listofplayersforfirstrun[x])
    if listejoueurs[u]["status"] != "dead":
        if listejoueurs[u]["item1"] == "survival blanket": #sleeps well
            
            name = listejoueurs[u]["name"]
            lbl_survivalblanket = tk.Label(master=frame11, text="%s is ready for a good night's sleep thanks to his/her survival blanket." % (name),font=('Helvetica',10,'bold'), bg='White')
            lbl_survivalblanket.pack()
            bttn_next3 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
            window.mainloop()
            
        elif listejoueurs[u]["item1"] == "camo outfit": 
            
            name = listejoueurs[u]["name"]
            lbl_camooutfit = tk.Label(master=frame11, text="%s uses his/her camo outfit to hide in a bush for the night." % (name),font=('Helvetica',10,'bold'), bg='White')
            lbl_camooutfit.pack()
            bttn_next3 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
            window.mainloop()
            
        elif listejoueurs[u]["item1"] == "bag full of canned food": 
            
            name = listejoueurs[u]["name"]
            lbl_bagfullofcannedfood = tk.Label(master=frame11, text="%s falls asleep after having eaten everything that was in his/her bag full of canned food." % (name), font=('Helvetica',10,'bold'), bg='White')
            lbl_bagfullofcannedfood.pack()
            listejoueurs[u]["item1"] = "none"
            bttn_next3 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
            window.mainloop()
            
        elif listejoueurs[u]["item1"] == "bag full of medics and bandages" and listejoueurs[u]["status"] == "Wounded": 
            
            name = listejoueurs[u]["name"]
            lbl_bagfullofmedicsandbandages = tk.Label(master=frame11, text="%s was wounded but used his/her bag full of medics and bandages to heal the wound." % (name), font=('Helvetica',10,'bold'), bg='White')
            lbl_bagfullofmedicsandbandages.pack()
            listejoueurs[u]["status"] = "Alive"
            bttn_next3 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
            window.mainloop()
            
        else: 
            
            name = listejoueurs[u]["name"]
            location = listejoueurs[u]["location"]
            randomtxtforthenight = random.randint(0,10)
            if randomtxtforthenight == 1 or randomtxtforthenight == 7:
                lbl_nighttext1 = tk.Label(master=frame11, text="%s finds a safe place for the night." % (name),font=('Helvetica',10,'bold'), bg='White')
                lbl_nighttext1.pack()
            elif randomtxtforthenight == 0 or randomtxtforthenight == 8 or randomtxtforthenight == 9:
                lbl_nighttext1 = tk.Label(master=frame11, text="%s tries to sleep but can't seem to find a good position so he/she stays awake all night." % (name),font=('Helvetica',10,'bold'), bg='White')
                lbl_nighttext1.pack()
            elif randomtxtforthenight == 2:
                lbl_nighttext1 = tk.Label(master=frame11, text="%s tries to sleep on the ground but is attacked by venomous ants." % (name),font=('Helvetica',10,'bold'), bg='White')
                lbl_nighttext1.pack()
                listejoueurs[u]["status"] = "Wounded"
            elif randomtxtforthenight == 4:
                lbl_nighttext1 = tk.Label(master=frame11, text="%s tries to fall asleep but is attacked by chimpanzes during the night." % (name),font=('Helvetica',10,'bold'), bg='White')
                lbl_nighttext1.pack()
                listejoueurs[u]["status"] = "Wounded"
            elif randomtxtforthenight == 3:
                lbl_nighttext1 = tk.Label(master=frame11, text="%s climbs a tree to sleep on a branch but it breaks and %s is badly wounded." % (name, name),font=('Helvetica',10,'bold'), bg='White')
                lbl_nighttext1.pack()
                listejoueurs[u]["status"] = "Wounded"
            elif randomtxtforthenight == 5:
                lbl_nighttext1 = tk.Label(master=frame11, text="%s thinks about his/her family and then goes to sleep." % (name),font=('Helvetica',10,'bold'), bg='White')
                lbl_nighttext1.pack()
            elif randomtxtforthenight == 6 or randomtxtforthenight == 10:
                lbl_nighttext1 = tk.Label(master=frame11, text="%s has a walk in the %s and falls asleep a few hours later." % (name, location),font=('Helvetica',10,'bold'), bg='White')
                lbl_nighttext1.pack()
            bttn_next3 = tk.Button(master=frame11, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
            window.mainloop()
    else:
        pass
    x += 1
        
def deleteframe11():
    for widget in frame11.winfo_children():
        widget.destroy()

bttn_nextday = tk.Button(master=frame11, text="Day Recap", command=lambda:[deleteframe11(),frame11.destroy(),window.quit()], fg='White', bg='Grey',font=('Helvetica',10,'bold'))
bttn_nextday.pack(pady=10)
window.mainloop()

frame13 = tk.Frame(bg='White')
frame13.pack()
def deleteframe13():
    for widget in frame13.winfo_children():
        widget.destroy()
        
#####################################################################################################################################################################################################################################
#####################RANDOM EVENT FUNCTION###########################################################################################################################################################################################
#####################################################################################################################################################################################################################################
def randomevent():
    randomeventnbr = random.randint(0,19)
    if randomeventnbr == 0: #GOES BACK TO CORNUCOPIA FINDS AN ITEM --
        cornuplayer = 'name'
        cornuplayerstatus = "dead"
        cornuplayeritem2 = 'item'
        cornuplayeralliancestatus = 'Alliance1'
        while cornuplayer == 'name' or cornuplayerstatus == 'dead':
            j = random.randint(0,int(len(listejoueurs)-1))
            cornuplayer = listejoueurs[j]['name']
            cornuplayerstatus = listejoueurs[j]['status']
            cornuplayeritem2 = listejoueurs[j]['item2']
            cornuplayeralliancestatus = listejoueurs[j]['alliance_status']
        if cornuplayeralliancestatus == 'Alliance1':
            randomitem2 = str(random.choice(itemnames))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'item2'",randomitem2))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'alliance_status'",'none'))
            location_lbl = tk.Label(frame13, text='%s breaks the alliance and goes to the Cornucopia.' % (cornuplayer),font=('Helvetica',10,'bold'), bg='White')
            location_lbl.pack()
            goesbacktocornu_lbl = tk.Label(frame13, text='%s finds a %s.' % (cornuplayer,randomitem2),font=('Helvetica',10,'bold'), bg='White')
            goesbacktocornu_lbl.pack()
            if cornuplayeritem2 != 'none':
                dropitem_lbl = tk.Label(frame13, text='%s could not keep all his items so he dropped his %s.' % (cornuplayer,cornuplayeritem2),font=('Helvetica',10,'bold'), bg='White')
                dropitem_lbl.pack()
            else:
                pass
        elif cornuplayeralliancestatus == 'none':
            randomitem2 = str(random.choice(itemnames))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'item2'",randomitem2))
            goesbacktocornu_lbl = tk.Label(frame13, text='%s goes back to the Cornucopia and finds a %s.' % (cornuplayer,randomitem2),font=('Helvetica',10,'bold'), bg='White')
            goesbacktocornu_lbl.pack()
            if cornuplayeritem2 != 'none':
                dropitem_lbl = tk.Label(frame13, text='%s could not keep all his items so he dropped his %s.' % (cornuplayer,cornuplayeritem2),font=('Helvetica',10,'bold'), bg='White')
                dropitem_lbl.pack()
            else:
                pass
        randomlocation = str(random.choice(locations_list))
        exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'location'",randomlocation))
        location_lbl = tk.Label(frame13, text='%s then heads towards the %s.' % (cornuplayer,randomlocation),font=('Helvetica',10,'bold'), bg='White')
        location_lbl.pack()
        bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
        bttn_next3.pack(pady=10)
        window.mainloop()
    elif randomeventnbr == 1: #GOES BACK TO CORNUCOPIA FINDS A WEAPON
        cornuplayer = 'name'
        cornuplayerstatus = "dead"
        cornuplayerweapon2 = 'weapon'
        cornuplayeralliancestatus = 'Alliance1'
        while cornuplayer == 'name' or cornuplayerstatus == 'dead':
            j = random.randint(0,int(len(listejoueurs)-1))
            cornuplayer = listejoueurs[j]['name']
            cornuplayerstatus = listejoueurs[j]['status']
            cornuplayerweapon2 = listejoueurs[j]['weapon2']
            cornuplayeralliancestatus = listejoueurs[j]['alliance_status']
        if cornuplayeralliancestatus == 'Alliance1':
            randomweapon2 = str(random.choice(weaponnames))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'alliance_status'",'none'))
            location_lbl = tk.Label(frame13, text='%s breaks the alliance and goes to the Cornucopia.' % (cornuplayer),font=('Helvetica',10,'bold'), bg='White')
            location_lbl.pack()
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'weapon2'",randomweapon2))
            goesbacktocornu_lbl = tk.Label(frame13, text='%s finds a %s.' % (cornuplayer,randomweapon2),font=('Helvetica',10,'bold'), bg='White')
            goesbacktocornu_lbl.pack()
            if cornuplayerweapon2 != 'none':
                dropweapon_lbl = tk.Label(frame13, text='%s could not keep all his weapons so he dropped his %s.' % (cornuplayer,cornuplayerweapon2),font=('Helvetica',10,'bold'), bg='White')
                dropweapon_lbl.pack()
            else:
                pass
        elif cornuplayeralliancestatus == 'none':
            randomweapon2 = str(random.choice(weaponnames))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'weapon2'",randomweapon2))
            goesbacktocornu_lbl = tk.Label(frame13, text='%s goes back to the Cornucopia and grabs a %s.' % (cornuplayer,randomweapon2),font=('Helvetica',10,'bold'), bg='White')
            goesbacktocornu_lbl.pack()
            if cornuplayerweapon2 != 'none':
                dropweapon_lbl = tk.Label(frame13, text='%s could not keep all his weapons so he dropped his %s.' % (cornuplayer,cornuplayerweapon2),font=('Helvetica',10,'bold'), bg='White')
                dropweapon_lbl.pack()
            else:
                pass
        
        randomlocation = str(random.choice(locations_list))
        exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'location'",randomlocation))
        location_lbl = tk.Label(frame13, text='%s then heads towards the %s.' % (cornuplayer,randomlocation),font=('Helvetica',10,'bold'), bg='White')
        location_lbl.pack()
        bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
        bttn_next3.pack(pady=10)
        window.mainloop()
    elif randomeventnbr == 2 or randomeventnbr == 3 or randomeventnbr == 4 or randomeventnbr == 5: #GOES TO RANDOM LOCATION
        cornuplayer = 'name'
        cornuplayerstatus = "dead"
        cornuplayeralliancestatus = 'Alliance1'
        while cornuplayer == 'name' or cornuplayerstatus == 'dead':
            j = random.randint(0,int(len(listejoueurs)-1))
            cornuplayer = listejoueurs[j]['name']
            cornuplayerstatus = listejoueurs[j]['status']
            cornuplayeralliancestatus = listejoueurs[j]['alliance_status']
        if cornuplayeralliancestatus == 'none':
            randomlocation = listejoueurs[int(j)]['location']
            while randomlocation == listejoueurs[int(j)]['location']:
                randomlocation = str(random.choice(locations_list))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'location'",randomlocation))
            location_lbl = tk.Label(frame13, text='%s moves to the %s.' % (cornuplayer,randomlocation),font=('Helvetica',10,'bold'), bg='White')
            location_lbl.pack()
            bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
        elif cornuplayeralliancestatus == 'Alliance1':
            randomlocation = listejoueurs[int(j)]['location']
            while randomlocation == listejoueurs[int(j)]['location']:
                randomlocation = str(random.choice(locations_list))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'location'",randomlocation))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'alliance_status'",'none'))
            location_lbl = tk.Label(frame13, text='%s breaks the alliance and moves to the %s.' % (cornuplayer,randomlocation),font=('Helvetica',10,'bold'), bg='White')
            location_lbl.pack()
            bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
        window.mainloop()
    elif randomeventnbr == 6 or randomeventnbr == 7 or randomeventnbr == 8 or randomeventnbr == 9 or randomeventnbr == 10: #2 PLAYERS IN THE SAME LOCATION
        player1 = "name"
        player2 = "name"
        player1status = "dead"
        player2status = "dead"
        player1location = "none"
        player2location = "none1"
        while player1 == "name" or player2 == "name" or player1 == player2 or player1status == "dead" or player2status == "dead":
            j = random.randint(0,int(len(listejoueurs)-1))
            j2 = random.randint(0,int(len(listejoueurs)-1))
            player1 = listejoueurs[j]['name']
            player2 = listejoueurs[j2]['name']
            player1status = listejoueurs[j]['status']
            player2status = listejoueurs[j2]['status']
            player1location = listejoueurs[j]['location']
            player2location = listejoueurs[j2]['location']
        if player1location != player2location:
            listejoueurs[j]['location'] = player2location
            if listejoueurs[j]['alliance_status'] == 'Alliance1':
                        location_lbl = tk.Label(frame13, text='%s breaks the alliance and moves to the %s.' % (player1,player2location),font=('Helvetica',10,'bold'), bg='White')
                        location_lbl.pack()
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'alliance_status'",'none'))
            else:
                location_lbl = tk.Label(frame13, text='%s moves to the %s.' % (player1,player2location),font=('Helvetica',10,'bold'), bg='White')
                location_lbl.pack()
            player1location = listejoueurs[j]['location']
            killerplayerrandom = random.randint(0,1)
            if player1location == "river":
                if killerplayerrandom == 0:   
                      
                    playerkillsplayer_lbl = tk.Label(frame13, text='%s finds %s near the %s and kills him/her.' % (player1,player2,player1location),font=('Helvetica',10,'bold'), bg='White')
                    playerkillsplayer_lbl.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(j2),"'status'","dead"))
                    listejoueurs[j]['killcount'] = str(int(listejoueurs[j]['killcount'])+1)
                elif killerplayerrandom == 1:   
                      
                    playerkillsplayer_lbl = tk.Label(frame13, text='%s finds %s near the %s and kills him/her.' % (player2,player1,player1location),font=('Helvetica',10,'bold'), bg='White')
                    playerkillsplayer_lbl.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","dead"))
                    listejoueurs[j2]['killcount'] = str(int(listejoueurs[j2]['killcount'])+1)
            else:
                if killerplayerrandom == 0:   
                         
                    playerkillsplayer_lbl = tk.Label(frame13, text='%s finds %s in the %s and kills him/her.' % (player1,player2,player1location),font=('Helvetica',10,'bold'), bg='White')
                    playerkillsplayer_lbl.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(j2),"'status'","dead"))
                    listejoueurs[j]['killcount'] = str(int(listejoueurs[j]['killcount'])+1)
                elif killerplayerrandom == 1:   
                
                    playerkillsplayer_lbl = tk.Label(frame13, text='%s finds %s in the %s and kills him/her.' % (player2,player1,player1location),font=('Helvetica',10,'bold'), bg='White')
                    playerkillsplayer_lbl.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","dead"))
                    listejoueurs[j2]['killcount'] = str(int(listejoueurs[j2]['killcount'])+1)
            bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
        else:
            killerplayerrandom = random.randint(0,1)
            if player1location == "river":
                if killerplayerrandom == 0:   
                    if listejoueurs[j2]['alliance_status'] == listejoueurs[j]['alliance_status'] and listejoueurs[j2]['alliance_status'] != 'none':
                        playerkillsplayer_lbl = tk.Label(frame13, text='%s breaks the alliance and kills %s near the %s.' % (player1,player2,player1location),font=('Helvetica',10,'bold'), bg='White')
                        playerkillsplayer_lbl.pack()
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j2),"'status'","dead"))
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'alliance_status'",'none'))
                        listejoueurs[j]['killcount'] = str(int(listejoueurs[j]['killcount'])+1)
                    else:    
                        playerkillsplayer_lbl = tk.Label(frame13, text='%s finds %s near the %s and kills him/her.' % (player1,player2,player1location),font=('Helvetica',10,'bold'), bg='White')
                        playerkillsplayer_lbl.pack()
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j2),"'status'","dead"))
                        listejoueurs[j]['killcount'] = str(int(listejoueurs[j]['killcount'])+1)
                elif killerplayerrandom == 1:   
                    if listejoueurs[j2]['alliance_status'] == listejoueurs[j]['alliance_status'] and listejoueurs[j2]['alliance_status'] != 'none':
                        playerkillsplayer_lbl = tk.Label(frame13, text='%s breaks the alliance and kills %s near the %s.' % (player2,player1,player1location),font=('Helvetica',10,'bold'), bg='White')
                        playerkillsplayer_lbl.pack()
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","dead"))
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j2),"'alliance_status'",'none'))
                        listejoueurs[j2]['killcount'] = str(int(listejoueurs[j2]['killcount'])+1)
                    else:    
                        playerkillsplayer_lbl = tk.Label(frame13, text='%s finds %s near the %s and kills him/her.' % (player2,player1,player1location),font=('Helvetica',10,'bold'), bg='White')
                        playerkillsplayer_lbl.pack()
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","dead"))
                        listejoueurs[j2]['killcount'] = str(int(listejoueurs[j2]['killcount'])+1)
            else:
                if killerplayerrandom == 0:   
                    if listejoueurs[j2]['alliance_status'] == listejoueurs[j]['alliance_status'] and listejoueurs[j2]['alliance_status'] != 'none':
                        playerkillsplayer_lbl = tk.Label(frame13, text='%s breaks the alliance and kills %s in the %s.' % (player1,player2,player1location),font=('Helvetica',10,'bold'), bg='White')
                        playerkillsplayer_lbl.pack()
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j2),"'status'","dead"))
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'alliance_status'",'none'))
                        listejoueurs[j]['killcount'] = str(int(listejoueurs[j]['killcount'])+1)
                    else:    
                        playerkillsplayer_lbl = tk.Label(frame13, text='%s finds %s in the %s and kills him/her.' % (player1,player2,player1location),font=('Helvetica',10,'bold'), bg='White')
                        playerkillsplayer_lbl.pack()
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j2),"'status'","dead"))
                        listejoueurs[j]['killcount'] = str(int(listejoueurs[j]['killcount'])+1)
                elif killerplayerrandom == 1:   
                    if listejoueurs[j2]['alliance_status'] == listejoueurs[j]['alliance_status'] and listejoueurs[j2]['alliance_status'] != 'none':
                        playerkillsplayer_lbl = tk.Label(frame13, text='%s breaks the alliance and kills %s in the %s.' % (player2,player1,player1location),font=('Helvetica',10,'bold'), bg='White')
                        playerkillsplayer_lbl.pack()
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","dead"))
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j2),"'alliance_status'",'none'))
                        listejoueurs[j2]['killcount'] = str(int(listejoueurs[j2]['killcount'])+1)
                    else:    
                        playerkillsplayer_lbl = tk.Label(frame13, text='%s finds %s in the %s and kills him/her.' % (player2,player1,player1location),font=('Helvetica',10,'bold'), bg='White')
                        playerkillsplayer_lbl.pack()
                        exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","dead"))
                        listejoueurs[j2]['killcount'] = str(int(listejoueurs[j2]['killcount'])+1)
            bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
        window.mainloop()
    elif randomeventnbr == 11 or randomeventnbr == 12 or randomeventnbr == 13 or randomeventnbr == 14: #ITEM EVENTS
        randomplayerstatus = 'dead'
        while randomplayerstatus == 'dead':
            j = random.randint(0,int(len(listejoueurs)-1))
            randomplayerforitems = listejoueurs[j]['name']
            randomplayerstatus = listejoueurs[j]['status']
            randomplayersitem1 = listejoueurs[j]['item1']
            randomplayersitem2 = listejoueurs[j]['item2']
            randomplayerssponsoritem = listejoueurs[j]['sponsor_item']
        if randomplayersitem1 != 'none':
            if randomplayersitem1 == "rope": #["rope", "pair of binoculars", "bear trap", "bag full of canned food", "bag full of medics and bandages", "camo outfit", "lighter", "flashlight", "survival blanket"]
                randomnum = random.randint(0,2)
                if randomnum == 0 or randomnum == 1 :
                    playerkillsitself = tk.Label(frame13, text='%s throws away his/her rope as he/she does not feel like it could be useful.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                    playerkillsitself.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'item1'","none"))
                elif randomnum == 2:
                    playerkillsitself = tk.Label(frame13, text='%s uses his/her rope to hang himself/herself.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                    playerkillsitself.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","dead"))
            elif randomplayersitem1 == "pair of binoculars":
                playerusesbinoculars = tk.Label(frame13, text='%s uses his/her pair of binoculars to spy on a nearby player.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playerusesbinoculars.pack()
            elif randomplayersitem1 == "lighter":
                playeruseslighter = tk.Label(frame13, text='%s uses his/her lighter to make a fire.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playeruseslighter.pack()
            elif randomplayersitem1 == "bag full of medics and bandages" and randomplayerstatus == 'Wounded':
                lbl_bagfullofmedicsandbandages = tk.Label(master=frame13, text="%s was wounded but used his/her bag full of medics and bandages to heal the wound." % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                lbl_bagfullofmedicsandbandages.pack()
                exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","Alive"))
            else:
                playerisbored = tk.Label(frame13, text='%s is bored and can not seem to find anything to do except wait.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playerisbored.pack()
            
        elif randomplayersitem2 != 'none':
            if randomplayersitem2 == "rope": #["rope", "pair of binoculars", "bear trap", "bag full of canned food", "bag full of medics and bandages", "camo outfit", "lighter", "flashlight", "survival blanket"]
                randomnum = random.randint(0,2)
                if randomnum == 0 or randomnum == 1 :
                    playerkillsitself = tk.Label(frame13, text='%s throws away his/her rope as he/she does not feel like it could be useful.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                    playerkillsitself.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'item2'","none"))
                elif randomnum == 2:
                    playerkillsitself = tk.Label(frame13, text='%s uses his/her rope to hang himself/herself.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                    playerkillsitself.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","dead"))
            elif randomplayersitem2 == "pair of binoculars":
                playerusesbinoculars = tk.Label(frame13, text='%s uses his/her pair of binoculars to spy on a nearby player.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playerusesbinoculars.pack()
            elif randomplayersitem2 == "lighter":
                playeruseslighter = tk.Label(frame13, text='%s uses his/her lighter to make a fire.' % (randomplayerforitems))
                playeruseslighter.pack()
            elif randomplayersitem2 == "bag full of medics and bandages" and randomplayerstatus == 'Wounded':
                lbl_bagfullofmedicsandbandages = tk.Label(master=frame13, text="%s was wounded but used his/her bag full of medics and bandages to heal the wound." % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                lbl_bagfullofmedicsandbandages.pack()
                exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","Alive"))
            else:
                playerisbored = tk.Label(frame13, text='%s is bored and can not seem to find anything to do except wait.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playerisbored.pack()
        elif randomplayerssponsoritem != 'none': #['foldable ladder', 'hot meal', 'hot chocolate','face cleansing kit','lollipop']
            if randomplayerssponsoritem == 'foldable ladder':
                playerusesladder = tk.Label(frame13, text='%s uses his/her foldable ladder to climb a tree and spy on nearby players.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playerusesladder.pack()
            elif randomplayerssponsoritem == 'hot meal':
                playereats = tk.Label(frame13, text='%s eats his/her hot meal which makes him/her feel better.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playereats.pack()
                exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'sponsor_item'","none"))
            elif randomplayerssponsoritem == 'hot chocolate':
                playereats = tk.Label(frame13, text='%s drinks his/her hot chocolate which makes him/her feel better.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playereats.pack()
                exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'sponsor_item'","none"))
            elif randomplayerssponsoritem == 'face cleansing kit':
                playercleans = tk.Label(frame13, text='%s uses his/her face cleansing kit to clean himself/herself.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playercleans.pack()
                exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'sponsor_item'","none"))
            elif randomplayerssponsoritem == 'lollipop':
                playereats = tk.Label(frame13, text='%s eats his/her lollipop which gaves him/her some strength.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
                playereats.pack()
                exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'sponsor_item'","none"))
        else:
            playerisbored = tk.Label(frame13, text='%s is bored and can not seem to find anything to do except wait.' % (randomplayerforitems),font=('Helvetica',10,'bold'), bg='White')
            playerisbored.pack()
        bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
        bttn_next3.pack(pady=10)
        window.mainloop()
    elif randomeventnbr == 15 or randomeventnbr == 16 or randomeventnbr == 17: #BIG EVENTS
        randomlocation = str(random.choice(locations_list))
        randomnigevent = random.choice(['tsunami', 'blood rain', 'massive locusts attack', 'tarantula attack','lightning storm','sandstorm','firestorm','rockslide'])
        bigevent_lbl = tk.Label(frame13, text='A %s takes place in the %s.' % (randomnigevent,randomlocation),font=('Helvetica',10,'bold'), bg='White')
        bigevent_lbl.pack()
        r = 0
        while r != len(listofplayersforfirstrun):
            u = int(listofplayersforfirstrun[r])
            if listejoueurs[u]["location"] == randomlocation and listejoueurs[u]["status"] != 'dead':
                name = listejoueurs[u]["name"]
                randomnbr = random.randint(0,2)
                if randomnbr == 0:
                    bigevent2_lbl = tk.Label(frame13, text='%s is killed during this event.' % (name),font=('Helvetica',10,'bold'), bg='White')
                    bigevent2_lbl.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(u),"'status'","dead"))
                    bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
                    bttn_next3.pack(pady=10)
                    window.mainloop()
                elif randomnbr == 1:
                    bigevent2_lbl = tk.Label(frame13, text='%s is wounded during this event.' % (name),font=('Helvetica',10,'bold'), bg='White')
                    bigevent2_lbl.pack()
                    exec ("listejoueurs[%s][%s] = '%s'" % (str(u),"'status'","Wounded"))
                    bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
                    bttn_next3.pack(pady=10)
                    window.mainloop()
                else:
                    bigevent2_lbl = tk.Label(frame13, text='%s manages to hide and is not wounded during this event.' % (name),font=('Helvetica',10,'bold'), bg='White')
                    bigevent2_lbl.pack()
                    bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
                    bttn_next3.pack(pady=10)
                    window.mainloop()
            else:
                pass
            r += 1
    elif randomeventnbr == 18 or randomeventnbr == 19: #SPONSORSHIPS
        sponsorshipplayer = 'name'
        sponsorshipplayerstatus = "dead"
        sponsorshipitem = 'none1'
        while sponsorshipplayer == 'name' or sponsorshipplayerstatus == 'dead' or sponsorshipitem != 'none':
            j = random.randint(0,int(len(listejoueurs)-1))
            sponsorshipplayer = listejoueurs[j]['name']
            sponsorshipplayerstatus = listejoueurs[j]['status']
            sponsorshipitem = listejoueurs[j]['sponsor_item']
        if sponsorshipplayerstatus == 'Wounded':
            sponsorshipitem_lbl = tk.Label(frame13, text='%s gets a healing cream from a sponsor. He/She uses it to heal his/her wounds.' % (sponsorshipplayer),font=('Helvetica',10,'bold'), bg='White')
            sponsorshipitem_lbl.pack()
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'status'","Alive"))
            bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
            window.mainloop()
        else:
            randomitem = str(random.choice(sponsorshipitemnames))
            exec ("listejoueurs[%s][%s] = '%s'" % (str(j),"'sponsor_item'",randomitem))
            sponsorshipitem_lbl = tk.Label(frame13, text='%s gets a %s from a sponsor.' % (sponsorshipplayer,randomitem),font=('Helvetica',10,'bold'), bg='White')
            sponsorshipitem_lbl.pack()
            bttn_next3 = tk.Button(master=frame13, text="Next", command=lambda:[bttn_next3.destroy(),window.quit()], fg='White', bg='Black',font=('Helvetica',10,'bold'))
            bttn_next3.pack(pady=10)
            window.mainloop()



##############################################################################################DAY RECAP###########################################################################################################

def dayrecap():
    for x in range(0,len(listejoueurs)):
            if listejoueurs[x]['status'] == 'dead':
                player = listejoueurs[x]['name']
                lbl_playername = tk.Label(frame13, text="Player %s: %s" % (str(x+1),player), font=('Helvetica',12,'bold'), fg="Red", width=55, bg='White')
                lbl_playername.pack()
                playerstatus = listejoueurs[x]['status']
                lbl_playerstatus = tk.Label(frame13, text="Status: %s" % (playerstatus), font=('Helvetica',8,'bold'), bg='White')
                lbl_playerstatus.pack()
            elif listejoueurs[x]['status'] == 'Alive':
                player = listejoueurs[x]['name']
                lbl_playername = tk.Label(frame13, text="Player %s: %s" % (str(x+1),player), font=('Helvetica',12,'bold'), fg="Green", width=55, bg='White')
                lbl_playername.pack()
                playerstatus = listejoueurs[x]['status']
                lbl_playerstatus = tk.Label(frame13, text="Status: %s" % (playerstatus), font=('Helvetica',8,'bold'), bg='White')
                lbl_playerstatus.pack()
                item1 = listejoueurs[x]['item1']
                if item1 != 'none':
                    lbl_item1 = tk.Label(frame13, text="Item 1: %s" % (item1), font=('Helvetica',8,'bold'), bg='White')
                    lbl_item1.pack()
                else:
                    pass
                item2 = listejoueurs[x]['item2']
                if item2 != 'none':
                    if item1 == 'none':
                        lbl_item1 = tk.Label(frame13, text="Item 1: %s" % (item2), font=('Helvetica',8,'bold'), bg='White')
                        lbl_item1.pack()
                    else:
                        lbl_item2 = tk.Label(frame13, text="Item 2: %s" % (item2), font=('Helvetica',8,'bold'), bg='White')
                        lbl_item2.pack()
                else:
                    pass
                weapon1 = listejoueurs[x]['weapon1']
                if weapon1 != 'none':
                    lbl_weapon1 = tk.Label(frame13, text="Weapon 1: %s" % (weapon1), font=('Helvetica',8,'bold'), bg='White')
                    lbl_weapon1.pack()
                else:
                    pass
                weapon2 = listejoueurs[x]['weapon2']
                if weapon2 != 'none':
                    if weapon1 == 'none':
                        lbl_weapon1 = tk.Label(frame13, text="Weapon 1: %s" % (weapon2), font=('Helvetica',8,'bold'), bg='White')
                        lbl_weapon1.pack()
                    else:
                        lbl_weapon2 = tk.Label(frame13, text="Weapon 2: %s" % (weapon2), font=('Helvetica',8,'bold'), bg='White')
                        lbl_weapon2.pack()
                else:
                    pass
                sponsoritem = listejoueurs[x]['sponsor_item']
                if sponsoritem != 'none':
                    lbl_sponsoritem = tk.Label(frame13, text="Item from sponsor: %s" % (sponsoritem), font=('Helvetica',8,'bold'), bg='White')
                    lbl_sponsoritem.pack()
                else:
                    pass
                killcount = listejoueurs[x]['killcount']
                lbl_killcount= tk.Label(frame13, text="Killcount: %s" % (killcount), font=('Helvetica',8,'bold'), bg='White')
                lbl_killcount.pack()
            elif listejoueurs[x]['status'] == 'Wounded':
                player = listejoueurs[x]['name']
                lbl_playername = tk.Label(frame13, text="Player %s: %s" % (str(x+1),player), font=('Helvetica',12,'bold'), fg="Orange", width=55, bg='White')
                lbl_playername.pack()
                playerstatus = listejoueurs[x]['status']
                lbl_playerstatus = tk.Label(frame13, text="Status: %s" % (playerstatus), font=('Helvetica',8,'bold'), bg='White')
                lbl_playerstatus.pack()
                item1 = listejoueurs[x]['item1']
                if item1 != 'none':
                    lbl_item1 = tk.Label(frame13, text="Item 1: %s" % (item1), font=('Helvetica',8,'bold'), bg='White')
                    lbl_item1.pack()
                else:
                    pass
                item2 = listejoueurs[x]['item2']
                if item2 != 'none':
                    if item1 == 'none':
                        lbl_item1 = tk.Label(frame13, text="Item 1: %s" % (item2), font=('Helvetica',8,'bold'), bg='White')
                        lbl_item1.pack()
                    else:
                        lbl_item2 = tk.Label(frame13, text="Item 2: %s" % (item2), font=('Helvetica',8,'bold'), bg='White')
                        lbl_item2.pack()
                else:
                    pass
                weapon1 = listejoueurs[x]['weapon1']
                if weapon1 != 'none':
                    lbl_weapon1 = tk.Label(frame13, text="Weapon 1: %s" % (weapon1), font=('Helvetica',8,'bold'), bg='White')
                    lbl_weapon1.pack()
                else:
                    pass
                weapon2 = listejoueurs[x]['weapon2']
                if weapon2 != 'none':
                    if weapon1 == 'none':
                        lbl_weapon1 = tk.Label(frame13, text="Weapon 1: %s" % (weapon2), font=('Helvetica',8,'bold'), bg='White')
                        lbl_weapon1.pack()
                    else:
                        lbl_weapon2 = tk.Label(frame13, text="Weapon 2: %s" % (weapon2), font=('Helvetica',8,'bold'), bg='White')
                        lbl_weapon2.pack()
                else:
                    pass
                sponsoritem = listejoueurs[x]['sponsor_item']
                if sponsoritem != 'none':
                    lbl_sponsoritem = tk.Label(frame13, text="Item from sponsor: %s" % (sponsoritem), font=('Helvetica',8,'bold'), bg='White')
                    lbl_sponsoritem.pack()
                else:
                    pass
                killcount = listejoueurs[x]['killcount']
                lbl_killcount= tk.Label(frame13, text="Killcount: %s" % (killcount), font=('Helvetica',8,'bold'), bg='White')
                lbl_killcount.pack()
    bttn_nextday = tk.Button(master=frame13, text="Next Day", command=lambda:[deleteframe13(),window.quit()], fg='White', bg='Grey',font=('Helvetica',10,'bold'))
    bttn_nextday.pack(pady=10)
    window.mainloop()

dayrecap()

########################MAIN EVENTS##################################
day = 1
listejoueursstatus = []
for x in range(0,len(listejoueurs)):
    if listejoueurs[x]['status'] != 'dead':
        exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
    else:
        pass
print(listejoueursstatus)

global j2
while len(listejoueursstatus) != 1:
    day += 1
    dispday_lbl = tk.Label(frame13, text="Day %d" % (day), width=70, bg='White',font=('Helvetica',14,'bold'))
    dispday_lbl.pack(pady=20)
    
    ###################EVENT 1################################
    if len(listejoueursstatus) != 1:
        randomevent()
    else:
        break
    
    listejoueursstatus = []
    for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
        else:
            pass
    print(listejoueursstatus)
    ###################EVENT 2################################
    if len(listejoueursstatus) != 1:
        randomevent()
    else:
        break
    
    listejoueursstatus = []
    for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
        else:
            pass
    print(listejoueursstatus)
    ###################EVENT 3################################
    if len(listejoueursstatus) != 1:
        randomevent()
    else:
        break
    
    listejoueursstatus = []
    for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
        else:
            pass
    print(listejoueursstatus)
    ###################EVENT 4################################
    if len(listejoueursstatus) != 1:
        randomevent()
    else:
        break
    
    listejoueursstatus = []
    for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
        else:
            pass
    print(listejoueursstatus)
    ###################EVENT 5################################
    if len(listejoueursstatus) != 1:
        randomevent()
    else:
        break
    
    listejoueursstatus = []
    for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
        else:
            pass
    print(listejoueursstatus)
    ###################EVENT 6################################
    if len(listejoueursstatus) != 1:
        randomevent()
    else:
        break
    
    listejoueursstatus = []
    for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
        else:
            pass
    print(listejoueursstatus)
    ###################EVENT 7################################
    if len(listejoueursstatus) != 1:
        randomevent()
    else:
        break
    
    listejoueursstatus = []
    for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
        else:
            pass
    print(listejoueursstatus)
    ###################EVENT 8################################
    if len(listejoueursstatus) != 1:
        randomevent()
    else:
        break
    
    listejoueursstatus = []
    for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
        else:
            pass
    
    print(listejoueursstatus)
    print(listejoueursstatus)
    bttn_nextday = tk.Button(master=frame13, text="Day Recap", command=lambda:[deleteframe13(),window.quit()], fg='White', bg='Grey',font=('Helvetica',10,'bold'))
    bttn_nextday.pack(pady=10)
    window.mainloop()
    
    listejoueursstatus = []
    for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            exec("listejoueursstatus.append(listejoueurs[%s]['status'])" % (x))
        else:
            pass
    dayrecap()
    
#################################THE WINNER IS################  
deleteframe13()
for x in range(0,len(listejoueurs)):
        if listejoueurs[x]['status'] != 'dead':
            winnername = listejoueurs[x]['name']
            lbl_winner = tk.Label(frame13, text="%s is the last person standing, he/she is declared winner of The Hunger Games!" % (winnername), font=('Helvetica',12,'bold'), bg='White')
            lbl_winner.pack(pady=40)
            winnerkillcount = listejoueurs[x]['killcount']
            lbl_winnerkillcount = tk.Label(frame13, text="%s killed %s other player(s) during this game!" % (winnername, str(winnerkillcount)), font=('Helvetica',10,'bold'), bg='White')
            lbl_winnerkillcount.pack(pady=10)
        else:
            pass
bttn_quit = tk.Button(master=frame13, text="Quit", command=lambda:[window.destroy()], fg='White', bg='Grey',font=('Helvetica',10,'bold'))
bttn_quit.pack(pady=10)
window.mainloop()
