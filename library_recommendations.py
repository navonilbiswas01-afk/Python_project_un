import datetime

# ------------------------------------------
# UNIVERSITY LIBRARY BOOK RECOMMENDATION SYSTEM
# ------------------------------------------

# Fixed options using tuple
programmes = ("BCA", "B.Com", "BBA")
levels = ("Beginner", "Intermediate", "Advanced")
purposes = ("Textbook", "Reference", "Research", "Supplementary")


# ------------------------------------------
# LIBRARY CATALOGUE
# List of dictionaries
# ------------------------------------------

library = [

    {
        "id": 101,
        "title": "Advanced Accountancy",
        "author": "R. L. Gupta",
        "subject": "Advanced Corporate Accounting",
        "topics": ["Consolidation of Accounts", "Financial Statements"],
        "programme": "B.Com",
        "level": "Advanced",
        "type": "Reference",
        "year": 2022,
        "availability": True
    },

    {
        "id": 102,
        "title": "Corporate Accounting",
        "author": "S. P. Jain",
        "subject": "Advanced Corporate Accounting",
        "topics": ["Consolidation of Accounts", "Company Accounts"],
        "programme": "B.Com",
        "level": "Intermediate",
        "type": "Textbook",
        "year": 2023,
        "availability": True
    },

    {
        "id": 103,
        "title": "Financial Accounting",
        "author": "T. S. Grewal",
        "subject": "Financial Accounting",
        "topics": ["Financial Statements", "Journal Entries"],
        "programme": "B.Com",
        "level": "Beginner",
        "type": "Textbook",
        "year": 2021,
        "availability": True
    },

    {
        "id": 104,
        "title": "Business Mathematics",
        "author": "J. K. Sharma",
        "subject": "Business Mathematics",
        "topics": ["Ratio Analysis", "Profit and Loss"],
        "programme": "B.Com",
        "level": "Beginner",
        "type": "Supplementary",
        "year": 2022,
        "availability": False
    },

    {
        "id": 105,
        "title": "Cost Accounting",
        "author": "M. N. Arora",
        "subject": "Cost Accounting",
        "topics": ["Cost Analysis", "Budgeting"],
        "programme": "B.Com",
        "level": "Intermediate",
        "type": "Reference",
        "year": 2020,
        "availability": True
    },

    {
        "id": 106,
        "title": "Financial Management",
        "author": "I. M. Pandey",
        "subject": "Financial Management",
        "topics": ["Capital Budgeting", "Financial Planning"],
        "programme": "B.Com",
        "level": "Advanced",
        "type": "Reference",
        "year": 2023,
        "availability": True
    },

    {
        "id": 107,
        "title": "Principles of Management",
        "author": "Harold Koontz",
        "subject": "Management",
        "topics": ["Planning", "Organising"],
        "programme": "BBA",
        "level": "Beginner",
        "type": "Textbook",
        "year": 2021,
        "availability": True
    },

    {
        "id": 108,
        "title": "Marketing Management",
        "author": "Philip Kotler",
        "subject": "Marketing Management",
        "topics": ["Marketing Strategy", "Consumer Behaviour"],
        "programme": "BBA",
        "level": "Intermediate",
        "type": "Reference",
        "year": 2022,
        "availability": True
    },

    {
        "id": 109,
        "title": "Human Resource Management",
        "author": "Gary Dessler",
        "subject": "Human Resource Management",
        "topics": ["Recruitment", "Training"],
        "programme": "BBA",
        "level": "Intermediate",
        "type": "Textbook",
        "year": 2020,
        "availability": False
    },

    {
        "id": 110,
        "title": "Business Economics",
        "author": "H. L. Ahuja",
        "subject": "Business Economics",
        "topics": ["Demand", "Supply"],
        "programme": "BBA",
        "level": "Beginner",
        "type": "Supplementary",
        "year": 2021,
        "availability": True
    },

    {
        "id": 111,
        "title": "Python Programming",
        "author": "John Zelle",
        "subject": "Python Programming",
        "topics": ["Functions", "Loops", "Lists"],
        "programme": "BCA",
        "level": "Beginner",
        "type": "Textbook",
        "year": 2023,
        "availability": True
    },

    {
        "id": 112,
        "title": "Data Structures",
        "author": "Seymour Lipschutz",
        "subject": "Data Structures",
        "topics": ["Linked List", "Stack", "Queue"],
        "programme": "BCA",
        "level": "Intermediate",
        "type": "Reference",
        "year": 2022,
        "availability": True
    },

    {
        "id": 113,
        "title": "Database Management System",
        "author": "Raghu Ramakrishnan",
        "subject": "DBMS",
        "topics": ["SQL", "Normalization"],
        "programme": "BCA",
        "level": "Intermediate",
        "type": "Textbook",
        "year": 2021,
        "availability": True
    },

    {
        "id": 114,
        "title": "Computer Networks",
        "author": "Andrew S. Tanenbaum",
        "subject": "Computer Networks",
        "topics": ["OSI Model", "TCP/IP"],
        "programme": "BCA",
        "level": "Advanced",
        "type": "Reference",
        "year": 2020,
        "availability": False
    },

    {
        "id": 115,
        "title": "Operating Systems",
        "author": "Galvin",
        "subject": "Operating Systems",
        "topics": ["Process Management", "Memory Management"],
        "programme": "BCA",
        "level": "Intermediate",
        "type": "Textbook",
        "year": 2023,
        "availability": True
    },

    {
        "id": 116,
        "title": "Software Engineering",
        "author": "Ian Sommerville",
        "subject": "Software Engineering",
        "topics": ["Software Design", "Testing"],
        "programme": "BCA",
        "level": "Advanced",
        "type": "Research",
        "year": 2022,
        "availability": True
    },

    {
        "id": 117,
        "title": "Computer Fundamentals",
        "author": "P. K. Sinha",
        "subject": "Computer Fundamentals",
        "topics": ["Computer Basics", "Hardware"],
        "programme": "BCA",
        "level": "Beginner",
        "type": "Supplementary",
        "year": 2021,
        "availability": True
    },

    {
        "id": 118,
        "title": "Investment Management",
        "author": "V. K. Bhalla",
        "subject": "Financial Management",
        "topics": ["Portfolio Management", "Investment Analysis"],
        "programme": "B.Com",
        "level": "Advanced",
        "type": "Research",
        "year": 2023,
        "availability": False
    },

    {
        "id": 119,
        "title": "Business Statistics",
        "author": "S. C. Gupta",
        "subject": "Business Mathematics",
        "topics": ["Statistical Analysis", "Probability"],
        "programme": "B.Com",
        "level": "Intermediate",
        "type": "Textbook",
        "year": 2022,
        "availability": True
    },

    {
        "id": 120,
        "title": "Research Methodology",
        "author": "C. R. Kothari",
        "subject": "Research Methodology",
        "topics": ["Research Design", "Data Collection"],
        "programme": "BBA",
        "level": "Advanced",
        "type": "Research",
        "year": 2023,
        "availability": True
    }
]


