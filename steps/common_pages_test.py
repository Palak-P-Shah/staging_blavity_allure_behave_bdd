from environment import *


def verify_load_more_stories(page_value):
    WebDriverWait(driver, 40).until(
      ec.presence_of_element_located((
        By.XPATH,
        "(//button[normalize-space()='load more stories'])[1]")))
    load_more = driver.find_element(By.XPATH, "(//button[normalize-space()='load more stories'])[1]")
    assert load_more.is_displayed(), "load more stories button is not present"
    actions = ActionChains(driver)
    actions.move_to_element(load_more).perform()
    print(page_value)
    if page_value != "Lifestyle":
        number_of_articles = driver.find_elements(
          By.XPATH,
          "//div[@class='page-category__article-card col-desktop-6 article-card article-card--overlapped']")
        print("number of articles are :-", len(number_of_articles))
    else:
        number_of_articles = driver.find_elements(
          By.XPATH,
          "//div[@class='page-category-sub__article-card col-desktop-6 article-card article-card--overlapped']")
        print("number of articles are :-", len(number_of_articles))
    load_more.click()
    time.sleep(2)
    # after the button is clicked, now there are 8 news stories.
    post_click_number = driver.find_elements(By.CLASS_NAME, "category-link-container")
    print("post click", len(post_click_number))
    assert len(post_click_number) > 0, "no articles are present"
    assert len(post_click_number) > len(number_of_articles), "articles are not present for this section"
    # print("", len(number_of_articles))
    # print("After clicking load more stories, number of articles present are: ", len(number_of_articles))


def post_click_load_more_verify_story(page_value):
    if page_value == "Op-Eds":
        page_value = "Opinion"
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//h1[normalize-space()='" + page_value + "']")))
    assert_test = driver.find_element(By.XPATH, "//h1[normalize-space()='" + page_value + "']")
    assert assert_test.is_displayed(), \
        "post click load more , for the sample story header " \
        "is not present of the " + page_value + " page"
    temp_xpath = "(//div[@class='title-container d-flex']//a//span)[5]"
    by_xpath = "(//div[@class='author d-flex align-items-center']//p//a)[5]"
    header_xpath = "(//div[@class='category-link-container'])[5]"
    img_xpath = "(//div[@class='font-0 image-wrapper font-0 image-wrapper--16x9']//img)[5]"
    title_xpath = temp_xpath
    link = driver.find_element(By.XPATH, temp_xpath)
    by = driver.find_element(By.XPATH, by_xpath).text
    header = driver.find_element(By.XPATH, header_xpath).text
    title = driver.find_element(By.XPATH, title_xpath).text
    assert (by is not None) and (by != ""), \
        "after load more click , for the loaded " \
        "articles ,by is not present for the article"
    if (by is not None) and by != "":
        print("By element is present for 5th article loaded after clicking load more stories")
    assert (header is not None) and (
        header != ""), "after load more click , for the loaded articles ,header is not present for the article"
    if (header is not None) and header != "":
        print("NEWS/OPINION/CULTURE element is present for 5th article loaded after clicking load more stories")
    assert (title is not None) or (
      title != ""), "after load more click , for the loaded articles ,title is not present for the article"
    if (title is not None) and title != "":
        print("title element is present for 5th article loaded after clicking load more stories")
    actions = ActionChains(driver)
    actions.move_to_element(link).perform()
    assert link.is_displayed(), "particular blavity " + page_value + " link is not there"
    print("loaded link of blavity " + page_value + " : ", link.get_attribute('href'))
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH,
      img_xpath)))
    img = driver.find_element(
      By.XPATH,
      img_xpath)
    image_present = driver.execute_script(
      "return arguments[0].complete && typeof arguments[0].naturalWidth "
      "!= \"undefined\" && arguments[0].naturalWidth > 0",
      img)
    if image_present:
        print("Image displayed.")
    else:
        print("Image not displayed.")
        assert image_present, "image is not displayed for page :" + page_value + "having article as: " + title
    temp_author = driver.find_element(
      By.XPATH,
      by_xpath)
    print("author :", temp_author.text)
    assert temp_author.text is not None and \
           temp_author.text != "", "author is not present for page :" + page_value + "having article as: " + title
    temp_category = driver.find_element(
      By.XPATH,
      header_xpath)
    print("category :", temp_category.text)
    assert temp_author.text is not None and \
           temp_author.text != "", "category is not present for page :" + page_value + "having article as: " + title
    link.click()
    WebDriverWait(driver, 40).until(ec.title_is(title + " - Blavity News"))
    print("Current window title for blavity story: " + driver.title)
    temp_str = driver.title
    temp = temp_str.split(' -')
    compare_1 = str(temp[0])
    compare_2 = str(title)
    print("deduced string is :", temp[0])
    print("text string is :", title)
    assert compare_1 == compare_2, "for page " + page_value + ", for one of the links , title text does not match"
    driver.back()
    print("After clicking load more button, the article link and page is displayed as expected")


