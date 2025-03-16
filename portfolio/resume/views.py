from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

def home(request):
    projects = [
        {
            "title": "Old Bailey Decisions Prediction Project",
            "description": "Developed a machine learning model to predict court decisions based on historical Old Bailey trial data. Implemented data preprocessing techniques using Pandas and NumPy, optimizing text-based datasets with multiple representations (Glove, TF-IDF, Bag-of-Words). Trained and evaluated models including SVM, Perceptron, Logistic Regression, and Voting Classifier, improving prediction accuracy through hyperparameter tuning and cross-validation..",
            "image": "images/oldml.jpg",
            "github_url": "https://github.com/apekshaan07/Machine-Learning"
        },
        {
            "title": "Portfolio Website",
            "description": "Developed a personal portfolio website using HTML, CSS, Django, and Bootstrap, showcasing projects, skills, and contact details. Integrated a responsive design with a dynamic backend, ensuring seamless navigation and user experience. Implemented Django for scalability, enabling efficient project management and content updates.",
            "image": "images/portfolio.png",
            "github_url": "https://github.com/apekshaan07/Portfolio"
        },
        {
            "title": "Payroll Management System",
            "description": "Developed a Payroll Management System to efficiently handle employee salaries, tax calculations, and attendance tracking using HTML, CSS, JavaScript, SQL, and Python. Designed a secure and scalable database structure, ensuring accurate payroll processing and compliance with tax regulations. Integrated user-friendly interfaces for seamless payroll operations and administrative control.",
            "image": "images/payroll.jpg",
            "github_url": "https://github.com/yourusername/payroll-management"
        }
    ]

    experience = [
        {
            "logo": "images/infogain.jpeg",
            "company": "Infogain India Private Limited",
            "role":"Associate Software Engineer",
            "start_date": "Aug 2022",
            "end_date": "July 2023",
            "description": [
                "Engineered a Responsive Web Design User Management system using HTML, CSS, JavaScript with a Java Spring Boot backend.",
                "Developed and deployed RESTful Web APIs and large-scale microservices applications, improving performance by 15%.",
                "Enhanced Costco Travel Investment Project, improving hotel, flight, and cruise bookings with Java, Spring, JavaScript, increasing engagement by 20%",
                "Collaborated with cross-functional teams to resolve production issues, ensuring 99% uptime and a seamless user experience.",
                "Led Agile SCRUM version control, reducing development time and merge conflicts by 30%, improving team productivity.",
                "Optimized backend integration with the front end, reducing data processing time by 15% and ensuring real-time UI updates.",
                "Diagnosed and resolved critical defects, improving code quality and reducing bug reports by 15%."

               

            ]
        },
        {
            "logo": "images/ek.jpeg",
            "company": "Ekathva Innovations Pvt Ltd",
             "role":"Software Engineer Intern",
            "start_date": "July 2021",
            "end_date": "Sep 2021",
            "description": [
               "Developed an online elective selection system using Python Flask, streamlining course selection for students and administrators.",
               "Integrated Cassandra Database with Flask, enabling real-time data retrieval and improving system responsiveness by 30%.",
               "Designed responsive web pages with HTML, CSS, and JavaScript, enhancing usability and cross-platform compatibility by 40%.",
               "Conducted testing and debugging, ensuring seamless functionality and reducing system downtime by 25%."
            ]
        },
    ]

    certificates = [
        {
            "logo": "images/azure.png",
            "title": "Microsoft Azure Fundamental",
            "issuer": "Microsoft",
            "description": "Foundational knowledge of cloud concepts and Azure services.",
            "link": "certificates/Azure.pdf",
        }
    ]

    education = [
        {
            "logo": "images/utah.png",
            "degree": "Master of Science in Computer Science",
            "institution": "University of Utah",
            "start_date": "08/2023",
            "end_date": "05/2025",
            "description": "Master of Science in Computer Science, focusing on advanced computing concepts, security, and data-driven applications. Gained expertise in software development, system architecture, cybersecurity, and human-centered computing. Worked on projects involving secure system design, machine learning applications, and software security, applying theoretical knowledge to real-world challenges. Developed strong problem-solving, analytical, and technical skills, with a focus on bridging security, privacy, and software engineering principles.",
        },
        {
            "logo": "images/vtu.png",
            "degree": "Bachelor of Engineering in Computer Science",
            "institution": "Visvesvaraya Technological University",
            "start_date": "08/2018",
            "end_date": "07/2022",
            "description": "Bachelor's in Computer Science, focusing on core computing principles, software development, and problem-solving techniques. Gained hands-on experience in data structures, algorithms, database management, web development, and machine learning. Worked on various projects, applying programming skills to real-world applications, including software engineering, cybersecurity, and cloud computing. Developed a strong foundation in coding, analytical thinking, and system design.",
        },
    ]

    return render(request, "home.html", {
        "projects": projects,
        "experience": experience,
        "certificates": certificates,
        "education": education
    })

def resume(request):
    resume_path = "myapp/APEKSHA RESUME.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404)
