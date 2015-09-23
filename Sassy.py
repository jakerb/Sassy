import sublime, sublime_plugin, urllib, urllib2
class SassyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            page = self.view.substr(sublime.Region(0, self.view.size()))
            encoded = {'sass': page}
            send = urllib.urlencode(encoded)
            url = 'http://178.62.31.223/s/jakebown/sassy/?'
            #url += send
            print(url)
            response = urllib2.urlopen(url, send)
            page = response.read()

            length = self.view.size()
            reg = sublime.Region(0, length)
            sublime.run_command("new_window")
            sublime.active_window().run_command("insert_snippet", {"contents": page})
            #sublime.active_window().open_file(page)
            #sublime.view.replace(0, 1, page)
            
            #self.view.replace(edit, reg, page)

        except Exception as (e):
            response = e;
            print("********* Sassy Error *********")
            print(response)
            print("********* Sassy Exit *********")