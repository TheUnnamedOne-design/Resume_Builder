from flask import Blueprint, request, jsonify
from server.services.openai_service import generate_response

api = Blueprint("api", __name__)

# @api.route("/generate", methods=["POST"])
# def generate():
#     data = request.get_json()
#     name = data.get("name", "")
#     role = data.get("job_role", "")  
#     experience = data.get("experience", "")
#     education = data.get("education", "")
#     skills = data.get("skills", "")

#     prompt = f"""
#     Generate a professional resume and cover letter for:
#     Name: {name}
#     Role: {role}
#     Experience: {experience}
#     Education: {education}
#     Skills: {skills}
#     """

#     try:
#         result = generate_response(prompt)
#         return jsonify({"result": result})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    


@api.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    # ✅ Correctly fetch from JSON — avoid hardcoded strings or incorrect assignments
    target_role = data.get("Target Role", "")
    Company_Target = data.get("Company Target", "")

    # ✅ Basic details
    name = data.get("name", "")
    mail = data.get("email", "")
    number = data.get("number", "")
    Github = data.get("Github", "")
    Portfolio = data.get("Portfolio", "")
    LinkedIn = data.get("LinkedIn", "")

    # ✅ Ensure all are lists (handles both single and multiple values)
    Degree = data.get("Degree", [])
    Institute = data.get("Institute", [])
    Title = data.get("Title", [])
    Link = data.get("link_project", [])
    Description = data.get("Description", [])
    Skill = data.get("Skill", [])
    Exp_Role=data.get("Role",[])
    Exp_Comp=data.get("Company",[])
    Exp_Desc=data.get("Role_Description",[])

    # Normalize to lists if accidentally sent as strings
    def ensure_list(field):
        return field if isinstance(field, list) else [field]

    Degree = ensure_list(Degree)
    Institute = ensure_list(Institute)
    Title = ensure_list(Title)
    Link = ensure_list(Link)
    Description = ensure_list(Description)
    Skill = ensure_list(Skill)
    Exp_Role=ensure_list(Exp_Role)
    Exp_Comp=ensure_list(Exp_Comp)
    Exp_Desc=ensure_list(Exp_Desc)

    
    Education_details = ""
    for i in range(min(len(Degree), len(Institute))):
        Education_details += f"Degree{i+1}: {Degree[i]}\n"
        Education_details += f"Institute{i+1}: {Institute[i]}\n\n"

    
    Project_details = ""
    for i in range(min(len(Title), len(Link), len(Description))):
        Project_details += f"Title{i+1}: {Title[i]}\n"
        Project_details += f"Project link{i+1}: {Link[i]}\n"
        Project_details += f"Description{i+1}: {Description[i]}\n\n"

    
    Skill_details = ""
    for i, skill in enumerate(Skill):
        Skill_details += f"Skill{i+1}: {skill}\n"

    Experience_details = ""
    for i in range(min(len(Exp_Role), len(Exp_Comp), len(Exp_Desc))):
        Experience_details += f"Role{i+1}: {Exp_Role[i]}\n"
        Experience_details += f"Company/Institute{i+1}: {Exp_Comp[i]}\n"
        Experience_details += f"Description{i+1}: {Exp_Desc[i]}\n\n"
   



    prompt=f"""

        Generate a professional resume and cover letter for while referring to the given format as reference tailored to the role of {target_role} at {Company_Target}
        Modify the contents from provided information accordingly. If any recommendations need to be made then make at the end of the resume not in the template itself.
        Do not add brackets [] like this in the resume. Make up your own descriptions if information seems less        

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

    print(prompt)

    try:
        result = generate_response(prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
