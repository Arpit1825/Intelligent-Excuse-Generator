// static/js/script.js

document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.getElementById("themeToggle");
  const form = document.querySelector("form");

  if (toggle) {
    toggle.addEventListener("click", function () {
      document.body.classList.toggle("dark");
      toggle.textContent = document.body.classList.contains("dark")
        ? "☀️ Light Mode"
        : "🌙 Dark Mode";
    });
  }

  if (form) {
    form.addEventListener("submit", function (e) {
      const reasonInput = document.querySelector("input[name='reason']");
      if (!reasonInput) return;

      const reason = reasonInput.value.trim();
      if (reason.length < 3) {
        alert("Please enter a valid reason (at least 3 characters).");
        e.preventDefault();
      }
    });
  }
});
