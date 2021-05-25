import time
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_guest_should_see_button(browser):
    browser.get(link)
    time.sleep(30)
    a = browser.find_element_by_class_name("btn-add-to-basket")
    assert a,"no but"