def search_by_disease(patients, disease):
    return [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]

def main():
    patients = []
    num = input("How many patients you want to enter? ")
    if not num.isdigit():
        print("Invalid number.")
        return
    for i in range(int(num)):
        print(f"\nEnter details for patient {i+1}")
        name = input("Name").strip()
        age = input("Age").strip()
        disease = input("Disease").strip()
        if not age.isdigit():
            print("Invalid age. Skipping this patient.")
            continue
        patient = {
            "Name": name,
            "Age": int(age),
            "Disease": disease
        }
        patients.append(patient)
    search_disease = input("\nEnter disease to search: ").strip()
    result = search_by_disease(patients, search_disease)
    if result:
        print(f"\nPatients with {search_disease}: {result}")
    else:
        print(f"\nNo patients found with {search_disease}.")
if __name__ == "__main__":
    main()
