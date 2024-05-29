def main():
    # Open the file for reading
    try:
        with open("students.txt", "r") as file:
            
            lines = file.readlines()
            highest_gwa = 0
            highest_gwa_student = ""

            
            for line in lines:
                name, gwa = line.strip().split(",")
                # Convert GWA to float
                gwa = float(gwa)

                
                if gwa > highest_gwa:
                    highest_gwa = gwa
                    highest_gwa_student = name

            # Output the student with the highest GWA
            print("Student with the highest GWA:")
            print("Name:", highest_gwa_student)
            print("GWA:", highest_gwa)

    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()
