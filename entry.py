import datetime
import random

print(format("MJ PARKING",">80"))
print("\nRATE:-45 PER HOUR FOR FOUR WHEELER \n\nRATE:-25 PER HOUR FOR TWO WHEELER\n"
	  "\nPARKING TERMINOLOGIES:-\n1:-FIRST FLOOR\n2:-SECOND FLOOR\n3:-THIRD FLOOR\n")

parkingid=random.randint(1186,9999)
list=[]
ans="y"
while ans=="y" or ans== "Y":
	name=input("ENTER THE NAME:-")
	vhicle_number=input("ENTER THE NUMBER:-")
	vehicle_type=input("ENTER 2 OR 4 :-")
	hour = datetime.datetime.today().time().hour
	minute = datetime.datetime.today().time().minute
	time=datetime.datetime.today().time()
	if vehicle_type=="2":
		floor=1
		file=open("C:\\Users\\intex\\PycharmProjects\\JARVIS\\mayankjoshi\\mayankjoshi\\first_floor.txt","r+")
		value = int(file.read())
		if value>0 and value<=300:
			l=[name.upper(),"\n",vhicle_number.upper(),"\n",str(hour),"\n",str(minute),"\n",str(vehicle_type),"\n",str(floor)]
			f=open(str(parkingid)+str(name)+".txt","w")
			f.writelines(l)

			value-=1
			file.seek(0,0)
			file.write(str(value))
		else:
			print("PARKING FULL !!!!")
	elif vehicle_type=="4":
		file1=open("C:\\Users\\intex\\PycharmProjects\\JARVIS\\mayankjoshi\\mayankjoshi\\second_floor.txt","r+")
		value=int(file1.read())
		if value>0 and  value<=300:
			floor=2
			print(floor)
			if floor == 2:
				l = [name.upper(), "\n", vhicle_number.upper(), "\n",str(hour),"\n",str(minute),"\n",str(vehicle_type),"\n",str(floor)]
				f = open(str(parkingid) + str(name)+".txt", "w")
				f.writelines(l)
				value -= 1
				file1.seek(0, 0)
				file1.write(str(value))
			else:
				print("PARKING FULL !!!!!")

		else:
			file2=open("C:\\Users\\intex\\PycharmProjects\\JARVIS\\mayankjoshi\\mayankjoshi\\third_floor.txt","r+")
			value=int(file2.read())
			if value>0 and value<=300:
				floor=3
				if floor == 3:
					l = [name.upper(), "\n", vhicle_number.upper(), "\n",str(hour),"\n",str(minute),"\n",str(vehicle_type),"\n",str(floor)]
					f = open(str(parkingid) + str(name)+".txt", "w")
					f.writelines(l)
					value -= 1
					file2.seek(0, 0)
					file2.write(str(value))
			else:
				print("PARKING FULL !!!!!")






	print("\n-----------------------------------------------------------------------------------------------------------------------")
	print(f"NAME                            PARKING_ID            VEHICLE NUMBER")
	print(f"{name}               				 {parkingid}                {vhicle_number} "
		  f"                         {datetime.datetime.today().date()}         ")

	ans=input("ENTER Y OR y FOR MORE ENTRIES:-")

