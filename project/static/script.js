// Dark mode toggle
document.addEventListener("DOMContentLoaded", () => {
  const modeToggle = document.getElementById("modeToggle");
  const body = document.body;

  // Check for stored mode
  if (localStorage.getItem("theme") === "dark") {
    body.classList.add("dark-mode");
    modeToggle.checked = true;
  }

  modeToggle.addEventListener("change", () => {
    body.classList.toggle("dark-mode");
    localStorage.setItem("theme", body.classList.contains("dark-mode") ? "dark" : "light");
  });

  // Image preview
  const imageUpload = document.getElementById("imageUpload");
  const previewImage = document.getElementById("previewImage");

  imageUpload.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
      previewImage.style.display = "block";
      previewImage.src = URL.createObjectURL(file);
    } else {
      previewImage.style.display = "none";
      previewImage.src = "#";
    }
  });
});