# ------------------------------------------
# FUNCTION 1: DISPLAY LIBRARY CATALOGUE
# ------------------------------------------

def display_library():

    print("\n========== LIBRARY CATALOGUE ==========")

    for book in library:

        print("\nBook ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Subject:", book["subject"])
        print("Topics:", ", ".join(book["topics"]))
        print("Programme:", book["programme"])
        print("Level:", book["level"])
        print("Type:", book["type"])
        print("Year:", book["year"])

        if book["availability"]:
            print("Availability: Available")
        else:
            print("Availability: Not Available")

        print("--------------------------------------")


# ------------------------------------------
# FUNCTION 2: SEARCH BOOKS
# ------------------------------------------

def search_books():

    print("\nSearch Books By:")
    print("1. Subject")
    print("2. Author")
    print("3. Topic")
    print("4. Programme")
    print("5. Book Type")

    choice = input("Enter your choice: ")

    keyword = input("Enter search keyword: ").strip().lower()

    found = False

    for book in library:

        match = False

        if choice == "1":
            if keyword in book["subject"].lower():
                match = True

        elif choice == "2":
            if keyword in book["author"].lower():
                match = True

        elif choice == "3":
            for topic in book["topics"]:
                if keyword in topic.lower():
                    match = True

        elif choice == "4":
            if keyword in book["programme"].lower():
                match = True

        elif choice == "5":
            if keyword in book["type"].lower():
                match = True

        else:
            print("Invalid search option.")
            return

        if match:
            print("\nBook:", book["title"])
            print("Author:", book["author"])
            print("Subject:", book["subject"])
            print("Type:", book["type"])
            print("Availability:", book["availability"])

            found = True

    if not found:
        print("\nNo matching books found.")


