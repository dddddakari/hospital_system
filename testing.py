# Group 16 Link --> https://github.com/dddddakari/finalproject

# Example Doctor class definition

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
        return f"{self.patient_id:<5} {self.name:<15} {self.disease:15} {self.gender:<15} {self.age:<15}"

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


class PatientManager:
    #Initializing 'PatientManager' class with the dictionary of Patients above
    def __init__(self):
        self.patients = {id: Patient(id, **info) for id, info in patients.items()}

    # Display the list of patients
    def display_patients_list(self):
        print("ID    NAME           DISEASE          GENDER         AGE")
        for patient in self.patients.values():
            print(str(patient))

    
# Testing the  class
if __name__ == "__main__":
    manager = PatientManager()
    manager.display_patients_list()





 
