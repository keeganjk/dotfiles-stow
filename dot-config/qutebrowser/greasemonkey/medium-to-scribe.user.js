/*
DESCRIPTION: This is a file that after installing a greasemonkey
extension can be used to convert Medium blogs to a Scribe link.

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
// @name           Medium to Scribe
// @namespace      Vertbyqb's userscripts
// @include        *medium.com*
// @include        *codeburst.io*
// @include        *uxdesign.cc*
// @include        *blog.devgenius.io*
// @include        *towardsdatascience.com*
// @include        *betterprogramming.pub*
// @include        *gitconnected.com*
// @grant          none
// @run-at         document-start
// ==/UserScript==

url = location.href
url = url.replace(/\bwww\.\b/, "")
if (window.location.href.includes(window.location.host)){
  url = window.location.href.replace(window.location.host,"scribe.rip")
  location.href = url
}