# ------------------------------------------
# FUNCTION 3: CALCULATE RECOMMENDATION SCORE
# ------------------------------------------

def calculate_score(book, student_requirements):

    score = 0

    if book["subject"].lower() == student_requirements["subject"].lower():
        score += 5

    for topic in book["topics"]:
        if topic.lower() == student_requirements["topic"].lower():
            score += 4
            break

    if book["programme"].lower() == student_requirements["programme"].lower():
        score += 2

    if book["level"].lower() == student_requirements["level"].lower():
        score += 3

    if book["type"].lower() == student_requirements["purpose"].lower():
        score += 2

    if book["availability"]:
        score += 1

    return score


# ------------------------------------------
# FUNCTION 4: RECOMMENDATION CATEGORY
# ------------------------------------------

def get_category(score):

    if score >= 14:
        return "Highly Recommended"

    elif score >= 10:
        return "Recommended"

    elif score >= 6:
        return "Moderately Relevant"

    elif score >= 1:
        return "Low Relevance"

    else:
        return "Not Relevant"


# ------------------------------------------
# FUNCTION 5: GENERATE RECOMMENDATIONS
# ------------------------------------------

def recommend_books(student_requirements):

    recommendations = []

    total_books = len(library)

    # Examine every book in the catalogue

    for book in library:

        score = calculate_score(book, student_requirements)

        if score > 0:

            reasons = []

            if book["subject"].lower() == student_requirements["subject"].lower():
                reasons.append("Exact subject match")

            for topic in book["topics"]:
                if topic.lower() == student_requirements["topic"].lower():
                    reasons.append("Topic match")
                    break

            if book["programme"].lower() == student_requirements["programme"].lower():
                reasons.append("Programme match")

            if book["level"].lower() == student_requirements["level"].lower():
                reasons.append("Level match")

            if book["type"].lower() == student_requirements["purpose"].lower():
                reasons.append("Purpose match")

            if book["availability"]:
                reasons.append("Currently available")

            recommendations.append({
                "book": book,
                "score": score,
                "reasons": reasons
            })

    # Sort books according to recommendation score
    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print("\n========== RECOMMENDATION RESULTS ==========")

    print("Total Books Examined:", total_books)
    print("Total Relevant Books:", len(recommendations))

    if len(recommendations) == 0:
        print("\nNo relevant books found.")
        return

    # Availability filtering

    print("\n1. Show all relevant books")
    print("2. Show only available books")

    option = input("Choose availability option: ")

    if option == "2":

        recommendations = [
            item for item in recommendations
            if item["book"]["availability"] == True
        ]

    elif option != "1":

        print("Invalid option. Showing all relevant books.")

    if len(recommendations) == 0:
        print("\nNo available matching books found.")
        return

    # Top-N recommendation using list slicing

    try:
        number = int(input("\nEnter number of recommendations: "))

        if number <= 0:
            print("Please enter a positive number.")
            return

    except ValueError:
        print("Invalid input. Enter a number.")
        return

    top_books = recommendations[:number]

    # Display ranked recommendations

    for rank, item in enumerate(top_books, start=1):

        book = item["book"]
        score = item["score"]

        print("\n======================================")
        print("Rank:", rank)
        print("Book ID:", book["id"])
        print("Book Title:", book["title"])
        print("Author:", book["author"])
        print("Subject:", book["subject"])
        print("Topics:", ", ".join(book["topics"]))
        print("Book Type:", book["type"])

        if book["availability"]:
            print("Availability: Available")
        else:
            print("Availability: Not Available")

        print("Recommendation Score:", str(score) + "/17")
        print("Category:", get_category(score))

        print("\nReason for Recommendation:")

        for reason in item["reasons"]:
            print("-", reason)

        print("======================================")


    # ----------------------------------
    # RECOMMENDATION SUMMARY
    # ----------------------------------

    highly_recommended = 0
    available_books = 0
    total_score = 0
    highest_score = 0

    for item in recommendations:

        score = item["score"]

        total_score += score

        if score >= 14:
            highly_recommended += 1

        if item["book"]["availability"]:
            available_books += 1

        if score > highest_score:
            highest_score = score

    average_score = total_score / len(recommendations)

    print("\n========== RECOMMENDATION SUMMARY ==========")

    print("Total Books Examined:", total_books)
    print("Total Relevant Books:", len(recommendations))
    print("Highly Recommended Books:", highly_recommended)
    print("Currently Available Books:", available_books)
    print("Highest Recommendation Score:", highest_score)
    print("Average Recommendation Score:", round(average_score, 2))

    # Date and time of execution

    current_time = datetime.datetime.now()

    print("\nExecution Date:", current_time.strftime("%d-%m-%Y"))
    print("Execution Time:", current_time.strftime("%I:%M:%S %p"))

    print("\nThank you for using the Library Recommendation System!")


