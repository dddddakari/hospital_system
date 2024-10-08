# Group 16 Link --> https://github.com/dddddakari/finalproject

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
    def __init__(self,doctor_id, name, specialization, working_time, qualification,room_number):
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
       return self.room_number
    def set_room_number(self, value):
        self.room_number= value

    #The final "string" self
    #!!!! GOOGLE THIS !!!!
    def __str__(self):
        return f"{self.doctor_id:<5} {self.get_name():<15} {self.get_specialization():15} {self.get_working_time():<15} {self.get_qualification():<15} {self.get_room_number()}"

class DoctorManager:
    #Initializing 'DoctorManager' class with the dictionary of Doctors above
    def __init__(self):
        self.doctors = {id: Doctor(id, **info) for id, info in doctors.items()}

    # Displaying The List of Doctors
    def display_doctors_list(self):
        print("\nID    NAME          SPECIALITY       TIMING         QUALIFICATION   ROOM NUMBER\n")
        for doctor in self.doctors.values():
            print(str(doctor))
    
    # Searching The Doctor THENNN displaying their details
        # COME BACK TO THIS
    def search_doctor_by_id(self, doctor_id):
        doctor_id = int(doctor_id) # Converting the input to integer as I keep getting errors
        doctor = self.doctors.get(doctor_id)
        if doctor:
            print("\nID    NAME           SPECIALITY      TIMING          QUALIFICATION   ROOM NUMBER\n")
            print(str(doctor))
        else:
            print("Can't find the doctor with the same ID in the system.")

    # Search for a doctor by name then display their details
    def search_doctor_by_name(self, name):
        # As to make sure the results are searched and displayed otherwise
        found = False
        # Searching through the dictionary values for the specific name
        for doctor in self.doctors.values():
            if doctor.get_name() == name:
                print("\nID     NAME            SPECIALITY      TIMING          QUALIFICATION   ROOM NUMBER\n")
                print(str(doctor))
                found = True
        if not found:
            print("Can't find the doctor with the same name in the system.")

    # Adding a new doctor
    def add_doctor(self, doctor_id, name, specialization, working_time, qualification, room_number):
        if doctor_id in self.doctors:
            print("A Doctor already exists with this ID.")
        else:
            self.doctors[doctor_id] = Doctor(doctor_id, name, specialization, working_time, qualification,room_number)
            print(f"\n Doctor whose ID is {doctor_id} has been added.")
    # Editing an existing doctor
    def edit_doctor(self, doctor_id, name, specialization, working_time, qualification, room_number):
        doctor = self.doctors.get(doctor_id)
        if doctor:
            doctor.set_name(name)
            doctor.set_specialization(specialization)
            doctor.set_working_time(working_time)
            doctor.set_qualification(qualification)
            doctor.set_room_number(room_number)
            print(f"\n Doctor whose ID is {doctor_id} has been edited.")
        else:
            print("Can't find the doctor with the same ID in the system.")

class Patient:
    # Initializing Patients with required attributes
    def __init__(self, patient_id, name, disease, gender, age):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age 

    # Getter and Setters for Patient's name
    def get_name(self):
        return self.name
    def set_name(self, value):
        self.name = value 

    # Getter and Setters for Patient's disease
    def get_disease(self):
        return self.disease
    def set_disease(self, value):
        self.disease = value

    # Getter and Setters for Patient's gender
    def get_gender(self):
        return self.gender
    def set_gender(self, value):
        self.gender = value

    # Getter and Setters for Patient's age
    def get_age(self):
        return self.age
    def set_age(self, value):
        self.age = value

    # String Representation of the patient
    def __str__(self):
        return f"{self.patient_id:<5} {self.get_name():<15} {self.get_disease():15} {self.get_gender():<15} {self.get_age():<15}"

class PatientManager:
    #Initializing 'PatientManager' class with the dictionary of Patients above
    def __init__(self):
        self.patients = {id: Patient(id, **info) for id, info in patients.items()}

     # Display the list of patients
    def display_patients_list(self):
        print("ID    NAME           DISEASE          GENDER          AGE")
        for patient in self.patients.values():
            print(str(patient))

    # Searching for a patient by ID and showing their details
    def search_patient_by_id(self, patient_id):
        patient_id = int(patient_id) # Coverting to integer to solve error
        patient = self.patients.get(patient_id)
        if patient: 
            print("ID    NAME           DISEASE          GENDER          AGE")
            print(str(patient))
        else:
            print("Can't find the patient with the same ID in the system.")

    # Adding a new patient
    def add_patient(self, patient_id, name, disease, gender, age):
        if patient_id in self.patients:
            print("Patient with this ID already exists.")
        else:
            self.patients[patient_id] = Patient(patient_id, name, disease,gender,age)
            print(f"\nPatient whose ID is {patient_id} has been added.\n")
    # Editing an existing patient
    def edit_patient(self, patient_id, name, disease, gender, age):
        patient = self.patients.get(patient_id)
        if patient:
            patient.set_name(name)
            patient.set_disease(disease)
            patient.set_gender(gender)
            patient.set_age(age)
            print(f"\nPatient whose ID is {patient_id} has been edited.\n")
        else:
            print("Can't find the patient with the same ID in the system.")

