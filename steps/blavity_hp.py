
from environment import *


def verify_adv():
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
      (By.XPATH, "(//div[@class='adgrid-ad-container'])[1]")))
    adv = driver.find_element(By.XPATH, "(//div[@class='adgrid-ad-container'])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", adv)
    time.sleep(3)
    adv_1 = driver.find_element(By.XPATH, "(//div[@id='google_ads_iframe_/11462305847/bla/hp_0__container__'])[1]")
    adv_1.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("HP"))
    print("Current Window Title for adv Link is : ", driver.title)
    assert "HP" in driver.title, "title text does not match"
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_nav_bar_blavity_hp():
    print("function called verify_nav_bar_blavity_hp")
    nav_bar = driver.find_element(By.XPATH, "//div[@class='container-fluid d-flex align-items-center']")
    print(nav_bar.text)
    assert nav_bar.text is not None and nav_bar.text != "", "navBar tabs are missing for blavity HP tab"


def verify_footer_presence():
    footer = driver.find_element(By.XPATH, "//footer[@class='app-footer text-center text-desktop-left text-white']")
    actions = ActionChains(driver)
    actions.move_to_element(footer).perform()
    assert footer.is_displayed(), "footer not present for blavity hp tab"


def verify_hero_card():
    print("function called verify_hero_card")
    hero_card = driver.find_element(By.XPATH, "//h1[@class='hp__hero__title']")
    # print(hero_card.text)
    assert hero_card.text is not None and hero_card.text != "", "Hero Card Text is not present"
    digital_equity_text = driver.find_element(By.XPATH, "//div[@class='hp__hero__copy']")
    # print(digital_equity_text.text)
    assert digital_equity_text.text is not None and digital_equity_text.text != "", "Digital Equity Text is not present"
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
      (By.XPATH, "//img[@alt='Blavity | HP']")))
    hero_img = driver.find_element(By.XPATH, "//img[@alt='Blavity | HP']")
    image_present = driver.execute_script(
      "return arguments[0].complete && typeof arguments[0].naturalWidth "
      "!= \"undefined\" && arguments[0].naturalWidth > 0",
      hero_img)
    if image_present:
        print("Hero card Image displayed.")
    else:
        print("Hero card Image not displayed.")
        assert image_present, "Hero card image is not displayed for blavity HP page"
    img_hp = driver.find_element(By.XPATH, "//img[@class='hp__hero__logo--hp']")
    actions = ActionChains(driver)
    actions.move_to_element(img_hp).perform()
    image_present = driver.execute_script(
      "return arguments[0].complete && typeof arguments[0].naturalWidth "
      "!= \"undefined\" && arguments[0].naturalWidth > 0",
      img_hp)
    if image_present:
        print("HP Image displayed.")
    else:
        print("HP Image not displayed.")
        assert image_present, "HP image is not displayed for blavity HP page :"


def verify_blavity_hp_digital():
    print("function called verify_blavity_hp_digital")
    header = driver.find_element(By.XPATH, "//h2[@class='hp__intro__title text-uppercase']")
    actions = ActionChains(driver)
    actions.move_to_element(header).perform()
    print(header.text)
    assert header.text is not None and header.text != "", "HP Digital Text is not present"
    desc = driver.find_element(By.XPATH, "//p[@class='hp__intro__description']")
    print(desc.text)
    assert desc.text is not None and desc.text != "", "HP Digital description is not present"
    watch_video_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Watch Video']")
    actions = ActionChains(driver)
    actions.move_to_element(watch_video_btn).perform()
    assert watch_video_btn.is_displayed(), "watch video button is not displayed"
    watch_video_btn.click()
    # video = driver.find_element(By.XPATH, "//div[@class='jw-media jw-reset']//video[@class='jw-video jw-reset']")
    # actions = ActionChains(driver)
    # actions.move_to_element(video).perform()
    # assert video.is_displayed(), "Video section is present for HP Digital"
    # video.load()
    # print("video load")
    # video.pause()
    # print("video pause")
    # time.sleep(2)
    # video.play()
    # print("video play")


