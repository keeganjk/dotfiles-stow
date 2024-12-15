/*
DESCRIPTION: This is a file that after installing a greasemonkey
extension can be used to convert Google Translate to any
SimplyTranslate instance.

----

Copyright (C) 2021 Vertbyqb and other contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
*/

// ==UserScript==
// @name           Google Translate to SimplyTranslate
// @namespace      Vertbyqb's userscripts
// @match          http://translate.google.com/*
// @match          https://translate.google.com/*
// @run-at         document-start
// ==/UserScript==
SIMPLYTRANSLATE_REDIRECT = "st.tokhmi.xyz"
url = location.href
url = url.replace(/\bwww\.\b/, "")
url = url.replace("translate.google.com",SIMPLYTRANSLATE_REDIRECT)
