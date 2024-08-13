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
        print("\nID     NAME            SPECIALITY      TIMING          QUALIFICATION   ROOM NUMBER")
        for doctor in self.doctors.values():
            print(str(doctor))
    
    # Searching The Doctor THENNN displaying their details
        # COME BACK TO THIS
    def search_doctor_by_id(self, doctor_id):
        doctor = self.doctors.get(doctor_id)
        if doctor:
            print("\nID     NAME            SPECIALITY      TIMING          QUALIFICATION   ROOM NUMBER")
            print(str(doctor))
        else:
            print("Can't find the doctor with the same ID in the system.")

    # Search for a doctor by name then display their details
    def search_doctor_by_name(self, name):
        # As to make sure the results are searched and displayed otherwise
        found = False
        print("\nID     NAME            SPECIALITY      TIMING          QUALIFICATION   ROOM NUMBER")
        # Searching through the dictionary values for the specific name
        for doctor in self.doctors.values():
            if doctor.get_name() == name:
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
            print("Doctor whose ID is {doctor_id} has been added.")
    # Editing an existing doctor
    def edit_doctor():

# class Patient:
    
# class PatientManager:

class Management:


    # Displaying the main menu and the choices
    def display_menu(self):
        print("Welcome to Alberta Hospital (AH) Management system \n Select from the following options, or select 3 to stop: \n 1 - Doctors \n 2 - Patients \n 3 - Exit Program \n")
        choice = input(">>> ")
        # This leads to the DOCTORS Menu
        if choice =='1':
            self.doctors_menu()
        # This ends the program
        elif choice == '3':
            print("Thanks for using the program. Bye!")
        # This is a fail safe incase the user doesn't enter one of the three choices
        else:
            print("Invalid Choice, Please Choose from 1, 2 or 3!")

    # The doctors menu that'll open based on on if you chose choice 1
    def doctors_menu(self):
        print("\n Doctors Menu: \n 1- Display Doctors List \n 2 - Search for doctor by ID \n 3 - Search for doctor by name \n 4 - Add doctor \n 5 - Edit doctor info \n 6 - Back to the Main Menu  ")
        choice = input(">>> ")
        # Displays the enter list of doctors
        if choice == "1":
            self.doctor_manager.display_doctors_list()
        # Displays the information of the specific chosen doctor by ID
        elif choice == "2":
            doctor_id = input("Enter the doctor's ID: ")
            self.doctor_manager.search_doctor_by_id(doctor_id)
        # Displays the information of a specific chosen doctor by name
        elif choice == "3":
            name = input("Please enter the doctor's name: ")
            self.doctor_manager.search_doctor_by_name(name)
        # Asks for new doctor's information 
        elif choice == "4":
            doctor_id = int(input("Enter this new doctor's ID: "))
            name = input("Enter the doctor's name: ")
            specialization = input("")
            working_time = input("")
            qualification = input("")
            room_number = input("")
            self.doctor_manager.add_doctor(doctor_id, name, specialization, working_time, qualification,room_number)
        #
        elif choice == "5":
        #
        elif choice == "6":
        # Fail Safe incase the user decides not to choose from the options
        else:
            print("Invalid choice, please choose from 1 to 6!")