def verify_articles():
    print("inside function verify articles")
    header = driver.find_element(By.XPATH, "//h2[normalize-space()='Articles']")
    actions = ActionChains(driver)
    actions.move_to_element(header).perform()
    assert header.is_displayed(), "Header Articles is displayed"
    temp_number = driver.find_elements(By.XPATH, "//div[@class='hp__articles__row d-grid']/div")
    print(len(temp_number))
    count = 0
    while count < len(temp_number):
        time.sleep(2)
        print("while count", count)
        img_str = "(//div[@class='hp-article-card__image-container " \
                  "image-wrapper image-wrapper--4x3']/img)["+str(count+1)+"]"
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
          (By.XPATH, img_str)))
        img = driver.find_element(
          By.XPATH,
          img_str)
        actions = ActionChains(driver)
        actions.move_to_element(img).perform()
        title = img.get_attribute("title")
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("for article having story :"+title+": Image displayed.")
        else:
            print("for article having story :"+title+": Image not displayed.")
            assert image_present, "article story image not displayed for " + title
        title_shown = driver.find_element(
          By.XPATH,
          "(//div[@class='hp-article-card__title-container']/a)["+str(count+1)+"]")
        actions = ActionChains(driver)
        actions.move_to_element(title_shown).perform()
        assert title_shown.is_displayed(), "Title is not shown for article" + title
        description = driver.find_element(
          By.XPATH,
          "(//p[@class='hp-article-card__excerpt d-none d-desktop-block']/span/p)["+str(count+1)+"]")
        actions = ActionChains(driver)
        actions.move_to_element(description).perform()
        assert description.is_displayed(), "description is not shown for article" + title
        title_shown.click()
        WebDriverWait(driver, 40).until(ec.title_is(title + " - Blavity News"))
        print("Current window title for blavity story: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = str(title)
        print("deduced string is :", temp[0])
        print("text string is :", title)
        assert compare_1 == compare_2, "for page " + title + ", title text does not match"
        driver.back()
        count += 1


def verify_featured_articles():
    print("function called verify_featured_articles")
    header_str = "(//p[@class='hp-featured-article-card-desktop__tag text-uppercase']" \
                 "[normalize-space()='Featured Article'])[1]"
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
      (By.XPATH, header_str)))
    header = driver.find_element(
      By.XPATH,
      header_str)
    actions = ActionChains(driver)
    actions.move_to_element(header).perform()
    assert header.is_displayed(), "Featured Article Header is not displayed"
    temp_number = driver.find_elements(
      By.XPATH,
      "//a[@class='article-link hp-featured-article-card-desktop__title text-uppercase']")
    print(len(temp_number))
    count = 0
    while count < len(temp_number):
        time.sleep(2)
        print("while count", count)
        img_str = "(//div[@class='slick-list draggable']//div[1]//div["+str(count+1)+"]//div[1]//div[1]//div[1]/img)[1]"
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
          (By.XPATH, img_str)))
        img = driver.find_element(
          By.XPATH,
          img_str)
        driver.execute_script("arguments[0].scrollIntoView();", img)
        # actions = ActionChains(driver)
        # actions.move_to_element(img).perform()
        title = img.get_attribute("title")
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("for article having story :" + title + ": Image displayed.")
        else:
            print("for article having story :" + title + ": Image not displayed.")
            assert image_present, "article story image not displayed for " + title
        article_header = driver.find_element(
          By.XPATH,
          "(//a[@class='article-link hp-featured-article-card-desktop__title text-uppercase'])["+str(count+1)+"]")
        assert article_header.is_displayed(), "Article Header is not displayed"
        print("article_header ", article_header.text)
        desc = driver.find_element(
          By.XPATH,
          "(//div[@class='hp-featured-article-card-desktop']/p[2]/span/p)["+str(count+1)+"]")
        print("desc ", desc.text)
        assert desc.is_displayed(), "Article desc is not displayed"
        article_header.click()
        WebDriverWait(driver, 40).until(ec.title_is(title + " - Blavity News"))
        print("Current window title for blavity story: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = str(title)
        print("deduced string is :", temp[0])
        print("text string is :", title)
        assert compare_1 == compare_2, "for page " + title + ", title text does not match"
        driver.back()
        WebDriverWait(driver, 40).until(ec.title_is("Blavity | HP - Blavity News"))
        if count == 1:
            break
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
          (By.XPATH, "(//button[@aria-label='Next'][normalize-space()='Next'])[2]")))
        next_slide = driver.find_element(By.XPATH, "(//button[@aria-label='Next'][normalize-space()='Next'])[2]")
        actions = ActionChains(driver)
        actions.move_to_element(next_slide).perform()
        next_slide.click()
        count += 1


def verify_blavity_hp_page():
    page = driver.find_element(By.XPATH, "//a[normalize-space()='Blavity x HP']")
    assert page.is_displayed(), "the tab Blavity x HP is present"
    page.click()
    WebDriverWait(driver, 30).until(ec.title_is("Blavity | HP - Blavity News"))
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
      (By.XPATH, "//img[@title='Blavity News']")))
    time.sleep(5)
    verify_nav_bar_blavity_hp()
    # time.sleep()
    # verify_adv()
    verify_hero_card()
    verify_blavity_hp_digital()
    verify_articles()
    verify_featured_articles()


# environment()
# page_load()
# post_page_load_pop_up()
# verify_blavity_hp_page()
