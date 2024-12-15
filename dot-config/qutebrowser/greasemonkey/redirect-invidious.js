// ==UserScript==
// @name        redirect.invidious.io
// @namespace   Zera's UserScripts
// @match       https://invidio.xamh.de/*
// @grant       GM_setClipboard
// ==/UserScript==

document.onkeyup=function(e) {
  var e = e || window.event; // for IE to cover IEs window event-object
  if(e.altKey && e.which == 89) {
    GM_setClipboard(window.location.href.replace(window.location.host, "redirect.invidious.io"))
    alert("redirect.invidious.io link has been copied to clipboard")
    return false;
  }
}
