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
		global world11
		global Tikteam
		global Yteam
		global createteam
		global createteam2
		createteam2= [ ]
		createteam= [ ]
		runlist=[1,2,3,4,5,6]
		teamlist1=["India","Pakistan","England","Australia","West Indies","Sri Lanka","New Zealand","South Africa","World 11","Youthoobers","Tiktokers"]
		Iteam=["K.L Rahul","R.Sharma","V.Kohli","Hardik Pandiya","MS Dhoni","Ravindra Jadeja","Kuldeep Yadav","Y.Chahal","Jaspreet Bumrah","M. Shammi","V.Sehwag"]
		Pteam=["Sarfraaz Ahmed","Asif Ali","Babar Azam","Fakhar Zaman","Haris Sohail","Hasan Ali","Imam Wasim","Imam-ul-haq","Sahid Afridi","Soaib Akhtar","Imran Khan"]
		Eteam=["Eoin Morgan","Moeen Ali","Jofra Archer","Jonny Bairstow","Jos Buttler","Tom Curran","Liam Dawson","Liam Plunkett","Adil Rashid","Joe Root","Ben Stokes"]
		Ateam=["Aron Finch","Jason Behrandroff","Alex Carey","Nathon Coulter-Nile","Pat Cummins","Peter Handscomb","Nathon Lyon","G.Maxwell","Kane Richardson","Steven Smith","Mitchell Starc"]
		Wteam=["Jason Holder","Sunil Ambris","Fabian Allen","Carlos Brathwaite","Dwayn Bravo","Sheldon Cotrell" ,"Shanon Gabriel","Chris Gayle","Andre Russell","Polard","Shai Hope"]
		Slteam=["Kasun Rajitha","Dimuth Karunartane","Dhananjay de silve","Avishka Fernando","Suranga Lakmal","Lasith Malinga","Jeavan Mendis","Kusal Mendis","Thusara Perera","Jayasuriya","Sanggakara"]
		Nteam=["Kane Williamson","Tom Blundell","Trent Boult","Colin Munro","Colin de Grandhomme","Lockie Feaguson","Martin Guptil","Matt Henry","Tom Latham","James Neesham","Henry Nicolls"]
		Sateam=["Faf du Plesis","Hasim Amla","Quinton de kock","Jean-PaulDumivy","Imran Tahir","Aiden Markram","David Miller","Chris Morris","ABD","Dale Steyn","Kagiso Rabada"]
		world11=["Gill Christ","Mathew Hayden","Sachin Tendulkar","K. Sangakara","Ricky Ponting","Abdul Razak", "Shane Warn","Daniel Vettory","Shoaib Akhtar","Wasim Akram","Shane Bond"]
		Yteam=["CarryMinati","BB ki Vines","Amit Bhadana","Ashish Chanchlani","Harsh Beniwal","R2H","Elvish Yadav","Technical Guruji","TVF","TSP","SlayyPoint"]
		Tikteam=["Mr.Taisu","Piyaz","Manjul Khatta","Adnan Shake","Husnain Shake","Awez Darwan","Garima-Aanchi","Jannat Zoo bair","Nisha Gurgaon","Nagma Mujrakar","Manav Chakkara"]
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
				try:
					
					runs=int(input("Hit between 1 to 6:》"))
				except:
					print("Wrong Input")
					continue
			
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
					if j==10:
							print("!!!Whole Team Out!!!")
							break
							os.system('clear')
					
					
				
				elif ball==runs:
					print(f"__{players[j]}__ !!Out!! at [{h}] runs by Hit wicket")
					file0=open("tempfile1.txt","a")
					file0.write(f"__{players[j]}__ Runs-{h}\n")
					file0.close()
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
				print("Wickets : ",j)
				
			os.system('clear')
			
				
		def balling(self):
			global c
			global c1
			j=0
			for i in range(0,jklm,1):
				try:
					
					ball=int(input("Take a runup and ball btw 1 to 6:》"))
				except:
					print("Wrong Input")
					continue
				
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
					print(f"__{players[j]}__ Out!! at {c} runs by \'Clean Bold\'")
					file2=open("tempfile2.txt","a")
					file2.write(f"{players[j]} Runs: {c}\n")
					file2.close()
					c=0
					
					
					j=j+1
					if j==10:
						print("!!!Whole Team Out!!!")
						break
					print(f"#{team2} : {c1}")
				elif c1>g2:
					print(f"#{team2} wins with {c1} run")
					break
				elif ball!=runs1 :
					c=c+runs1
					
					c1=c1+runs1
					print(f"__{players[j]}__:Runs:{c}")
				print(f"#{team2}:{c1}")
				print("Wickets : ",j)
			
	
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
		print("1.INDIA\n2.PAKISTAN\n3.ENGLAND\n4.AUSTRALIA\n5.WEST INDIES\n6.SRI LANKA\n7.NEW ZEALAND\n8.SOUTH AFRICA\n9.World 11\n10.Youthoobers\n11.Tiktokers\n0.For your team")
		
		
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
		elif cteam==9:
				team1=teamlist1[8]
				players=world11
		elif cteam==10:
				team1=teamlist1[9]
				players=Yteam
		elif cteam==11:
				team1=teamlist1[10]
				players=Tikteam
		elif cteam==0:
			teamname0=str.capitalize(input("Enter Your Team Name : "))
			for i in range(0, 11): 
				print(f"Player {i+1} Name :")
				ele = str(input()) 

				createteam.append(ele)
			team1=teamname0
			players=createteam
				
				
		os.system('clear')
		print("Players in team")
		for i in range(0,11):
			
				print("____",players[i],"____")
		input("\n\t\t\t@Press Enter")
		os.system('clear')
				
		play=Gameplay()
		play.batting()
		
		print("\nChoose your opponenet:")
		print("1.INDIA\n2.PAKISTAN\n3.ENGLAND\n4.AUSTRALIA\n5.WEST INDIES\n6.SRI LANKA\n7.NEW ZEALAND\n8.SOUTH AFRICA\n9.World 11\n10.Youthoobers\n11.Tiktokers\n0.For new team")
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
		elif cteam1==9:
				team2=teamlist[8]
				players=world11
		elif cteam1==10:
				team2=teamlist1[9]
				players=Yteam
		elif cteam1==11:
				team2=teamlist1[10]
				players=Tikteam
		elif cteam1==0:
			teamname00=str.capitalize(input("Enter Your Team Name : "))
			for i in range(0, 11): 
				print(f"Player {i+1} Name :")
				ele = str(input()) 

				createteam2.append(ele)
			team2=teamname00
			players=createteam2
		
		
			

		
		os.system('clear')
		print("#Players in team")
		for i in range(0,11):
			
				print("____",players[i],"____")
		input("\n\t\t\t@Press Enter")
		os.system('clear')
		play.balling()
	highscore=open("hscore.txt","a")
	file0read=open("tempfile1.txt")
	me=file0read.read()
	print(me)
	file0read.close()
	file0read=open("tempfile1.txt","r+")
	file0read.seek(0)
	file0read.truncate()
	file0read.close()
	file2read=open("tempfile2.txt")
	me1=file2read.read()
	print(me1)
	file2read.close()
	file2read=open("tempfile2.txt","r+")
	file2read.seek(0)
	file2read.truncate()
	file2read.close()
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

	

	
	
	
	

		
	
			
			
			

		
		