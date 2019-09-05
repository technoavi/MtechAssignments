# Patient record including the patient name, age and the patient number 
class PatientRecord:

	def __init__(self, name,age,pid):
		self.PatId = str(pid).strip() + str(age).strip()
		self.name = name 
		self.age = age
		self.next = None
		self.prev = None
        
#list containing the patient informations 
class PatientList:
	def __init__(self):
		self.head = None

	def append(self, patient_record): 

		new_node = patient_record

		new_node.next = None

		if self.head is None: 
			new_node.prev = None
			self.head = new_node 
			return

		last = self.head 
		while(last.next is not None): 
			last = last.next

		last.next = new_node 

		new_node.prev = last 

		return

	def printList(self, node): 

		print "\nAll Patients"
		while(node is not None): 
			print "Patient Id is : % s" %(node.PatId)+" name is : % s" %(node.name) +" Age is : % s" %(node.age)+"\n",
			last = node 
			node = node.next
    #find Patient by Id        
	def find_element(self, patient_id):
		current = self.head
		while(current is not None):
			if int(current.PatId) == int(patient_id):
				return current
			current = current.next
			 
		return False


	def remove_element(self, patient_id):
		current = self.head
		while(current is not None):
			if int(current.PatId) == int(patient_id):
				if current.prev is None:
					self.head = current.next
					return True
				elif current.next is None:
					current.prev.next = None
					return True
				else:
					current.prev.next = current.next
					return True
			else:
				current = current.next
			
			 
		return False