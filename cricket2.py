import random
import os
class Gameplay:
		global runlist
		global teamlist1
		global Iteam
		global Pteam
		global Eteam
		global Ateam
		global Wteam
		global Slteam
		global Nteam
		global Sateam
		runlist=[1,2,3,4,5,6]
		teamlist1=["India","Pakistan","England","Australia","West Indies","Sri Lanka","New Zealand","South Africa"]
		Iteam=["V.Kohli","R.Sharma","Ms Dhoni","R.Jadeja","Kedar Jadhav","Kuldeep Yadav","Jaspreet Bumrah","Y.Chahal","Hardik P.","S.Dhawan","V.Sehwag"]
		Pteam=["Sarfraaz Ahmed","Asif Ali","Babar Azam","Fakhar Zaman","Haris Sohail","Hasan Ali","Imam Wasim","Imam-ul-haq","Sahid Afridi","Soaib Akhtar","Imran Khan"]
		Eteam=["Eoin Morgan","Moeen Ali","Jofra Archer","Jonny Bairstow","Jos Buttler","Tom Curran","Liam Dawson","Liam Plunkett","Adil Rashid","Joe Root","Ben Stokes"]
		Ateam=["Aron Finch","Jason Behrandroff","Alex Carey","Nathon Coulter-Nile","Pat Cummins","Peter Handscomb","Nathon Lyon","G.Maxwell","Kane Richardson","Steven Smith","Mitchell Starc"]
		Wteam=["Jason Holder","Sunil Ambris","Fabian Allen","Carlos Brathwaite","Dwayn Bravo","Sheldon Cotrell" ,"Shanon Gabriel","Chris Gayle","Andre Russell","Polard","Shai Hope"]
		Slteam=["Kasun Rajitha","Dimuth Karunartane","Dhananjay de silve","Avishka Fernando","Suranga Lakmal","Lasith Malinga","Jeavan Mendis","Kusal Mendis","Thusara Perera","Jayasuriya","Sanggakara"]
		Nteam=["Kane Williamson","Tom Blundell","Trent Boult","Colin Munro","Colin de Grandhomme","Lockie Feaguson","Martin Guptil","Matt Henry","Tom Latham","James Neesham","Henry Nicolls"]
		Sateam=["Faf du Plesis","Hasim Amla","Quinton de kock","Jean-PaulDumivy","Imran Tahir","Aiden Markram","David Miller","Chris Morris","ABD","Dale Steyn","Kagiso Rabada"]
		def batting(self):
			global h
			global jklm
			global ball
			global c
			c=0
			global c1
			
			c1=0
			h=0
		
			
			over=int(input("[Enter no. of overs]:\t"))
			os.system('clear')
			balls=over*6
			#for opponent overs
			jklm=balls
			global j
			j=0
			global prun
			prun=0
			global h1
			h1=0
			global run2
			run2=0
		
			
			
			for i in range(0,jklm,1):
				runs=int(input("Hit between 1 to 6:》"))
				os.system('clear')
				
				ball=random.choice(runlist)
				print("●Ball no.",i+1)
				if runs>6:
					
					h=0
					h1=h1
					print(f"__{players[j]}__ LBW!!!!")
					j=j+1
					if j==9:
							print("!!!Whole Team Out!!!")
							break
							os.system('clear')
				elif runs<=0:
					h=0
					h1=h1
					print(f"__{players[j]}__ Run Out!!!")
					j=j+1
					if j==9:
							print("!!!Whole Team Out!!!")
							break
							os.system('clear')
					
					
				
				elif ball==runs:
					print(f"__{players[j]}__ !!Out!! at [{h}] runs by Hit wicket")
					try:
						print(f"__{players[j]}__ Runs-{h}\n")
						if j==9:
							print("!!!Whole Team Out!!!")
							break
					except:
						print("!!!All Players Out!!!")
			
					
					j=j+1
					h=0
					
				elif ball!=runs :
					h=h+runs
					
					h1=h1+runs
					global g2
					
					g2=h1
					print(f"__{players[j]}__:Runs:{h}")
				
					
					
				
				print(team1,":",h1)
				
			os.system('clear')
			
				
		def balling(self):
			c=0
			global c1
			j=0
			for i in range(0,jklm,1):
				ball=int(input("Take a runup and ball btw 1 to 6:》"))
				os.system('clear')
				runs1=random.choice(runlist)
				print("●Ball no.",i+1)
				
				if ball>6:
					print("Wide ball☆")
					c1=c1+6
					
				elif ball<=0:
					print("No ball☆")
					c1=c1+6
			
				elif ball==runs1:
					print(f"__{players[j]}__ Out!! at {h} runs by \'Clean Bold\'")
					c=0
					
					try:
						print(f"__{players[j]}__:Runs:{c}\n")
						j=j+1
						if j==9:
							print("!!!Whole Team Out!!!")
							break
					except:
						print("!!!All Players Out")
					finally:
						print(f"#{team2} : {c1}")
				elif c1>g2:
					print(f"#{team2} wins with {c1} run")
					break
				elif ball!=runs1 :
					c=c+runs1
					
					c1=c1+runs1
					print(f"__{players[j]}__:Runs:{c}")
				print(f"#{team2}:{c1}")
			
	
