from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from server.services.openai_service import generate_response

api = Blueprint("api", __name__)

@api.route("/generate", methods=["POST", "OPTIONS"])
@cross_origin(
    origins=[
        "https://theunnamedone-design.github.io",
        "https://theunnamedone-design.github.io/Resume_Builder",
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_headers=["Content-Type", "Authorization"],
    methods=["POST", "OPTIONS"]
)
def generate():
    data = request.get_json()

    # ✅ (Your logic here stays the same)
    target_role = data.get("Target Role", "")
    Company_Target = data.get("Company Target", "")
    name = data.get("name", "")
    mail = data.get("email", "")
    number = data.get("number", "")
    Github = data.get("Github", "")
    Portfolio = data.get("Portfolio", "")
    LinkedIn = data.get("LinkedIn", "")

    Degree = data.get("Degree", [])
    Institute = data.get("Institute", [])
    Title = data.get("Title", [])
    Link = data.get("link_project", [])
    Description = data.get("Description", [])
    Skill = data.get("Skill", [])
    Exp_Role = data.get("Role", [])
    Exp_Comp = data.get("Company", [])
    Exp_Desc = data.get("Role_Description", [])

    def ensure_list(field):
        return field if isinstance(field, list) else [field]

    Degree = ensure_list(Degree)
    Institute = ensure_list(Institute)
    Title = ensure_list(Title)
    Link = ensure_list(Link)
    Description = ensure_list(Description)
    Skill = ensure_list(Skill)
    Exp_Role = ensure_list(Exp_Role)
    Exp_Comp = ensure_list(Exp_Comp)
    Exp_Desc = ensure_list(Exp_Desc)

    Education_details = "\n".join(
        f"Degree{i+1}: {Degree[i]}\nInstitute{i+1}: {Institute[i]}"
        for i in range(min(len(Degree), len(Institute)))
    )

    Project_details = "\n".join(
        f"Title{i+1}: {Title[i]}\nProject link{i+1}: {Link[i]}\nDescription{i+1}: {Description[i]}"
        for i in range(min(len(Title), len(Link), len(Description)))
    )

    Skill_details = "\n".join(f"Skill{i+1}: {s}" for i, s in enumerate(Skill))

    Experience_details = "\n".join(
        f"Role{i+1}: {Exp_Role[i]}\nCompany{i+1}: {Exp_Comp[i]}\nDescription{i+1}: {Exp_Desc[i]}"
        for i in range(min(len(Exp_Role), len(Exp_Comp), len(Exp_Desc)))
    )

    prompt = f"""
        Generate a professional resume and cover letter tailored to {target_role} at {Company_Target}.
        Modify the contents accordingly, and make recommendations at the end.

        {name} 
        Email: {mail} 
        Phone: {number}  
        LinkedIn: {LinkedIn} 
        GitHub: {Github}  
        Portfolio: {Portfolio}  

        ======================================================================
        EDUCATION
        ======================================================================
        {Education_details}

        ======================================================================
        SKILLS
        ======================================================================
        {Skill_details}

        ======================================================================
        PROJECTS
        ======================================================================
        {Project_details}

        ======================================================================
        EXPERIENCE 
        ======================================================================
        {Experience_details}
    """

    try:
        result = generate_response(prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
