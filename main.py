# Setting Doctor Dictionary
doctors = {
    21: {
        "name": "Dr.Gody",                 #  DR NAME
        "specialization": "ENT",           #  DR SPECIALIZATION
        "working_time": "5am-11am",        #  DR WORKING HOURS
        "qualification": "MBBS,MD",        #  DR QUALIFICATIONS
        "room_number": 17                  #  DR ROOM NUMBER @ HOSPITAL
    },
    32: {
        "name": "Dr.Vikram",
        "specialization": "Physician",
        "working_time": "10am-3pm",
        "qualification": "MBBS,MD",
        "room_number": 45
    },
    17: {
        "name": "Dr.Amy",
        "specialization": "Surgeon",
        "working_time": "8am-2pm",
        "qualification": "BDM",
        "room_number": 8
    },
    33: {
        "name": "Dr.David",
        "specialization": "Artho",
        "working_time": "10am-4pm",
        "qualification": "MBBS,MS",
        "room_number": 40
    },
    123: {
        "name": "Dr.Ross",
        "specialization": "Headaches",
        "working_time": "8am-10am",
        "qualification": "Mst",
        "room_number": 102
    },
    66: {
        "name": "Dr.Mike",
        "specialization": "Heart",
        "working_time": "9am-5pm",
        "qualification": "MS",
        "room_number": 2
    }
}
# Setting Patient Dictionary
patients = {
    12: {
        "name": "Pankaj",                       #  PATIENT NAME
        "disease": "Cancer",                    #  PATIENT DISEASE
        "gender": "Male",                       #  PATIENT GENDER
        "age": 30                               #  PATIENT AGE
    },
    13: {
        "name": "Sumit",
        "disease": "Cold",
        "gender": "Male",
        "age": 23
    },
    14: {
        "name": "Alok",
        "disease": "Malaria",
        "gender": "Male",
        "age": 45
    },
    15: {
        "name": "Ravi",
        "disease": "Diabetes",
        "gender": "Male",
        "age": 65
    }
}

class Doctor:
    # Initializing a doctor with the attributes mentioned in Dict
    def __init__(self,doctor_id, name, specialization, working_tIme, qualification,room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
    
    # Getter and Setter for Doctor's Name
    def get_name(self):
        return self.name
    def set_name(self,value):
        self.name = value  

    # Getter and Setter for Doctor's specialization
    def get_specialization(self):
        return self.specialization
    def set_specialization(self, value):
        self.specialization = value

    # Getter and Setter for Doctor's working time
    def get_working_time(self):
        return self.working_time
    def set_working_time(self, value):
        self.working_time =value

    # Getter and Setter for Doctor's qualification
    def get_qualification(self):
        return self.qualification
    def set_qualification(self, value):
        self.qualification = value

    # Getter and Setter for Doctor's room number
    def get_room_number(self):
        self.room_number
    def set_room_number(self, value):
        self.room_number= value

    #The final "string" self
    #!!!! GOOGLE THIS !!!!
    def __str__(self):
        return f"{self.doctor_id:<5} {self.name:<15} {self.specialization:15} {self.working_time:<15} {self.qualification:<15} {self.room_number}"

class DoctorManager:
    #Initializing 'DoctorManager' class with the dictionary of Doctors above
    def __init__(self):
        self.doctors = {id: Doctor(id, **info) for id, info in doctors.items()}

    # Displaying The List of Doctors
    def display_doctors_list(self):
        print("\n ID     NAME               SPECIALITY               TIMING            QUALIFICATION               ROOM NUMBER")
        for doctor in self.doctors.valuse():
            print(str(doctor))

    
    # Searching The Doctor THENNN displaying their details
    # Search for a doctor by name then display their details
    # Adding a new doctor
    # Editing an existing doctor

# class Patient:
    
# class PatientManager:

# class Management: