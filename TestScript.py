import unittest
import time
import os
import win32com.client
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

__author__ = 'Kan!skA'


# (C)2017,GIST,CDAC


class TTS(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox()
        time.sleep(11)
        cls.driver.maximize_window()
        cls.driver.get("http://tdil-dc.in/tts1/")
        time.sleep(5)

    def test_TTS(self):
        iFolder = ['COMP', 'DO', 'LANG_SPEC', 'MOS', 'MRT', 'OMOS', 'SUS']
        iFile = ['pass', 'DO', 'Lanspec', 'MOS', 'MRT', 'OLDMOS', 'Sus']

        for i, j in zip(iFolder, iFile):
            inputFileName = 'Input/' + i + '/' + j
            iPath = inputFileName + '.txt'
            if os.path.exists(iPath):
                reader = open(iPath, encoding='utf-8')
                lineNumForFile = 1
                for inputData in reader.read().split('\n'):
                    # Select Your Language---------------------------------------------------------------------->
                    Select(self.driver.find_element_by_xpath(".//*[@id='Language']")).select_by_visible_text("Hindi")
                    # Clear the Text Area
                    self.driver.find_element_by_xpath(".//*[@id='ip']").clear()
                    time.sleep(2)
                    # Enter Input in the Text Area
                    self.driver.find_element_by_xpath(".//*[@id='ip']").send_keys(str(inputData))
                    time.sleep(2)
                    # Click on Listen Button
                    self.driver.find_element_by_xpath(".//*[@id='AutoNumber1']/tbody/tr[4]/td[2]/input[2]").click()
                    time.sleep(35)
                    displayed = self.driver.find_elements_by_xpath(".//*[@id='t2vDownloadLink']").__len__()

                    if displayed > 0:
                        # Right-Click on Download Link
                        download = self.driver.find_element_by_xpath(".//*[@id='t2vDownloadLink']")
                        ActionChains(self.driver).move_to_element(download).context_click(download).key_down(
                            Keys.ARROW_DOWN).perform()
                        time.sleep(2)
                        shell = win32com.client.Dispatch("WScript.Shell")
                        shell.SendKeys('k')
                        time.sleep(2)
                        # Path for Keeping Output
                        # Change the language name----------------------------->
                        shell.SendKeys(os.getcwd() + str('\Output\\' + i + '\\Hin_' + i + '_') + str(lineNumForFile))
                        lineNumForFile += 1
                        time.sleep(2)
                        shell.SendKeys('{ENTER}')
                        time.sleep(11)
                    else:
                        errorOutputFileName = inputFileName + '_error'
                        error_out_data_file = open(errorOutputFileName + '.txt', "w", encoding='utf-8')
                        error_out_data_file.write(str(inputData))
                        error_out_data_file.writelines('\n')
                        time.sleep(3)
                        error_out_data_file.close()
            else:
                print('No Input File exists for ' + i)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
