from flask import Blueprint, request, jsonify
from server.services.openai_service import generate_response

api = Blueprint("api", __name__)

@api.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    name = data.get("name", "")
    role = data.get("job_role", "")  # fix name mismatch with frontend
    experience = data.get("experience", "")
    education = data.get("education", "")
    skills = data.get("skills", "")

    prompt = f"""
    Generate a professional resume and cover letter for:
    Name: {name}
    Role: {role}
    Experience: {experience}
    Education: {education}
    Skills: {skills}
    """

    try:
        result = generate_response(prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
