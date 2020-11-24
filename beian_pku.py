from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep

# 学号
id_card = '1901xxxxx'
# 密码
pswd = 'pswd'
# 出校事由
chu_shiyou = '实习'
# 出校轨迹
chu_guiji = '南门'
# 入校事由
ru_shiyou = '回宿舍'
# 居住地所在区
ru_district = '海淀'
# 入校街道
ru_jiedao = '北京大学'


def off_school():
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=option)

    try:
        browser.get(
            'https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal2017&appName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97%A8%E6%88%B7%E6%96%B0%E7%89%88&redirectUrl=https%3A%2F%2Fportal.pku.edu.cn%2Fportal2017%2FssoLogin.do')
        browser.implicitly_wait(10)
        user = browser.find_element_by_xpath("//input[@id='user_name']")
        user.send_keys(id_card)
        pw = browser.find_element_by_xpath("//input[@id='password']")
        pw.send_keys(pswd)

        denglu = browser.find_element_by_xpath("//input[@type='submit']")
        denglu.click()
        browser.implicitly_wait(10)

        crx = browser.find_element_by_xpath("//a[@id = 'stuCampusExEnReq']")
        crx.click()
        browser.implicitly_wait(10)
        browser.switch_to.window(browser.window_handles[1])
        dengji = browser.find_elements_by_xpath("//div[contains(@class, 'box-card')]")
        dengji[0].click()
        sleep(5)

        shiyou = browser.find_element_by_xpath("//textarea[@placeholder='请输入出入校事由']")
        shiyou.send_keys(chu_shiyou)
        print('done')
        xz1 = browser.find_elements_by_xpath("//input[@placeholder='请选择']")[0]
        xz1.click()
        browser.implicitly_wait(10)
        chuxiao = browser.find_elements_by_xpath("//li[contains(@class,'el-select-dropdown__item')]")[-2]
        chuxiao.click()
        guiji = browser.find_element_by_xpath("//textarea[@placeholder='请填写主要停留地点和目的地，如：北大南门—校医院—北医三院—北大东门。']")
        guiji.send_keys(chu_guiji)

        browser.find_element_by_xpath("//span[@class='el-checkbox__inner']").click()
        browser.find_element_by_xpath("//button[@class='el-button el-button--primary el-button--small']").click()
        browser.implicitly_wait(10)
        bts = browser.find_elements_by_xpath("//button[contains(@class,'el-button--primary')]")[2]
        bts.click()

        sleep(5)
        print("success off school")
    finally:
        browser.quit()


def back_to_school():
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=option)

    try:
        browser.get(
            'https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal2017&appName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97%A8%E6%88%B7%E6%96%B0%E7%89%88&redirectUrl=https%3A%2F%2Fportal.pku.edu.cn%2Fportal2017%2FssoLogin.do')
        browser.implicitly_wait(10)
        user = browser.find_element_by_xpath("//input[@id='user_name']")
        user.send_keys(id_card)
        pw = browser.find_element_by_xpath("//input[@id='password']")
        pw.send_keys(pswd)

        denglu = browser.find_element_by_xpath("//input[@type='submit']")
        denglu.click()
        browser.implicitly_wait(10)

        crx = browser.find_element_by_xpath("//a[@id = 'stuCampusExEnReq']")
        crx.click()
        browser.implicitly_wait(10)
        browser.switch_to.window(browser.window_handles[1])
        dengji = browser.find_elements_by_xpath("//div[contains(@class, 'box-card')]")
        dengji[0].click()
        sleep(5)

        shiyou = browser.find_element_by_xpath("//textarea[@placeholder='请输入出入校事由']")
        shiyou.send_keys(ru_shiyou)
        print('done')
        xz1 = browser.find_elements_by_xpath("//input[@placeholder='请选择']")[0]
        xz1.click()
        browser.implicitly_wait(10)
        ruxiao = browser.find_elements_by_xpath("//li[contains(@class,'el-select-dropdown__item')]")[-1]
        ruxiao.click()
        xz2 = browser.find_elements_by_xpath("//input[@placeholder='请选择']")[3]
        xz2.click()
        browser.implicitly_wait(10)
        haidian = browser.find_elements_by_xpath("//li[contains(@class,'el-select-dropdown__item')]")
        for i, item in enumerate(haidian):
            if ru_district in item.text:
                item.click()
        print('done')

        jiedao = browser.find_element_by_xpath("//textarea[@placeholder='请输入居住地所在街道']")
        jiedao.send_keys(ru_jiedao)

        days14 = browser.find_elements_by_xpath("//span[contains(@class,'el-radio__input')]")[0]
        days14.click()

        browser.find_element_by_xpath("//span[@class='el-checkbox__inner']").click()
        browser.find_element_by_xpath("//button[@class='el-button el-button--primary el-button--small']").click()
        browser.implicitly_wait(10)
        bts = browser.find_elements_by_xpath("//button[contains(@class,'el-button--primary')]")[2]
        bts.click()
        print('success back to school')
        sleep(5)
    finally:
        browser.quit()


if __name__ == '__main__':
    off_school()
    back_to_school()