def verify_each_story(page_value):
    count = 0
    # time.sleep(1)
    if page_value == "Lifestyle":
        page_value = "Life Style"
    number_of_articles = driver.find_elements(
      By.XPATH,
      "//div[@class='page-category__article-card col-desktop-6 article-card article-card--overlapped']")
    print("number of articles are :-", len(number_of_articles))
    assert len(number_of_articles) > 0, "articles are not present for the page " + page_value
    while count < len(number_of_articles):
        if page_value == "Op-Eds":
            page_value = "Opinion"
        print(page_value, " is the page")
        WebDriverWait(driver, 40).until(
            ec.presence_of_element_located((By.XPATH, "//h1[normalize-space()='"+page_value+"']")))
        assert_test = driver.find_element(By.XPATH, "//h1[normalize-space()='"+page_value+"']")
        assert assert_test.is_displayed(), "header is not present of the " + page_value + " page"
        temp_string = str(count + 1)
        temp_xpath = "(//div[@class='title-container d-flex']//a//span)["+temp_string+"]"
        by_xpath = "(//div[@class='author d-flex align-items-center']//p//a)["+temp_string+"]"
        header_xpath = "(//div[@class='category-link-container'])["+temp_string+"]"
        img_xpath = "(//div[@class='font-0 image-wrapper font-0 image-wrapper--16x9']//img)["+temp_string+"]"
        title_xpath = temp_xpath
        link = driver.find_element(By.XPATH, temp_xpath)
        title = driver.find_element(By.XPATH, title_xpath).text
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH,
          img_xpath)))
        img = driver.find_element(
          By.XPATH,
          img_xpath)
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for page :" + page_value + "having article as: " + title
        temp_author = driver.find_element(
          By.XPATH,
          by_xpath)
        print("author :", temp_author.text)
        assert temp_author.text is not None and \
               temp_author.text != "", "author is not present for page :" + page_value + "having article as: " + title
        temp_category = driver.find_element(
          By.XPATH,
          header_xpath)
        print("category :", temp_category.text)
        assert temp_author.text is not None and \
               temp_author.text != "", "category is not present for page :" + page_value + "having article as: " + title

        # print("tempString",temp_string)
        by = driver.find_element(By.XPATH, by_xpath).text
        header = driver.find_element(By.XPATH, header_xpath).text
        assert(by is not None) and (by != ""), "by is not present for the article"
        if (by is not None) and by != "":
            print("By element is present for this article")
        assert header is not None and header != "", "header is not present for the article"
        if (header is not None) and header != "":
            print("NEWS/OPINION/CULTURE element is present for this article")
        assert title is not None and title != "", "title is not present for the article"
        if (title is not None) and title != "":
            print("title element is present for this article")
        # print("tempXpath :", temp_xpath)
        # print("link is", link.text)
        actions = ActionChains(driver)
        actions.move_to_element(link).perform()
        link.click()
        WebDriverWait(driver, 40).until(ec.title_is(title + " - Blavity News"))
        print("Current window title for blavity story: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = str(title)
        print("deduced string is :", temp[0])
        print("text string is :", title)
        assert compare_1 == compare_2, "for page "+page_value+", for one of the links , title text does not match"
        driver.back()
        count += 1


def verify_news_page():
    page_value = "News"
    print("page is", page_value)
    time.sleep(2)
    page = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='"+page_value+"']")
    assert page.is_displayed(), "News link is not present in the NavBar"
    page.click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Blavity is a tech company for forward thinking Bla')]")))
    verify_each_story(page_value)
    time.sleep(4)
    verify_load_more_stories(page_value)
    post_click_load_more_verify_story(page_value)
    print("the links of blavity "+page_value+" section are working correctly, including load more button")


def verify_opinion_page():
    page_value = "Op-Eds"
    print("page is", page_value)
    time.sleep(2)
    page = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='"+page_value+"']")
    assert page.is_displayed(), "Opinion link is not present in the NavBar"
    page.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Blavity is a tech company for forward thinking Bla')]")))
    verify_each_story(page_value)
    verify_load_more_stories(page_value)
    post_click_load_more_verify_story(page_value)
    print("the links of blavity "+page_value+" section are working correctly, including load more button")


def verify_life_style_page():
    page_value = "Lifestyle"
    print("page is", page_value)
    time.sleep(2)
    page = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='"+page_value+"']")
    assert page.is_displayed(), "LifeStyle link is not present in the NavBar"
    page.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Tricks and insights to help you build your brand a')]")))
    verify_each_story(page_value)
    verify_load_more_stories(page_value)
    post_click_load_more_verify_story(page_value)
    print("the links of blavity "+page_value+" section are working correctly, including load more button")


def verify_politics_page():
    page_value = "Politics"
    print("page is", page_value)
    time.sleep(2)
    more_link = driver.find_element(By.XPATH, "//span[@class='font-primary']")
    assert more_link.is_displayed(), "more link is not displayed in the Navigation Bar"
    more_link.click()
    print("More link is active")
    more_page_link = driver.find_element(By.XPATH, "//a[normalize-space()='"+page_value+"']")
    assert more_page_link.is_displayed(), "More --> Politics link is not displayed in the Navigation Bar"
    more_page_link.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Blavity is a tech company for forward thinking Bla')]")))
    verify_each_story(page_value)
    verify_load_more_stories(page_value)
    post_click_load_more_verify_story(page_value)
    print("the links of blavity "+page_value+" section are working correctly, including load more button")


def verify_culture_page():
    page_value = "Culture"
    print("page is", page_value)
    time.sleep(2)
    more_link = driver.find_element(By.XPATH, "//span[@class='font-primary']")
    more_link.click()
    assert more_link.is_displayed(), "more link is not displayed in the Navigation Bar"
    print("More link is active")
    time.sleep(2)
    more_page_link = driver.find_element(By.XPATH, "//a[normalize-space()='"+page_value+"']")
    assert more_page_link.is_displayed(), "More --> Culture link is not displayed in the Navigation Bar"
    more_page_link.click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Commentary on culture, happenings, and the things ')]")))
    verify_each_story(page_value)
    verify_load_more_stories(page_value)
    post_click_load_more_verify_story(page_value)
    print("the links of blavity "+page_value+" section are working correctly, including load more button")


# environment()
# page_load()
# post_page_load_pop_up()
# verify_opinion_page()
# verify_news_page()
# verify_life_style_page()
# verify_politics_page()
# verify_culture_page()
# # verify_footer_presence()
# # driver.quit()