# ------------------------------------------
# FUNCTION 6: SUBJECT-WISE RECOMMENDATION
# ------------------------------------------

def subject_wise_recommendation():

    subject = input("\nEnter subject name: ").strip().lower()

    found = False

    print("\nBooks Related to:", subject)

    for book in library:

        if subject == book["subject"].lower():

            print("\nBook:", book["title"])
            print("Author:", book["author"])
            print("Topics:", ", ".join(book["topics"]))
            print("Level:", book["level"])

            if book["availability"]:
                print("Availability: Available")
            else:
                print("Availability: Not Available")

            found = True

    if not found:
        print("\nNo books found for this subject.")


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

def main():

    print("\n==========================================")
    print(" UNIVERSITY LIBRARY BOOK RECOMMENDATION ")
    print("==========================================")

    while True:

        print("\n1. Display Library Catalogue")
        print("2. Search Books")
        print("3. Generate Book Recommendations")
        print("4. Subject-Wise Recommendation")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            display_library()

        elif choice == "2":

            search_books()

        elif choice == "3":

            print("\nEnter Student Academic Requirements")

            # Programme validation
            while True:

                programme = input("Programme (BCA/B.Com/BBA): ").strip()

                if programme.lower() in [p.lower() for p in programmes]:
                    programme = next(
                        p for p in programmes
                        if p.lower() == programme.lower()
                    )
                    break

                print("Invalid programme. Please try again.")

            # Semester validation
            while True:

                semester = input("Semester (e.g. Semester 4): ").strip()

                if semester:
                    break

                print("Semester cannot be empty.")

            # Subject validation
            while True:

                subject = input("Enter Subject: ").strip()

                if subject:
                    break

                print("Subject cannot be empty.")

            # Topic validation
            while True:

                topic = input("Enter Topic: ").strip()

                if topic:
                    break

                print("Topic cannot be empty.")

            # Academic level validation
            while True:

                level = input(
                    "Level (Beginner/Intermediate/Advanced): "
                ).strip()

                if level.lower() in [l.lower() for l in levels]:
                    level = next(
                        l for l in levels
                        if l.lower() == level.lower()
                    )
                    break

                print("Invalid level. Please try again.")

            # Purpose validation
            while True:

                purpose = input(
                    "Purpose (Textbook/Reference/Research/Supplementary): "
                ).strip()

                if purpose.lower() in [p.lower() for p in purposes]:
                    purpose = next(
                        p for p in purposes
                        if p.lower() == purpose.lower()
                    )
                    break

                print("Invalid purpose. Please try again.")

            # Store student details in dictionary

            student_requirements = {
                "programme": programme,
                "semester": semester,
                "subject": subject,
                "topic": topic,
                "level": level,
                "purpose": purpose
            }

            print("\nStudent Requirements:")
            print(student_requirements)

            recommend_books(student_requirements)

        elif choice == "4":

            subject_wise_recommendation()

        elif choice == "5":

            print("\nExiting the program. Thank you!")
            break

        else:

            print("\nInvalid choice. Please try again.")


# Run the main program

main()
