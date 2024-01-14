import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.google.android.calculator',
    appActivity='com.android.calculator2.Calculator',
    language='en',
    locale='US',
)

capabilities_optional = UiAutomator2Options().load_capabilities(capabilities)

appium_server_url = 'http://localhost:4723'

# @pytest.fixture(scope="session", autouse=True)
# service = AppiumService()
# service.start(args=['-address', 'localhost', '-p', '4723'])
# print(service.is_running)
# print(service.is_listening)
# service.stop()


@pytest.fixture()
def driver():
    app_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield app_driver
    # if driver:
    #     driver.quit()


def test_addition(driver):
    button_seven = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="7"]')
    button_seven.click()
    button_plus = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="plus"]')
    button_plus.click()
    button_three = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="3"]')
    button_three.click()
    button_equals = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="equals"]')
    button_equals.click()
    result = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView["
                                                          "@resource-id='com.google.android.calculator:id"
                                                          "/result_final']").text
    expected_result = '10'
    assert result == expected_result
    driver.quit()


def test_multiplication(driver):
    button_four = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="4"]')
    button_four.click()
    button_multiply = driver.find_element(by=AppiumBy.XPATH,
                                          value='//android.widget.ImageButton[@content-desc="multiply"]')
    button_multiply.click()
    button_six = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="6"]')
    button_six.click()
    button_equals = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="equals"]')
    button_equals.click()
    result = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView["
                                                          "@resource-id='com.google.android.calculator:id"
                                                          "/result_final']").text
    expected_result = '24'
    assert result == expected_result
    driver.quit()


def test_division_by_zero(driver):
    button_eight = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="8"]')
    button_eight.click()
    button_divide = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="divide"]')
    button_divide.click()
    button_zero = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="0"]')
    button_zero.click()
    button_equals = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="equals"]')
    button_equals.click()
    result = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView["
                                                          "@resource-id='com.google.android.calculator:id"
                                                          "/result_preview']").text
    expected_result = "Can't divide by 0"
    assert result == expected_result
    driver.quit()


def test_incorrect_sequence(driver):
    button_percent = driver.find_element(by=AppiumBy.XPATH,
                                         value='//android.widget.ImageButton[@content-desc="percent"]')
    button_percent.click()
    button_six = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="6"]')
    button_six.click()
    button_equals = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="equals"]')
    button_equals.click()
    result = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView["
                                                          "@resource-id='com.google.android.calculator:id"
                                                          "/result_preview']").text
    expected_result = "Format error"
    assert result == expected_result
    driver.quit()