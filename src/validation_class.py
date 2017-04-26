class Validation():

	#check if room Type Entered is Either an oofice or LivingRoom
	def check_room_type(self,room_type):
		#check if arg person_type is not empty
		if person_type!=None:
			if isinstance(room_type, str):#check if its a string
				if room_type=="office" or room_type=="livingRoom": 
					return room_type
				else:
					raise ValueError("error")
			else:
				raise TypeError(" error")
		else:
			raise TypeError(" error")

	#check if room name entered is a string and not empty
	def check_room_name(self,room_name):
		#check if room name  is not empty
		if room_name!=None:
			if isinstance(room_name, str):#check if its a string
				return room_name
			else:
				raise TypeError(" error")
		else:
			raise TypeError(" error")

	def check_personType(self,person_type):
		#check if arg person_type is not empty
		if person_type!=None:
			if isinstance(person_type, str):#check if its a string
				if person_type=="Fellow" or person_type=="Staff": #check if Person_type is either a fellow or staff
					return person_type
				else:
					raise ValueError("error")
			else:
				raise TypeError(" error")
		else:
			raise ValueError

	#check if person name entered is a string and not empty
	def check_person_name(self,person_name):
		#check if room name  is not empty
		if person_name!=None:
			if isinstance(room_name, str):#check if its a string
				return person_name
			else:
				raise TypeError(" error")
		else:
			raise TypeError(" error")



