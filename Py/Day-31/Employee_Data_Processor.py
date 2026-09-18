import csv
import logging


INPUT_FILE = "employees.csv"
OUTPUT_FILE = "engineering_employees.csv"


# Configure logging
logging.basicConfig(
    filename="employee_processor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_employee_data():
    employees = []

    try:
        with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                employees.append(row)

        logging.info(f"Successfully read {len(employees)} employees.")

    except FileNotFoundError:
        logging.error(f"File not found: {INPUT_FILE}")
        print(f"Error: {INPUT_FILE} not found.")

    except Exception as error:
        logging.error(f"Error reading CSV: {error}")
        print(f"Error: {error}")

    return employees


def calculate_salary_statistics(employees):
    if not employees:
        return 0, 0, 0

    salaries = [int(employee["Salary"]) for employee in employees]

    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)
    highest_salary = max(salaries)

    return total_salary, average_salary, highest_salary


def filter_by_department(employees, department):
    return [
        employee
        for employee in employees
        if employee["Department"].lower() == department.lower()
    ]


def save_to_csv(employees):
    if not employees:
        print("No employees to save.")
        return

    fieldnames = employees[0].keys()

    try:
        with open(
            OUTPUT_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(employees)

        logging.info(
            f"Saved {len(employees)} employees to {OUTPUT_FILE}"
        )

        print(f"Exported data to {OUTPUT_FILE}")

    except Exception as error:
        logging.error(f"Error writing CSV: {error}")
        print(f"Error: {error}")


def main():

    print("Employee Data Processor")
    print("-----------------------")

    employees = read_employee_data()

    if not employees:
        return

    print(f"Total employees: {len(employees)}")

    total, average, highest = calculate_salary_statistics(employees)

    print(f"Total salary: ₹{total:,}")
    print(f"Average salary: ₹{average:,.2f}")
    print(f"Highest salary: ₹{highest:,}")

    engineering_employees = filter_by_department(
        employees,
        "HR"
    )

    print(
        f"Engineering employees: "
        f"{len(engineering_employees)}"
    )

    save_to_csv(engineering_employees)


if __name__ == "__main__":
    main()