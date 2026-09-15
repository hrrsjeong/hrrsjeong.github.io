// Keep in-page sections and search parameters when switching languages.
function updateLanguageLinks() {
  document.querySelectorAll("[data-language-link]").forEach((link) => {
    const target = new URL(link.href);
    target.search = window.location.search;
    target.hash = window.location.hash;
    link.href = target.href;
  });
}

updateLanguageLinks();
window.addEventListener("hashchange", updateLanguageLinks);
