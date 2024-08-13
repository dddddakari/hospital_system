# Example Doctor class definition
class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return f"{self.doctor_id:<5}   {self.name:<15} {self.specialization:15} {self.working_time:<15} {self.qualification:<15} {self.room_number}"

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

class DoctorManager:
    def __init__(self):
        self.doctors = {id: Doctor(id, **info) for id, info in doctors.items()}

    def display_doctors_list(self):
        print("")
        for doctor in self.doctors.values():
            print(str(doctor))

# Testing the DoctorManager class
if __name__ == "__main__":
    manager = DoctorManager()
    manager.display_doctors_list()
