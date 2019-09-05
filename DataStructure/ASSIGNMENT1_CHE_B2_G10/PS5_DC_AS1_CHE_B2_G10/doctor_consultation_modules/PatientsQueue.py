'''
Contains the patient id in the sequence of the next consultation 
based on the age of the patient.
'''
class ConsultQueue:
	def __init__(self, items=[]):
		self.heap = []
		for i in items:
			self.heap.append(i)
			self.__floatUp(len(self.heap) - 1)

	def push(self, pt_id):
            string_form_ptid = str(pt_id)
            pt_id_length = len(string_form_ptid.strip())
            age_part = string_form_ptid[pt_id_length-2:pt_id_length]
            age = int(age_part)
            ptid_object = patientId(age,pt_id)
            self.heap.append(ptid_object)
            self.__floatUp(len(self.heap) - 1)



	def peek(self):
		if len(self.heap) > 1:
			return self.heap[1]
		else:
			return patientId(False,False)
			
	def pop(self):
		if len(self.heap) > 2:
			self.__swap(1, len(self.heap) - 1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else: 
			max = patientId(False,False)
		return max

	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		parent = index//2
		if index <= 1:
			return
		elif self.heap[index].age > self.heap[parent].age:
			self.__swap(index, parent)
			self.__floatUp(parent)

	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest].age < self.heap[left].age:
			largest = left
		if len(self.heap) > right and self.heap[largest].age < self.heap[right].age:
			largest = right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)

# PatientId 
class patientId:
    	def __init__(self,age,pat_id):
            self.pat_id = pat_id
            self.age = age


