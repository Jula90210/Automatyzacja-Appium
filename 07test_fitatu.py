import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test7Appium(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['app'] = PATH('Fitatu.apk')
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Genymotion Cloud'
        desired_caps['udid'] = 'localhost:10000'  # do uzupelnia gdyby nie byl staly
        desired_caps['appPackages'] = 'com.fitatu.tracker'
        desired_caps['appActivity'] = 'com.fitatu.tracker.MainActivity'
        desired_caps['noReset'] = 'true'

        # polaczenie z Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(4)

    def tearDown(self):
        self.driver.quit()

    def testAddMealToBreakfast(self):
        self.driver.find_element_by_id('android:id/aerr_close').click()
        self.driver.find_element_by_class_name('android.widget.Button').click()
        self.driver.find_element_by_class_name('android.view.View').click()
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[0].send_keys('04')
        textfields[1].send_keys('07')
        textfields[2].send_keys('1997')
        textfields[3].send_keys('172')
        textfields[4].send_keys('76')
        textfields[5].send_keys('66')
        self.driver.find_element_by_class_name('android.widget.Button').click()
        self.driver.find_element_by_class_name('android.view.View').click()
        self.driver.find_element_by_class_name('android.widget.Button').click()
        self.driver.find_element_by_xpath('//*[@text="Next"]').click()
        # Sleepy sa potrzebne poniewaz testy przechodza szybciej niz elementy sa widoczne dla frameworka
        sleep(4)
        self.driver.back()
        self.driver.find_element_by_class_name('android.widget.Button').click()
        self.driver.find_element_by_xpath('//*[@text="Next"]').click()
        sleep(4)
        self.driver.find_element_by_xpath('//*[@text="Next"]').click()
        sleep(4)
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        # Aplikacja / wirtualne urzadzenie tez prawdopodobnie ma ustawiana klawiature w jezyku angielskim dlatego
        # ponizej podaje nazwe produktu bez uzywania polskich znakow
        textfields[0].send_keys('platki owsiane')
        self.driver.find_element_by_xpath('//*[@text="# płatki owsiane górskie z biedronki (Plony Natury)"]').click()
        self.driver.find_element_by_xpath('//*[@text="Done"]').click()
        self.driver.find_element_by_xpath('//*[@text="4× tablespoon"]').click()
        sleep(4)

        # assertion
        views = self.driver.find_elements_by_class_name('android.view.View')
        views_names = set([i.text for i in views])
        self.assertTrue(set(['# płatki owsiane górskie z biedronki (Plony Natury)']) <= views_names)


if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test7Appium)
    unittest.TextTestRunner(verbosity=2).run(suite)
