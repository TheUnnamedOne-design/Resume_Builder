document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("resumeForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const loading = document.getElementById("loading");
    const output = document.getElementById("outputArea");
    output.innerHTML = "";
    loading.style.display = "block";

    const formData = Object.fromEntries(new FormData(e.target).entries());

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
