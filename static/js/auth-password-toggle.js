(function () {
  document.querySelectorAll(".form-input-wrap").forEach(function (wrap) {
    const input = wrap.querySelector('input[type="password"]');
    const btn = wrap.querySelector(".form-input-toggle");
    if (!input || !btn) return;

    btn.addEventListener("click", function () {
      const isVisible = input.type === "text";
      input.type = isVisible ? "password" : "text";
      btn.classList.toggle("is-visible", !isVisible);
      btn.setAttribute("aria-pressed", isVisible ? "false" : "true");
      btn.setAttribute("aria-label", isVisible ? "Показать пароль" : "Скрыть пароль");
      btn.title = isVisible ? "Показать пароль" : "Скрыть пароль";
    });
  });
})();
