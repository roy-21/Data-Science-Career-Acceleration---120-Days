'''
DEEP DIVE: 13.10 Micro-Challenge: Pickle (The Warning)
Goal: Save a Python Object (Class) to file. 
Deep Dive: Use pickle. Warning: Never unpickle data from untrusted 
sources. It can execute arbitrary code (Security Risk).
'''
import pickle

class PatientData:
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.features = [23.5, 180, 75]  # BMI, height, weight

# Create object
patient = PatientData("John Doe", 45, "Diabetes Type II")

# Save to file
with open('patient.pkl', 'wb') as f:
    pickle.dump(patient, f)
