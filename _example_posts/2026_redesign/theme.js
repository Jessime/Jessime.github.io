/* Runs before CSS is painted to avoid flashing the wrong color scheme. */
(() => {
  "use strict";
  const key = "my-life-in-bio-reading-theme";
  const root = document.documentElement;
  const preference = window.matchMedia("(prefers-color-scheme: dark)");
  let chosen = null;
  try {
    const saved = localStorage.getItem(key);
    if (saved === "light" || saved === "dark") chosen = saved;
  } catch (_) { /* File previews and private browsing may restrict storage. */ }

  const update = () => {
    const mode = chosen || (preference.matches ? "dark" : "light");
    root.dataset.mode = mode;
    root.style.colorScheme = mode;
    const button = document.querySelector(".theme-toggle");
    if (button) {
      const nextMode = mode === "dark" ? "light" : "dark";
      button.setAttribute("aria-label", "Switch to " + nextMode + " mode");
      button.querySelector("span").textContent = nextMode === "dark" ? "Dark mode" : "Light mode";
    }
  };
  update();
  preference.addEventListener("change", () => { if (!chosen) update(); });
  window.addEventListener("storage", (event) => {
    if (event.key !== key && event.key !== null) return;
    chosen = event.newValue === "light" || event.newValue === "dark" ? event.newValue : null;
    update();
  });
  document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector(".theme-toggle");
    button.hidden = false;
    update();
    button.addEventListener("click", () => {
      chosen = root.dataset.mode === "dark" ? "light" : "dark";
      try { localStorage.setItem(key, chosen); } catch (_) { /* Still works this visit. */ }
      update();
    });
    const current = window.location.pathname.split("/").pop();
    document.querySelectorAll(".design-picker a").forEach((link) => {
      if (link.getAttribute("href") === current) link.setAttribute("aria-current", "page");
    });
  });
})();
