/////////////////////////////////////////////////////////////////////
//                                                                   /
// DESCRIPTION:                                                      /
// This is a file that after installing a greasemonkey extension can /
// be used to convert yewtu.be to any other invidious instance.      /
// NOTE: I might change this really often because instances may fail./
// variables.                                                        /
//                                                                   /
// LISCENSE INFO (A dedicated liscense file is in the repo.):        /
//      ALL THE CODE IN THIS REPOSITORY INCLUDING THIS FILE IS       /
// (C) Zera Zelix and Other Contributors 2021.                       /
// YOU CAN USE THIS FILE AND ANY OTHER FILE IN THIS REPOSITORY UNDER /
// THE TERMS OF GNU GENERAL PUBLIC LICENSE VERSION 3 OR ANY LATER    /
// VERSION. TO FIND THE FULL TEXT OF THE LICENSE GO TO THE GNU.ORG   /
// WEBSITE AT ( https://www.gnu.org/licenses/gpl-3.0.html ).         /
/////////////////////////////////////////////////////////////////////
// ==UserScript==
// @name           yewtube to invidious
// @namespace      Zera's anti yewtu.be script
// @match          http://yewtu.be/*
// @match          https://yewtu.be/*
// @match          http://yewtu.be/*
// @match          https://yewtu.be/*
// @run-at         document-start
// ==/UserScript==
url = location.href
//url = url.replace(/\bwww\.\b/, "")
//url = url.replace("yewtu.be","watch.thekitty.zone")
location.href = url
