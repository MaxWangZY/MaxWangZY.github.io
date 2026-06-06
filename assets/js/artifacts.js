document.addEventListener("DOMContentLoaded", () => {
  const artifacts = document.querySelectorAll("[data-artifact]");

  artifacts.forEach((artifact) => {
    const toggle = artifact.querySelector(".artifact-toggle");
    const detail = artifact.querySelector(".artifact-detail");

    if (!toggle || !detail) {
      return;
    }

    toggle.addEventListener("click", () => {
      const isExpanded = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!isExpanded));
      detail.hidden = isExpanded;
      artifact.classList.toggle("is-expanded", !isExpanded);
    });
  });
});
