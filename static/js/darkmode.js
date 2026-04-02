/**
 * Dark mode toggle for Phalanx AI Dashboard.
 *
 * Reads the saved preference from localStorage (key: "theme").
 * Falls back to the OS preference via prefers-color-scheme.
 * Persists the user's choice so it survives page reloads.
 */
(function () {
    "use strict";

    var STORAGE_KEY = "theme";
    var DARK = "dark";
    var LIGHT = "light";

    /** Return the preferred theme: saved → OS → light. */
    function getPreferred() {
        var saved = localStorage.getItem(STORAGE_KEY);
        if (saved === DARK || saved === LIGHT) return saved;
        if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
            return DARK;
        }
        return LIGHT;
    }

    /** Apply theme to <html> and persist it. */
    function applyTheme(theme) {
        document.documentElement.setAttribute("data-theme", theme);
        localStorage.setItem(STORAGE_KEY, theme);
    }

    // Apply on load.
    applyTheme(getPreferred());

    // Wire up the toggle button.
    var btn = document.getElementById("dark-mode-toggle");
    if (btn) {
        btn.addEventListener("click", function () {
            var current = document.documentElement.getAttribute("data-theme");
            applyTheme(current === DARK ? LIGHT : DARK);
        });
    }
})();
