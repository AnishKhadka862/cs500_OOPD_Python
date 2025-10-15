class Education:
    def __init__(self, institution, degree, year_completed):
        # Private fields
        self.__institution = institution
        self.__degree = degree
        self.__year_completed = year_completed

    @property
    def institution(self):
        return self.__institution

    @institution.setter
    def institution(self, value):
        self.__institution = value

    @property
    def degree(self):
        return self.__degree

    @degree.setter
    def degree(self, value):
        self.__degree = value

    @property
    def year_completed(self):
        return self.__year_completed

    @year_completed.setter
    def year_completed(self, value):
        self.__year_completed = value

    def __str__(self):
        return f"Institution: {self.__institution}, Degree: {self.__degree}, Year: {self.__year_completed}"


class Extracurricular:
    def __init__(self, activity_name, description):
        self.__activity_name = activity_name
        self.__description = description

    @property
    def activity_name(self):
        return self.__activity_name

    @activity_name.setter
    def activity_name(self, value):
        self.__activity_name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def __str__(self):
        return f"Activity: {self.__activity_name}, Description: {self.__description}"


class Applicant:
    def __init__(self, full_name, contact_number, email, address):
        # Keeping applicant details private
        self.__full_name = full_name
        self.__contact_number = contact_number
        self.__email = email
        self.__address = address

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def contact_number(self):
        return self.__contact_number

    @contact_number.setter
    def contact_number(self, value):
        self.__contact_number = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value


class Application:
    def __init__(self, applicant, program_name):
        # Encapsulating sensitive fields
        self.__applicant = applicant
        self.__program_name = program_name
        self.__education_records = []
        self.__extracurriculars = []
        self.__status = "Pending"

    @property
    def applicant(self):
        return self.__applicant

    @property
    def program_name(self):
        return self.__program_name

    @program_name.setter
    def program_name(self, value):
        self.__program_name = value

    @property
    def education_records(self):
        return self.__education_records

    @property
    def extracurriculars(self):
        return self.__extracurriculars

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    # Add a new education record for the applicant
    def add_education(self, education):
        self.__education_records.append(education)

    # Add a new extracurricular activity
    def add_extracurricular(self, activity):
        self.__extracurriculars.append(activity)

    def __str__(self):
        # Preparing education list in string form
        edu_str = ""
        for edu in self.__education_records:
            edu_str += str(edu) + "\n"

        # Preparing extracurricular list in string form
        extra_str = ""
        for act in self.__extracurriculars:
            extra_str += str(act) + "\n"

        return (
            f"Applicant: {self.__applicant.full_name}\n"
            f"Contact: {self.__applicant.contact_number}, Email: {self.__applicant.email}\n"
            f"Address: {self.__applicant.address}\n"
            f"Program Applied For: {self.__program_name}\n"
            f"Status: {self.__status}\n"
            f"Education:\n{edu_str if edu_str else 'None'}"
            f"Extracurricular:\n{extra_str if extra_str else 'None'}"
        )


class AdmissionSystem:
    def __init__(self):
        # Holding all applications in a private list
        self.__applications = []

    # Add a new application
    def add_application(self, application):
        self.__applications.append(application)

    # Find application by name
    def find_application(self, full_name):
        for app in self.__applications:
            if app.applicant.full_name.lower() == full_name.lower():
                return app
        return None

    # Search application by name, program, or education
    def search_application(self, keyword):
        results = []
        for app in self.__applications:
            if (
                keyword.lower() in app.applicant.full_name.lower()
                or keyword.lower() in app.program_name.lower()
            ):
                results.append(app)
            else:
                for edu in app.education_records:
                    if keyword.lower() in edu.institution.lower() or keyword.lower() in edu.degree.lower():
                        results.append(app)
                        break
        return results

    # Update application (status, applicant info, program) with confirmation
    def update_application(self, full_name):
        app = self.find_application(full_name)

        if app is None:
            print("Application not found.")
            return False

        while True:
            print("\nUpdate Menu:")
            print("1. Update Application Status")
            print("2. Update Applicant Information")
            print("3. Update Program Applied For")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                status = input("Enter new status (Pending/Reviewed/Accepted/Rejected): ")
                confirm = input(f"Confirm update status to '{status}'? (y/n): ")
                if confirm.lower() == "y":
                    app.status = status
                    print("Status updated successfully.")
                else:
                    print("Status update cancelled.")

            elif choice == "2":
                new_name = input(f"Full Name ({app.applicant.full_name}): ") or app.applicant.full_name
                new_contact = input(f"Contact Number ({app.applicant.contact_number}): ") or app.applicant.contact_number
                new_email = input(f"Email ({app.applicant.email}): ") or app.applicant.email
                new_address = input(f"Address ({app.applicant.address}): ") or app.applicant.address

                print("\nPlease confirm the new details:")
                print(f"Full Name: {new_name}")
                print(f"Contact Number: {new_contact}")
                print(f"Email: {new_email}")
                print(f"Address: {new_address}")

                confirm = input("Apply these changes? (y/n): ")
                if confirm.lower() == "y":
                    app.applicant.full_name = new_name
                    app.applicant.contact_number = new_contact
                    app.applicant.email = new_email
                    app.applicant.address = new_address
                    print("Applicant information updated successfully.")
                else:
                    print("Applicant update cancelled.")

            elif choice == "3":
                new_program = input(f"Program Applied For ({app.program_name}): ") or app.program_name
                confirm = input(f"Confirm update program to '{new_program}'? (y/n): ")
                if confirm.lower() == "y":
                    app.program_name = new_program
                    print("Program updated successfully.")
                else:
                    print("Program update cancelled.")

            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

        return True

    # Delete an application by applicant name
    def delete_application(self, full_name):
        app = self.find_application(full_name)
        if app:
            self.__applications.remove(app)
            return True
        return False

    # Display all applications
    def display_applications(self):
        if len(self.__applications) == 0:
            print("No applications available.")
        else:
            for app in self.__applications:
                print(app)
                print()


# menu-driven interface

def main():
    system = AdmissionSystem()

    while True:
        print("\nAdmission System Menu:")
        print("1. Add Application")
        print("2. Search Application")
        print("3. Update Application")
        print("4. Delete Application")
        print("5. Display All Applications")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Full Name: ")
            contact = input("Contact Number: ")
            email = input("Email: ")
            address = input("Address: ")
            program = input("Program Applied For: ")

            applicant = Applicant(name, contact, email, address)
            application = Application(applicant, program)

            while True:
                add_edu = input("Add Education Record? (y/n): ")
                if add_edu.lower() == "y":
                    inst = input("Institution: ")
                    degree = input("Degree/Level: ")
                    year = input("Year Completed: ")
                    application.add_education(Education(inst, degree, year))
                else:
                    break

            while True:
                add_extra = input("Add Extracurricular Activity? (y/n): ")
                if add_extra.lower() == "y":
                    act = input("Activity Name: ")
                    desc = input("Description: ")
                    application.add_extracurricular(Extracurricular(act, desc))
                else:
                    break

            system.add_application(application)
            print("Application added successfully.")

        elif choice == "2":
            keyword = input("Enter name, program, or education keyword to search: ")
            results = system.search_application(keyword)
            if len(results) == 0:
                print("No applications found.")
            else:
                for app in results:
                    print(app)

        elif choice == "3":
            name = input("Enter applicant name to update: ")
            system.update_application(name)

        elif choice == "4":
            name = input("Enter applicant name to delete: ")
            if system.delete_application(name):
                print("Application deleted successfully.")
            else:
                print("Application not found.")

        elif choice == "5":
            system.display_applications()

        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
