browser_history = []


def visit_web_page(page):  # ['google.com']; ['google.com', 'python.org']; ['google.com', 'python.org', 'python.org/list']
    browser_history.append(page)


def go_back():
    if len(browser_history) > 1:
        current_page = browser_history.pop()
        previous_page = browser_history[-1]
        return previous_page
    else:
        return "Cannot go back further. You are on the first page."


def current_page():
    return browser_history[-1]


visit_web_page("Home Page")  # ['Home Page']
visit_web_page("Page A")     # ['Home Page', 'Page A']
visit_web_page("Page B")     # ['Home Page', 'Page A', 'Page B']

print("Current Page:", current_page())  # 'Page B'
print("Going back...")
previous_page = go_back()               # 'Page A', ['Home Page', 'Page A']
print("Current Page:", previous_page)
print("Going back...")
previous_page = go_back()               # 'Home Page', ['Home Page']
print("Current Page:", previous_page)
