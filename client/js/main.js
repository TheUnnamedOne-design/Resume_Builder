$(document).ready(function () {
  $("#Education .adder-wrapper").on("click", function () {
    appendEducation(); // make sure this function is defined
  });
});

$(document).ready(function () {
  $("#Projects .adder-wrapper").on("click", function () {
    appendProjects(); // make sure this function is defined
  });
});


$(document).ready(function () {
  $("#Skills .adder-wrapper").on("click", function () {
    appendSkills(); // make sure this function is defined
  });
});

$(document).ready(function () {
  $("#Experience .adder-wrapper").on("click", function () {
    appendExperience(); // make sure this function is defined
  });
});

function appendEducation()
{
  var contain=document.querySelector("#Education .container-store");
  var divcont1=document.createElement("div");
  var divcont2=document.createElement("div");
  var divcont3=document.createElement("div");
  var divcont4=document.createElement("div");

  divcont1.setAttribute("class","Field");
  divcont1.textContent="Degree";

  divcont3.setAttribute("class","Input-Field");
  var inp1=document.createElement("input");
  inp1.type="text";
  inp1.name="Degree";
  inp1.placeholder="Degree";
  divcont3.appendChild(inp1);


  divcont2.setAttribute("class","Field");
  divcont2.textContent="Institute";

  divcont4.setAttribute("class","Input-Field");
  var inp2=document.createElement("input");
  inp2.type="text";
  inp2.name="Institute";
  inp2.placeholder="Institute";
  divcont4.appendChild(inp2);
  
  contain.appendChild(divcont1);
  contain.appendChild(divcont3);
  contain.appendChild(divcont2);
  contain.appendChild(divcont4);
}

function appendProjects()
{
  var contain=document.querySelector("#Projects .container-store");
  var divcont1=document.createElement("div");
  var divcont2=document.createElement("div");
  var divcont3=document.createElement("div");
  var divcont4=document.createElement("div");
  var divcont5=document.createElement("div");
  var divcont6=document.createElement("div");

  divcont1.setAttribute("class","Field");
  divcont1.textContent="Title";

  divcont3.setAttribute("class","Input-Field");
  var inp1=document.createElement("input");
  inp1.type="text";
  inp1.name="Title";
  inp1.placeholder="Title";
  divcont3.appendChild(inp1);

  divcont5.setAttribute("class","Field");
  divcont5.textContent="Link:";

  divcont6.setAttribute("class","Input-Field");
  var inp2=document.createElement("input");
  inp2.type="text";
  inp2.name="link_project";
  inp2.placeholder="Repo or deployed link (optional)";
  divcont6.appendChild(inp2);


  divcont2.setAttribute("class","Field");
  divcont2.textContent="Description";

  divcont4.setAttribute("class","Input-Field");
  var inp2=document.createElement("textarea");
  inp2.name="Description";
  inp2.placeholder="Description";
  divcont4.appendChild(inp2);

  var divh1=document.createElement("div");
  var divh2=document.createElement("div");
  var divh3=document.createElement("div");
  var divh4=document.createElement("div");
  
  contain.appendChild(divcont1);
  contain.appendChild(divcont3);
  contain.appendChild(divcont5);
  contain.appendChild(divcont6);
  contain.appendChild(divcont2);
  contain.appendChild(divcont4);

  contain.appendChild(divh1);
  contain.appendChild(divh2);
  contain.appendChild(divh3);
  contain.appendChild(divh4);
}


function appendSkills()
{
  var contain=document.querySelector("#Skills .container-store");
  var divcont1=document.createElement("div");
  var divcont3=document.createElement("div");


  divcont1.setAttribute("class","Field");
  divcont1.textContent="Skill:";

  divcont3.setAttribute("class","Input-Field");
  var inp1=document.createElement("input");
  inp1.type="text";
  inp1.name="Skill";
  inp1.placeholder="Skill";
  divcont3.appendChild(inp1);

  
  contain.appendChild(divcont1);
  contain.appendChild(divcont3);


}

function appendExperience()
{
  var contain=document.querySelector("#Experience .container-store");
  var divcont1=document.createElement("div");
  var divcont2=document.createElement("div");
  var divcont3=document.createElement("div");
  var divcont4=document.createElement("div");
  var divcont5=document.createElement("div");
  var divcont6=document.createElement("div");

  divcont1.setAttribute("class","Field");
  divcont1.textContent="Role";

  divcont3.setAttribute("class","Input-Field");
  var inp1=document.createElement("input");
  inp1.type="text";
  inp1.name="Role:";
  inp1.placeholder="Role";
  divcont3.appendChild(inp1);

  divcont5.setAttribute("class","Field");
  divcont5.textContent="Company/Institute:";

  divcont6.setAttribute("class","Input-Field");
  var inp2=document.createElement("input");
  inp2.type="text";
  inp2.name="Company";
  inp2.placeholder="Company/Institute name";
  divcont6.appendChild(inp2);


  divcont2.setAttribute("class","Field");
  divcont2.textContent="Role Description";

  divcont4.setAttribute("class","Input-Field");
  var inp2=document.createElement("textarea");
  inp2.name="Role_Description";
  inp2.placeholder="Role Description";
  divcont4.appendChild(inp2);

  var divh1=document.createElement("div");
  var divh2=document.createElement("div");
  var divh3=document.createElement("div");
  var divh4=document.createElement("div");
  
  contain.appendChild(divcont1);
  contain.appendChild(divcont3);
  contain.appendChild(divcont5);
  contain.appendChild(divcont6);
  contain.appendChild(divcont2);
  contain.appendChild(divcont4);

  contain.appendChild(divh1);
  contain.appendChild(divh2);
  contain.appendChild(divh3);
  contain.appendChild(divh4);
}




document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("Resume").addEventListener("submit", async (e) => {
    e.preventDefault();

    const loading = document.getElementById("loading");
    const output = document.getElementById("outputArea");
    output.innerHTML = "";
    loading.style.display = "block";


    const formData = {};
    const rawFormData = new FormData(e.target);
    
    for (const [key, value] of rawFormData.entries()) {
      if (!formData[key]) {
        formData[key] = [];
      }
      formData[key].push(value);
    }
    
    
    console.log("Form data:", formData);


   // 🌐 Set base URL depending on environment
    const baseURL = window.location.hostname.includes("localhost")
      ? "http://localhost:5000" // Local dev
      : "https://resume-builder-cbjz.onrender.com"; // Render backend


    try {
      const response = await fetch(`${baseURL}/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
      });

      const data = await response.json();
      loading.style.display = "none";

      if (data.result) {
        output.innerText = data.result;
      } else {
        output.innerText = "❌ Something went wrong. Check backend.";
      }
    } catch (error) {
      loading.style.display = "none";
      output.innerText = "❌ Error: " + error.message;
      console.error("Fetch error:", error);
    }
  });
});
