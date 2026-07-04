/** Client-side i18n helper for PyBlocks. */
(function (global) {
  "use strict";

  function normalizeStore(raw) {
    if (!raw) {
      return { locale: "ru", messages: {} };
    }
    if (raw.messages && typeof raw.messages === "object") {
      return { locale: raw.locale || "ru", messages: raw.messages };
    }
    const locale = raw.locale || "ru";
    const messages = {};
    Object.keys(raw).forEach(function (key) {
      if (key !== "locale") {
        messages[key] = raw[key];
      }
    });
    return { locale: locale, messages: messages };
  }

  const store = normalizeStore(global.__I18N__);

  function t(key, fallback, params) {
    const messages = store.messages || {};
    let text = messages[key];
    if (text === undefined || text === null) {
      text = fallback !== undefined ? fallback : key;
    }
    if (params && typeof text === "string") {
      Object.keys(params).forEach(function (name) {
        text = text.replace(new RegExp("\\{" + name + "\\}", "g"), String(params[name]));
      });
    }
    return text;
  }

  global.t = t;
  global.getLocale = function () {
    return store.locale || "ru";
  };
})(window);