class Management:
    # Initializing the Management with the DoctorManager
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    # Displaying the main menu and the choices
    def display_menu(self):
        while True:
            print("\n Welcome to Alberta Hospital (AH) Management system \n Select from the following options, or select 3 to stop: \n 1 - Doctors \n 2 - Patients \n 3 - Exit Program")
            choice = input(">>> ")
            # This leads to the DOCTORS Menu
            if choice =="1":
                self.doctors_menu()
            # This leads to the PATIENTS menu
            elif choice == "2":
                self.patients_menu()
            # This ends the program
            elif choice == "3":
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid Choice, Please Choose from 1, 2 or 3!")     # This is a fail safe incase the user doesn't enter one of the three choices


    # The doctors menu that'll open based on on if you chose choice 1
    def doctors_menu(self):
        while True:
            print("\n Doctors Menu: \n 1- Display Doctors List \n 2 - Search for doctor by ID \n 3 - Search for doctor by name \n 4 - Add doctor \n 5 - Edit doctor info \n 6 - Back to the Main Menu  ")
            choice = input(">>> ")
            # Displays the enter list of doctors
            if choice == "1":
                self.doctor_manager.display_doctors_list()
            # Displays the information of the specific chosen doctor by ID
            elif choice == "2":
                doctor_id = int(input("\n Enter the doctor's ID: ")) # Converting to interger to avoid confusing the computer
                self.doctor_manager.search_doctor_by_id(doctor_id)
            # Displays the information of a specific chosen doctor by name
            elif choice == "3":
                name = input("\n Please enter the doctor's name: ")
                self.doctor_manager.search_doctor_by_name(name)
            # Asks for new doctor's information 
            elif choice == "4":
                doctor_id = int(input("\nEnter this new doctor's ID: "))
                name = input("Enter the doctor's name: ")
                specialization = input("Enter the doctor's specility: ")
                working_time = input("Enter the doctor's timing (e.g., 7am-10pm):")
                qualification = input("Enter the doctor's qualification:")
                room_number = input("Enter the doctor's room number: ")
                self.doctor_manager.add_doctor(doctor_id, name, specialization, working_time, qualification,room_number)
            # Asks which doctor you'd like to edit, then asks you everything you'd like to edit 
            elif choice == "5":
                doctor_id = int(input("\n Please enter the ID of the doctor you want to edit: "))
                name = input("Enter new Name: ")
                specialization = input("Enter new Specialty: ")
                working_time = input("Enter new Timing: ")
                qualification = input("Enter new Qualification: ")
                room_number = int(input("Enter new Room Number: "))
                self.doctor_manager.edit_doctor(doctor_id, name, specialization, working_time, qualification, room_number)
            # A get out option, will bring you back to the main menu
            elif choice == "6":
                break
            # Fail Safe incase the user decides not to choose from the options
            else:
                print("Invalid choice, please choose from 1 to 6!")

    # The Patient's Menu that'll open based on if you chose choice 2
    def patients_menu(self):
        while True:
            print("\n Patients Menu \n 1 - Display Patients list \n 2 - Search for patient by ID \n 3 - Add patient \n 4 - Edit patient info \n 5 - Back to the Main Menu")
            choice = input(">>> ")
            if choice == "1":
                self.patient_manager.display_patients_list()
            elif choice == "2":
                patient_id = int(input("Enter the patient ID: "))
                self.patient_manager.search_patient_by_id(patient_id)
            elif choice == "3":
                patient_id= int(input("Enter the patient's ID: "))
                name = input("Enter the Patient's name: ")
                disease = input("Enter the patient's disease: ")
                gender = input("Enter the Patient's Gender: ")
                age= int(input("Enter the Patient's Age: ")) # Converting to int to avoid confusion
                self.patient_manager.add_patient(patient_id,name, disease, gender, age)
            elif choice == "4":
                patient_id= int(input("Please enter the ID of the patient you want to edit: "))
                name = input("Enter New name: ")
                disease = input("Enter New disease: ")
                gender = input("Enter New Gender: ")
                age= int(input("Enter New Age: ")) # Converting to int to avoid confusion2
                self.patient_manager.edit_patient(patient_id,name, disease, gender, age)
            elif choice == "5":
                break
            else:
                print("Invalid Choice, Please choose from 1 to 5")


if __name__ ==  "__main__":
   hospital_system = Management()
   hospital_system.display_menu()
