from doctor_consultation_modules import PatientRecord
from doctor_consultation_modules import PatientList
from doctor_consultation_modules import ConsultQueue
from doctor_consultation_modules import patientId

'''
DoctorConsultationSystem keeps  track  of  incoming patients in a hospital.

'''
class DoctorConsultationSystem:
    
    initial_patient_id = 1001 # assigning initial patient Id
    patient_list = PatientList()
    dummy_patient = patientId(1000,00)
    consult_queue = ConsultQueue([dummy_patient])


    #register the name and age of the patient 
    def registerPatient(self, name, age):

        DoctorConsultationSystem.initial_patient_id = DoctorConsultationSystem.initial_patient_id + 1
        value = DoctorConsultationSystem.initial_patient_id
        # make patient record
        patient_record = PatientRecord(name,age,value)
        self.patient_list.append(patient_record)
        #add in Q
        self.enqueuePatient(patient_record.PatId)
        return patient_record.PatId

        
    #assigns  the  patient  a  place  in  the  max  heap depending  on  their  age
    def enqueuePatient(self, PatId):
        self.consult_queue.push(PatId)
    #prints the patient_IDand name of the patient that is next in line to meet the doctor    
    def nextPatient(self):
        next_patient_from_q = self.consult_queue.peek()
        self._dequeuePatient()
        return next_patient_from_q;
    #removes from the queue the patient ID that has consulted the doctor and updates the queue
    def _dequeuePatient(self):
        popped_item = self.consult_queue.pop()
        return popped_item
    
    #read from file
    def doTask(self):
        self.readInputFile(True)
        self.readInputFile(False)
    #write to file    
    def writeOutput(self,retain_q):
        f= open("outputPS5.txt","a+")
        data_available = True
        temp_patient = patientId(1000,00)
        temp_data = ConsultQueue([temp_patient])
        while(data_available):
            item_from_q = self._dequeuePatient()
            if item_from_q.pat_id is not False:
                patient_id_from_q = item_from_q.pat_id
                temp_data.push(patient_id_from_q)
                patient_in_list = self.patient_list.find_element(patient_id_from_q)
                if patient_in_list is False:
                    flag = false;
                    #print('Patient Not found in list')
                else:
                   # f.write(patient_in_list.name + ", " + str(patient_in_list.PatId) +"\n" )
                   f.write(  str(patient_in_list.PatId) + ", " +patient_in_list.name+"\n" )
            else:
                data_available = False
        f.write
        f.close()
        if retain_q is True:
            self.consult_queue = temp_data




    '''to read all records  from the input file 
        sorting as per the max heap and forming the queue based on patient age(descending order)  along with patient Id
        and appending new patient records to the file
    '''
    def readInputFile(self,is_read_type_initial):
        if is_read_type_initial is True:
            f = open("inputPS5a.txt", "r") #reading the inputPS5a file for first time execution 
            file_content = f.readlines()
            for line_entry in range(len(file_content)):
                patinet_name = file_content[line_entry].split(',')[0]
                patinet_age = file_content[line_entry].split(',')[1]
                self.registerPatient(patinet_name,patinet_age)
                output_file = open("outputPS5.txt","w+")
                output_file.write('----initial queue ---------------\n')
                output_file.write("No of patients added: " + str(len(file_content)) + "\nRefreshed queue: \n")
                output_file.close()
            f.close()
            self.writeOutput(True)
        else:
            #reading the inputPS5b file for later execution
            f2 = open("inpuPS5b.txt", "r") 
            file_content = f2.readlines()
            for line_entry in range(len(file_content)):
                line_data = file_content[line_entry]
                if "newPatient: " in line_data:
                    new_patient_detail = line_data.split('newPatient: ')[1]
                    patinet_name = new_patient_detail.split(',')[0]
                    patinet_age = new_patient_detail.split(',')[1]
                    new_patient_id = self.registerPatient(patinet_name,patinet_age)
                    output_file = open("outputPS5.txt","a+")
                    output_file.write('-------------------new patient entered---------------\n')
                    output_file.write('Patient details: ' + patinet_name.strip() +', '+patinet_age.strip()+', '+ str(new_patient_id)+'\n')
                    output_file.write('Refreshed queue:\n')
                    output_file.close()
                    self.writeOutput(True)

                elif "nextPatient" in line_data:
                    output_file = open("outputPS5.txt","a+")
                    output_file.write('--------------------next patient --------------\n')
                    next_patient_from_q_for_consultation = self.nextPatient()
                    if next_patient_from_q_for_consultation.pat_id is not False:

                        patient_consulted = self.patient_list.find_element(next_patient_from_q_for_consultation.pat_id)
                        output_file.write('Next patient for consultation is: ' + str(next_patient_from_q_for_consultation.pat_id) +', '+ patient_consulted.name + '\n')
                        self.patient_list.remove_element(next_patient_from_q_for_consultation.pat_id)
                        output_file.close()
                    else:
                        output_file.write('No Further patient available for consultation \n')
                        output_file.close()
                    
                else:
                    flag = False
                    #print('not expected content')
            f2.close()
            
            
doctorConsultationSystem = DoctorConsultationSystem()
doctorConsultationSystem.doTask()








