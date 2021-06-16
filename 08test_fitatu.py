import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test8Appium(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['app'] = PATH('Fitatu.apk')
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Genymotion Cloud'
        desired_caps['udid'] = 'localhost:10000'  # do uzupelnienia gdyby nie byl staly
        desired_caps['appPackages'] = 'com.fitatu.tracker'
        desired_caps['appActivity'] = 'com.fitatu.tracker.MainActivity'
        desired_caps['noReset'] = 'true'

        # polaczenie z Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(4)

    def tearDown(self):
        self.driver.quit()

    def testChooseLanguage(self):
        self.driver.find_element_by_id('android:id/aerr_close').click()
        element = self.driver.find_element_by_class_name('android.widget.Spinner')
        element.click()
        self.driver.is_app_installed('com.fitatu.tracker')
        self.driver.find_element_by_xpath('//*[@text="Polski"]').click()
        sleep(4)
        self.driver.find_element_by_xpath('//*[@text="Utrata masy ciała"]').click()
        # czekam poniewaz test wykonuje sie zbyt szybko i struktura DOM niepoprawnie sie aktualizuje
        # selenium.common.exceptions.StaleElementReferenceException:
        # Message: Cached elements 'By.clazz: android.widget.Button' do not exist in DOM anymore
        sleep(4)
        buttons = self.driver.find_elements_by_class_name('android.widget.Button')
        button_names = set([i.text for i in buttons])
        self.assertTrue(set(['Dalej']) <= button_names)


if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test8Appium)
    unittest.TextTestRunner(verbosity=2).run(suite)