while True:
	print("\t\tVirtual Cricket")
	print("1.Play\n2.Score\n3.Rules\n4.Exit")
	choice=int(input())
	os.system('clear')
	if choice==4:
		exit()
	elif choice==2:
		rscore=open("hscore.txt","r")
		me=rscore.read()
		print(me)
		input()
		os.system('clear')
		rscore.close()
	elif choice==3:
		print("\t\t××××Rules××××")
		print("1.If you enter more then 6 while batting you will get LBW.\n2.If you enter less then 0 or equal to 0 you will get run out.\n3.If you enter more then 6 while balling opponent will get 6 run due to wide ball.\n4.If you enter less then 0 or equal to 0 opponent team will get 6 run due to no ball." )
		exit()
	elif choice==1:
		name1=str.upper(input("Enter your name:"))
		os.system('clear')
		
		print("Choose your team:")
		print("1.INDIA\n2.PAKISTAN\n3.ENGLAND\n4.AUSTRALIA\n5.WEST INDIES\n6.SRI LANKA\n7.NEW ZEALAND\n8.SOUTH AFRICA\n")
		
		
		global cteam
		global team1
		global cteam1
		global team2
		cteam=int(input())
		if cteam==1:
				team1=teamlist1[0]
				players=Iteam
		elif cteam==2:
				team1=teamlist1[1]
				players=Pteam
		elif cteam==3:
				players=Eteam
				team1=teamlist1[2]
		elif cteam==4:
				players=Ateam
				team1=teamlist1[3]
		elif cteam==5:
				team1=teamlist1[4]
				players=Wteam
		elif cteam==6:
				team1=teamlist1[5]
				players=Slteam
		elif cteam==7:
				team1=teamlist1[6]
				players=Nteam
		elif cteam==8:
				team1=teamlist1[7]
				players=Sateam
		os.system('clear')
		print("Players in team")
		for i in range(0,11):
			
				print("____",players[i],"____")
		input("\n\t\t\t@Press Enter")
		os.system('clear')
				
		play=Gameplay()
		play.batting()
		
		print("\nChoose your opponenet:")
		print("1.INDIA\n2.PAKISTAN\n3.ENGLAND\n4.AUSTRALIA\n5.WEST INDIES\n6.SRI LANKA\n7.NEW ZEALAND\n8.SOUTH AFRICA\n")
		cteam1=int(input())
		if cteam1==1:
				team2=teamlist1[0]
				players=Iteam
		elif cteam1==2:
				team2=teamlist1[1]
				players=Pteam
		elif cteam1==3:
				players=Eteam
				team2=teamlist1[2]
		elif cteam1==4:
				players=Ateam
				team2=teamlist1[3]
		elif cteam1==5:
				team2=teamlist1[4]
				players=Wteam
		elif cteam1==6:
				team2=teamlist1[5]
				players=Slteam
		elif cteam1==7:
				team2=teamlist1[6]
				players=Nteam
		elif cteam1==8:
				team2=teamlist1[7]
				players=Sateam
		os.system('clear')
		print("#Players in team")
		for i in range(0,11):
			
				print("____",players[i],"____")
		input("\n\t\t\t@Press Enter")
		os.system('clear')
		play.balling()
	highscore=open("hscore.txt","a")
	highscore.write(f"\t\t\t\n{name1} HAS SCORED {h1} RUNS WITH TEAM {team1}")
	highscore.close()
	print(f"\t\t\t■{team1} Runs:{h1}■")
	print(f"\t\t\t■{team2} Runs:{c1}■")
	if c1>h1:
		print(f"-------:#{team2} wins with #{c1} RUNS:---------")
		input()
		os.system('clear')
		
	elif h1>c1:
		print(f"-------:#{team1} wins with #{h1} RUNS:--------")
		input()
		os.system('clear')
		
	elif h1==c1:
		print("××××Game Draw××××")
		input()
		os.system('clear')
		
print("@Press Enter to restart")

	

	
	
	
	

		
	
			
			
			

		
		