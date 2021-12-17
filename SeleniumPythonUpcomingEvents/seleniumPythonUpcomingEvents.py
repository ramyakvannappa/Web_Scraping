from selenium import webdriver #

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("https://www.python.org/")   # opens new browzer window
event_times = driver.find_elements_by_css_selector(".event-widget time")  # time is inside event-widget class
event_names = driver.find_elements_by_css_selector(".event-widget li a")

# for time in event_times:
#     print(time.text)
#
# for name in event_names:
#     print(name.text)

events ={}
for n in range(0, len(event_times)):
    events[n] = {
    "time": event_times[n].text,
    "name" : event_names[n].text
    }

print(events)
#driver.close() # closes the single active tab
driver.quit() # quit the entire program / multiple browzers