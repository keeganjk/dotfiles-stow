OPENDIR = '/home/user/'
# Consider disabling or modifying search history display
config.load_autoconfig(False)
#c.completion.open_categories = ["history", "searchengines"]
c.completion.shrink = True
c.downloads.location.directory = "/home/user/tmp/"
c.editor.command = ['st', '-e', 'nvim', '{}']
c.fileselect.handler = 'external'
c.fileselect.folder.command = ['st', '-e', 'ranger', OPENDIR, '--choosedir={}']
c.fileselect.multiple_files.command = ['st', '-e', 'ranger', OPENDIR, '--choosefiles={}']
c.fileselect.single_file.command = ['st', '-e', 'ranger', OPENDIR, '--choosefile={}']
c.fonts.default_size = "11pt"
#c.url.default_page = "about:blank"
c.url.default_page = "qute://start"
c.url.start_pages = "about:blank"
c.colors.statusbar.private.bg = "#AA00AA"
c.colors.statusbar.private.fg = "#FFFFFF"
c.colors.statusbar.command.private.bg = "#AA00AA"
c.colors.statusbar.command.private.fg = "#FFFFFF"

SEARX_SEARCH = "https://search.canoemail.net/search?q={}&safesearch=2"
INVIDIOUS_SEARCH = "https://invidious.einfachzocken.eu/search?q={}"
TEDDIT_SEARCH = "https://redlib.zaggy.nl/r/all/search?q={}"
WIKILESS_SEARCH = "https://wikiless.tiekoetter.com/w/index.php?lang=en&search={}&title=Special%3ASearch&fulltext=Search"

c.url.searchengines = {
	"DEFAULT":"https://duckduckgo.com/?q={}",
	"?ar":"https://archive.org/search?query={}",
    "?arpd":"https://archive.org/search?query=licenseurl%3A*publicdomain*+{}",
    "?arp":"https://archive.org/search?query=licenseurl%3A*publicdomain*+{}",
	"?at":"https://alternativeto.net/browse/search/?q={}",
    #"?az":"https://simpleamazon.esmailelbob.xyz/s?k={}",
    "?az":"https://www.amazon.com/s?k={}",
	"?aur":"https://aur.archlinux.org/packages?O=0&K={}",
	"?aw":"https://wiki.archlinux.org/index.php?search={}",
	#"?dc":"https://www.discogs.com/search/?q={}&type=all",
	"?ddg":"https://duckduckgo.com/?q={}",
	"?ddgi":"https://duckduckgo.com/?q={}&t=h_&iax=images&ia=images",
	"?dcc":"https://www.dict.cc/?s={}",
	#"?ec":"https://www.ecosia.org/search?method=index&q={}",
	#"?eci":"https://www.ecosia.org/images?q={}",
	"?et":"https://www.etymonline.com/search?q={}",
	"?eb":"https://www.ebay.com/sch/i.html?_from=&_nkw={}",
	#"?gh":"https://github.com/search?q={}&type=repositories",
    "?gu":"https://gutenberg.org/ebooks/search/?query={}&submit_search=Go%21",
	"?j":"https://jisho.org/search/{}",
	#"?mw":"https://www.merriam-webster.com/dictionary/{}",
	#"?na":"https://www.newadvent.org/utility/search.htm?q={}",
	"?od":"https://odysee.com/$/search?q={}",
	"?oed":"https://www.oed.com/dictionary/{}",
	#"?sx":SEARX_SEARCH,
    "?sfr":"https://www.sefaria.org/search?q={}",
	"?the":"https://www.thesaurus.com/browse/{}",
	"?ud":"https://www.urbandictionary.com/define.php?term={}",
	"?wbm":"https://web.archive.org/web/*/{}",
	#"?we":"https://webstersdictionary1828.com/Dictionary/{}",
	"?wi":"https://wiby.me/?q={}",
	"?wp":WIKILESS_SEARCH,
	"?wkt":"https://en.wiktionary.org/w/index.php?search={}",
	"?wktt":"https://en.wiktionary.org/wiki/Special:Search?search={}",
	"?yt":"https://www.youtube.com/results?search_query={}",
	"?ytm":"https://music.youtube.com/search?q={}",
	#"?yx":"https://yandex.com/search/?text={}",
}

config.bind('A', 'hint links run open -p {hint-url}')
config.bind(',a', 'hint links spawn setsid st -e mpv --no-video {hint-url}')
config.bind(',A', 'spawn setsid kill "$(cat /tmp/AUDIOPID)"')
config.bind(',c', 'config-edit')
config.bind(',i', 'edit-text')
config.bind(',j', 'config-cycle content.javascript.enabled')
config.bind(',r', 'config-source')
config.bind(',R', 'greasemonkey-reload')
config.bind(',t', 'config-cycle content.javascript.can_open_tabs_automatically')
config.bind(',u', 'view-source --edit')
config.bind(',U', 'hint links spawn view-source --edit')
config.bind(',v', 'hint links spawn setsid mpv --force-window=immediate {hint-url}')
config.bind(',V', 'spawn setsid mpv --force-window=immediate {url}')
config.bind(',y', 'hint links yank')
config.bind('"', 'cmd-set-text -s :open -t -r') # obsolete now...
config.bind('|', 'cmd-set-text -s :open -t -r')
config.bind('\\', ':open -t -r about:blank')
config.bind("<Alt-9>", "tab-focus 9")
config.bind("<Alt-0>", "tab-focus 10")
config.bind("<Alt-->", "tab-focus 11")
config.bind("<Alt-=>", "tab-focus 12")
config.bind("<Alt-backspace>", "tab-focus 13")

# fake keys for navigation without needing to go into insert mode
config.bind("<Alt-c>", "fake-key c")
config.bind("<Alt-f>", "fake-key f")
config.bind("<Alt-m>", "fake-key m")
config.bind("<Alt-Shift-P>", "fake-key <Shift-P>")
config.bind("<Alt-Shift-N>", "fake-key <Shift-N>")

# see input.forward_unbound_keys
