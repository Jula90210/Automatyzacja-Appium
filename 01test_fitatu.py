import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test1Appium(unittest.TestCase):
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

    def testIncorrectEmail(self):
        self.driver.find_element_by_id('android:id/aerr_close').click()
        self.driver.find_element_by_xpath('//*[@text="Log in"]').click()
        self.driver.find_element_by_class_name('android.widget.Button').click()
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[0].send_keys('tester.135@wp.pl')
        textfields[1].send_keys('Testy123')
        self.driver.find_element_by_class_name('android.widget.Button').click()
        self.driver.back()

        # assertion
        views = self.driver.find_elements_by_class_name('android.view.View')
        # wydobywam atrybut text z widokow i sprawdzam czy jest informacja o blednym logowaniu
        views_names = set([i.text for i in views])
        self.assertTrue(set(['Login error', 'Incorrect email address or/and password.']) <= views_names)


if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test1Appium)
    unittest.TextTestRunner(verbosity=2).run(suite)
