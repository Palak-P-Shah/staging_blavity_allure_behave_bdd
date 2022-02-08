from environment import *


def verify_presence_of_element_in_page():
    verify_blavity_news_at_top()


def verify_if_ticker_exists():
    ticker = driver.find_element(By.XPATH, "//div[@class='story-ticker__wrapper d-flex align-items-center']")
    assert ticker.is_displayed(), "ticker is not present"
    assert (ticker.text != "") and (ticker.text is not None), "ticker text is not present"
    # print("text :", ticker.text)
    if (ticker.text != "") and (ticker.text is not None):
        print("Ticker Exists")
        # assert_equal(True, True, "ticker section is present")


def ticker_text_values(ticker_items):
    items = []
    count_test = 0
    while count_test < len(ticker_items):
        print("count test is: ", count_test)
        temp_test_temp = ticker_items[count_test].text
        items.append(temp_test_temp)
        print("txt test is : ", temp_test_temp)
        count_test += 1
        # time.sleep(1)
    print("test array", items)
    print("number of items in array", len(items))
    # element = ""
    # var1 = ""
    # if element in items:
    #   print("empty string position is : ", items.index(element))
    #   var1 = items.index(element)
    time.sleep(1)
    return items


def verify_ticker_count_and_links():
    ticker_items = driver.find_elements(By.CLASS_NAME, "story-ticker-item")
    deduced_array_items = ticker_text_values(ticker_items)
    element = ""
    # var1 = ""
    if element in deduced_array_items:
        print("after iteration array has empty string")
        while element in deduced_array_items:
            deduced_array_items = ticker_text_values(ticker_items)
            if "" not in deduced_array_items:
                break
            var1 = deduced_array_items.index(element)
            print("value is missing at position", var1)
            # time.sleep(2)
    else:
        print("array has no empty string")
    # ticker_text_values(ticker_items)
    print("finally array is, ", deduced_array_items)
    print("count :- ", len(ticker_items))
    assert len(ticker_items) > 0, "ticker items are not present in the ticker"
    # number = len(ticker_items)
    # ticker_text_values(ticker_items)
    time.sleep(1)
    count = 0
    while count < len(ticker_items):
        # time.sleep(1)
        print("count: ", count)
        time.sleep(1)
        temp_test_temp = deduced_array_items[count]
        time.sleep(1)
        print("txt is : ", temp_test_temp)
        print("required link : ", ticker_items[count].get_attribute('href'))
        new_url = ticker_items[count].get_attribute('href')
        # open a new tab
        print("opening a new tab")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
        driver.execute_script("window.open('','_blank');")
        print("opened a new tab")
        # switch command to the new tab being opened.
        driver.switch_to.window(driver.window_handles[1])
        # open the url in new tab
        driver.get(new_url)
        # driver.execute_script("window.open("+b[z].get_attribute('href')+");")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = str(temp_test_temp)
        print("deduced string is :", temp[0])
        print("text string is :", temp_test_temp)
        assert compare_1 == compare_2, "for ticker links, for one of the links , title text does not match"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        count += 1
        time.sleep(1)
    print("All the ticker links do work as expected")


def verify_carousel_read_more_arrows():
    verify_presence_of_element_in_page()
    print("inside function carousel read more and arrows verification")
    number_of_entries = driver.find_elements(By.CLASS_NAME, "home-hero-card__title-wrapper")
    assert len(number_of_entries) > 0, "articles are not present in carousel"
    print("number of entries in Carousel are :- ", len(number_of_entries))
    left_click_button = driver.find_element(By.XPATH, "//button[@id='home-hero-slick-arrow-prev']")
    assert left_click_button.is_displayed(), "left click arrow button is not displayed in carousel"
    right_click_button = driver.find_element(
        By.XPATH, "//button[@id='home-hero-slick-arrow-next']")
    assert right_click_button.is_displayed(), "right click arrow button is not displayed in carousel"
    if left_click_button.is_displayed() and right_click_button.is_displayed():
        print("both right and left click buttons are displayed on this page")
    count = 0
    while count < len(number_of_entries):
        # xpath for author (//div[@class='home-hero-card__author d-flex align-items-center']/a[2])[6]
        # xpath for img (//div[@class='home-hero-card__image-container']/img)[6]
        # xpath for category (//div[@class='home-hero-card__categories d-flex flex-wrap'])[6]
        # xpath for desc (//p[@class='home-hero-card__excerpt d-none d-desktop-block']//span[1]//p)[6]
        # xpath for article (//div[@class='home-hero-card__title-wrapper']/a)[6]
        # xpath for read more (//div[@class='d-none d-desktop-block']/a)[6]
        temp_string = str(count+1)
        temp_str_author = "(//div[@class='home-hero-card__author d-flex align-items-center']/a[2])["+temp_string+"]"
        temp_str_img = "(//div[@class='home-hero-card__image-container']/img)["+temp_string+"]"
        temp_str_category = "(//div[@class='home-hero-card__categories d-flex flex-wrap'])["+temp_string+"]"
        temp_str_desc = "(//p[@class='home-hero-card__excerpt d-none d-desktop-block']//span[1]//p)["+temp_string+"]"
        # temp_str_read_more = "(//div[@class='d-none d-desktop-block']/a)["+temp_string+"]]"
        temp_xpath = "(//div[@class='d-none d-desktop-block']/a)["+temp_string+"]"
        temp_xpath_article_heading = "(//div[@class='home-hero-card__title-wrapper']/a)["+temp_string+"]"
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, temp_xpath_article_heading)))
        # actions = ActionChains(driver)
        article_heading = driver.find_element(By.XPATH, temp_xpath_article_heading)
        assert article_heading.is_displayed(), "article heading is not displayed in carousel"
        article = str(article_heading.text)
        print("article is :", article)

        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH,
          temp_str_img)))
        img = driver.find_element(
          By.XPATH,
          temp_str_img)
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for top stories section for article " + article
        temp_author = driver.find_element(
          By.XPATH,
          temp_str_author)
        print("author :", temp_author.text)
        assert temp_author.text is not None and temp_author.text != "", \
            "Author is not present in carousel for article as " + article
        temp_category = driver.find_element(
          By.XPATH,
          temp_str_category)
        print("category :", temp_category.text)
        assert temp_category.text is not None and \
               temp_category.text != "", "Category is not present for : " + article + \
                                         " in carousel."
        temp_desc = driver.find_element(
          By.XPATH,
          temp_str_desc)
        print("description :", temp_desc.text)
        assert temp_desc.text is not None and \
               temp_desc.text != "", "Description is not present for : " + article + " in carousel."
        read_more_button = driver.find_element(By.XPATH, temp_xpath)
        assert read_more_button.is_displayed(), "read more button for particular article is missing"
        if read_more_button.is_displayed():
            driver.execute_script("arguments[0].click();", read_more_button)
            print("clicked on read more button")
            WebDriverWait(driver, 40).until(ec.title_is(article+" - Blavity News"))
            print("Current window title: " + driver.title)
            temp_str = driver.title
            temp = temp_str.split(' -')
            compare_1 = str(temp[0])
            compare_2 = article
            print("deduced string is :", compare_1)
            print("text string is :", compare_2)
            assert compare_1 == compare_2, "for Carousel links, having link "+article+" , title text does not match"
            driver.execute_script("window.history.go(-1)")
            WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
            temp = 0
            while temp < (count + 1):
                if count == 5:
                    break
                right_arrow = driver.find_element(By.XPATH, "//button[@id='home-hero-slick-arrow-next']")
                right_arrow.click()
                time.sleep(1)
                temp += 1
                print("clicked the right icon number of times :- ", temp)
            count += 1
    print("All the Read More Links are working as expected along with left and right click arrow buttons in Carousel")


def verify_side_bar_top_stories():
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
        By.CSS_SELECTOR,
        ".home-top-stories.page-home__top-stories.flex-full")))
    print("Within the function call top stories")
    b = driver.find_element(By.CSS_SELECTOR, ".home-top-stories.page-home__top-stories.flex-full")
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH,
      "//div[@class='home-top-story-card d-grid']")))
    inner_class = driver.find_elements(By.XPATH, "//div[@class='home-top-story-card d-grid']")
    assert len(inner_class) > 0, "stories are not present for side bar top stories"
    print("number of instances under the top stories section are :", len(inner_class))
    number = len(inner_class)
    count = 0
    while count < number:
        temp_string = str(count + 1)
        temp_xpath = "(//a[@class='article-link home-top-story-card__title'])["+temp_string+"]"
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH,
          temp_xpath)))
        b = driver.find_element(By.XPATH, temp_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(b).perform()
        assert b.is_displayed(), "particular side bar top story is not present"
        print("top story article is : ", b.text)
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH,
          "(//div[@class='image-wrapper image-wrapper--1x1']/img)["+temp_string+"]")))
        img = driver.find_element(
          By.XPATH,
          "(//div[@class='image-wrapper image-wrapper--1x1']//img[1])["+temp_string+"]")
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for top stories section for article " + b.text
        temp_author = driver.find_element(
          By.XPATH,
          "(//p[@class='home-top-story-card__author']/a)["+temp_string+"]")
        print("author :", temp_author.text)
        assert temp_author.text is not None and temp_author.text != "",\
            "Author is not present for top stories section having article as " + b.text
        b.click()
        compare_1 = str(b.text)
        WebDriverWait(driver, 40).until(ec.title_is(b.text+" - Blavity News"))
        print("Current top story window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_2 = str(temp[0])
        assert compare_1 == compare_2, "for side bar top stories, for this particular article :" \
                                       + driver.title + " :story, the text does not match"
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        driver.back()
        WebDriverWait(driver, 20).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
        count += 1
        time.sleep(1)
    print("All the Side bar Top Stories links do work as expected")


def verify_load_more_stories_home_page():
    print("inside function load more stories")
    b = driver.find_element(By.XPATH, "//button[normalize-space()='Load more stories']")
    assert b.is_displayed(), "load more stories button is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    if b.is_displayed():
        print("the Load More Stories button is there")
        temp_count = driver.find_elements(
          By.XPATH,
          "//a[@class='article-link home-sec-article-card__title text-white']")
        print("count before click", len(temp_count))
        assert len(temp_count) > 0, "No Articles are present for this section"
        WebDriverWait(driver, 40).until(
            ec.presence_of_element_located((By.XPATH, "//button[normalize-space()='Load more stories']")))
        count = 0
        print("now iterating stories")
        while count < len(temp_count):
            temp_string = str(count + 1)
            temp_xpath = "(//a[@class='article-link home-sec-article-card__title text-white'])["+temp_string+"]"
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((
                By.XPATH, temp_xpath)))
            temp_element_story = driver.find_element(By.XPATH, temp_xpath)
            temp_test = temp_element_story.text
            print("article is :", temp_test)

            WebDriverWait(driver, 40).until(ec.presence_of_element_located((
              By.XPATH,
              "//div[@class='page-home__second__articles d-none d-desktop-grid flex-full']"
              "//div["+temp_string+"]//div[1]//img")))
            img = driver.find_element(
              By.XPATH,
              "//div[@class='page-home__second__articles d-none d-desktop-grid flex-full']"
              "//div["+temp_string+"]//div[1]//img")
            image_present = driver.execute_script(
              "return arguments[0].complete && typeof arguments[0].naturalWidth "
              "!= \"undefined\" && arguments[0].naturalWidth > 0",
              img)
            if image_present:
                print("Image displayed.")
            else:
                print("Image not displayed.")
                assert image_present, "image is not displayed for top stories section for article " + temp_test
            temp_category = driver.find_element(
              By.XPATH,
              "//div[@class='page-home__second__articles d-none d-desktop-grid flex-full']"
              "//div["+temp_string+"]//div[2]//div[1]")
            print("category :", temp_category.text)
            assert temp_category.text is not None and \
                   temp_category.text != "", "Category is not present for : " + temp_test + \
                                             " article in top stories section."

            actions = ActionChains(driver)
            actions.move_to_element(temp_element_story).perform()
            print("loaded story required link : ", temp_element_story.get_attribute('href'))
            loaded_story_link_url = temp_element_story.get_attribute('href')
            assert loaded_story_link_url is not None and loaded_story_link_url != "", "" \
                "Under load more stories the story link is not present"
            if (loaded_story_link_url is None) or (loaded_story_link_url == ""):
                print("particular top story link is not there")
            driver.get(loaded_story_link_url)
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
            print("Current window title for loaded story: " + driver.title)
            temp_str = driver.title
            temp = temp_str.split(' -')
            compare_1 = str(temp[0])
            compare_2 = str(temp_test)
            assert compare_1 == compare_2, "for stories, for one of the links , title text does not match"
            print("deduced string is :", temp[0])
            print("text string is :", temp_test)
            driver.back()
            WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
            driver.switch_to.window(driver.window_handles[0])
            count += 1
        load_more_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Load more stories']")
        actions = ActionChains(driver)
        actions.move_to_element(load_more_btn).perform()
        temp_count = driver.find_elements(
          By.XPATH,
          "//a[@class='article-link home-sec-article-card__title text-white']")
        print("count before click :", len(temp_count))
        driver.execute_script("arguments[0].click();", load_more_btn)
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH,
          "//button[normalize-space()='Load more stories']")))
        temp_count_after = driver.find_elements(
          By.XPATH,
          "//a[@class='article-link home-sec-article-card__title text-white']")
        assert len(temp_count_after) > len(temp_count), "No Articles are appended after clicking load more stories"
        print("count after click :", len(temp_count_after))
    print("this section do work as expected for 3 articles")


def verify_subscribe_banner_section():
    print("inside function subscribe_banner_section")
    b = driver.find_element(By.XPATH, "//h4[contains(text(),'Want a daily dose of Blavity News?')]")
    assert b.is_displayed(), "subscribe banner text is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    if b.is_displayed():
        print("the subscribe_banner_section is there")
        email_field = driver.find_element(By.XPATH, "//input[@class='bg-red border-0 text-white w-100']")
        assert email_field.is_displayed(), "email field is not displayed under subscribe banner section"
        email_field.send_keys("fortestpurposesonly5@gmail.com")
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[value='submit']")
        assert submit_button.is_displayed(), "submit button is not displayed under subscribe banner section"
        # actions = ActionChains(driver)
        actions.move_to_element(submit_button).perform()
        driver.execute_script("arguments[0].click();", submit_button)
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
            By.XPATH, "//p[contains(text(),'Welcome to the family!')]")))
        after_click = driver.find_element(By.XPATH, "//p[contains(text(),'Welcome to the family!')]")
        assert after_click.is_displayed(), \
            "after clicking submit, the text is not displayed under subscribe banner section"
        if ec.visibility_of_element_located(after_click):
            print("submit button works as expected")


def verify_lunchtable_section():
    # this function verifies if the lunchtable logo exists, checkout more link works and the video exists
    print("inside function call lunchtable section")
    b = driver.find_element(By.XPATH, "//div[@class='home-lunchtable position-relative text-center text-desktop-left']")
    assert b.is_displayed(), "lunchtable section is not displayed"
    if b.is_displayed():
        print("lunchtable section is there")
        link_lunchtable_webelement = driver.find_element(
            By.XPATH, "//a[@class='btn btn-outline-primary d-none d-desktop-inline-block text-bold text-uppercase']")
        actions = ActionChains(driver)
        actions.move_to_element(link_lunchtable_webelement).perform()
        print("lunchtable link : ", link_lunchtable_webelement.get_attribute('href'))
        link_lunchtable = link_lunchtable_webelement.get_attribute('href')
        assert link_lunchtable is not None and link_lunchtable != "", "lunchtable link is not present"
        if (link_lunchtable is None) or (link_lunchtable == ""):
            print("lunchtable link is not there")
        # open a new tab
        print("opening a new tab")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 't')
        driver.execute_script("window.open('','_blank');")
        print("opened a new tab")
        # switch command to the new tab being opened.
        driver.switch_to.window(driver.window_handles[1])
        # open the url present in carousel link in a new tab
        driver.get(link_lunchtable)
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        print("Current window title for lunchtable is: " + driver.title)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        # check for the video section
        video_path = driver.find_element(By.XPATH, "//video[@class='jw-video jw-reset']")
        assert video_path.is_displayed(), "video is not present for lunchtable section"
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, ".jwplayer.image-wrapper.image-wrapper--16x9.home-lunchtable__player")))
        print("video is present")


def verify_blavity_originals_section():
    # this function verifies if all the 8 links in the section works fine
    print("in the function blavity originals section ")
    b = driver.find_element(By.XPATH, "//h3[normalize-space()='Blavity Originals']")
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    tmp_count = driver.find_elements(
      By.XPATH,
      "//div[@class='home-original-slider__slick slick-initialized slick-slider']/div[1]/div[1]/div")
    assert b.is_displayed(), "text heading is present for blavity originals"
    if b.is_displayed():
        print("blavity originals section is there")
        count = 0
        while count < len(tmp_count):
            temp_str = str(count + 1)
            temp_xpath = "(//div[@class='home-original-card__content-body flex-full']//div[1]/a)["+temp_str+"]"
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, temp_xpath)))
            b = driver.find_element(By.XPATH, temp_xpath)
            actions = ActionChains(driver)
            actions.move_to_element(b).perform()
            print("loaded link of blavity originals : ", b.get_attribute('href'))
            blavity_original_link_url = b.get_attribute('href')
            temp_var = b.text
            print("Article is :", temp_var)
            assert blavity_original_link_url is not None and blavity_original_link_url != "", \
                "particular blavity originals article link is present"
            if (blavity_original_link_url is None) or (blavity_original_link_url == ""):
                print("particular blavity original link is not there")
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((
              By.XPATH,
              "(//div[@class='home-original-card position-relative']//div[1]/img)["+temp_str+"]")))
            img = driver.find_element(
              By.XPATH,
              "(//div[@class='home-original-card position-relative']//div[1]/img)["+temp_str+"]")
            image_present = driver.execute_script(
              "return arguments[0].complete && typeof arguments[0].naturalWidth "
              "!= \"undefined\" && arguments[0].naturalWidth > 0",
              img)
            if image_present:
                print("Image displayed.")
            else:
                print("Image not displayed.")
                assert image_present, "image is not displayed for blavity originals section for article " + temp_var
            temp_category = driver.find_element(
              By.XPATH,
              "(//div[@class='home-original-card__categories d-flex "
              "flex-wrap text-bold text-uppercase'])["+temp_str+"]")
            print("category :", temp_category.text)
            assert temp_category.text is not None and \
                   temp_category.text != "", "Category is not present for : " + temp_var + \
                                             " article in 'blavity originals' section."
            temp_author = driver.find_element(
              By.XPATH,
              "(//a[@class='author-link home-original-card__author-name'])["+temp_str+"]")
            print("author :", temp_author.text)
            assert temp_author.text is not None and \
                   temp_author.text != "", "Author is not present for : "\
                                           + temp_var + " article in 'blavity originals' section."
            b.click()
            WebDriverWait(driver, 40).until(ec.title_is(temp_var + " - Blavity News"))
            print("Current window title for opinion ed is : " + driver.title)
            temp_str = driver.title
            temp = temp_str.split(' -')
            compare_1 = str(temp[0])
            compare_2 = temp_var
            assert compare_1 == compare_2, "for a particular story of blavity original section:" \
                                           + temp_var + ", title text does not match"
            print("deduced string is :", compare_1)
            print("text string is :", compare_2)
            driver.back()
            WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
            count += 1
        print("all the links of blavity originals section are working correctly")


def verify_page_op_ed_section():
    # this function verifies if the Op_ed section is visible on the page,
    # and verifies if all the 6 links within this section works
    print("in the function page op ed section")
    b = driver.find_element(
        By.XPATH, "//a[@class='text-bold text-uppercase d-flex align-items-center justify-content-center']")
    assert b.is_displayed(), "Page Opinion Section is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(b).perform()
    if b.is_displayed():
        print("the op ed section is displayed")
        print("link to blavity's op ed section : ", b.get_attribute('href'))
        driver.execute_script("arguments[0].click();", b)
        print("Current Page title: " + driver.title)
        # see whether login page is presented or not.
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Login']")))
        # back to previous page with back()
        driver.back()

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((
            By.XPATH, "//button[normalize-space()='Read more op-eds']")))
        # time.sleep(2)
        # number of articles before and after clicking read more oped's xpath
        # //div[@class='page-home__op-ed__articles d-grid']/div
        print("Current Page title after back: " + driver.title)
        # time.sleep(3)
        temp_number = driver.find_elements(By.XPATH, "//div[@class='page-home__op-ed__articles d-grid']/div")
        print("number of articles before click ", len(temp_number))
        count = 6
        while count < 12:
            temp_string = str(count + 1)
            temp_xpath = "(//div[@class='home-op-ed-card__title-container flex-full']/a)["+temp_string+"]"
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, temp_xpath)))
            # 7 to 12 total 6
            # article link as and title for comparison from
            # (//div[@class='home-op-ed-card__title-container flex-full']/a)[7]
            # category xpath (//div[@class='home-op-ed-card d-flex flex-column']//div[2]//div[1])[7]
            # author xpath (//div[@class='home-op-ed-card__author d-flex align-items-center']/a)[7]
            # img xpath (//div[@class='home-op-ed-card d-flex flex-column']//div[1]//img[1])[7]
            b = driver.find_element(By.XPATH, temp_xpath)
            temp_var = str(b.text)
            WebDriverWait(driver, 40).until(ec.presence_of_element_located((
              By.XPATH,
              "(//div[@class='home-op-ed-card d-flex flex-column']//div[1]//img[1])["+temp_string+"]")))
            img = driver.find_element(
              By.XPATH,
              "(//div[@class='home-op-ed-card d-flex flex-column']//div[1]//img[1])["+temp_string+"]")
            image_present = driver.execute_script(
              "return arguments[0].complete && typeof arguments[0].naturalWidth "
              "!= \"undefined\" && arguments[0].naturalWidth > 0",
              img)
            if image_present:
                print("Image displayed.")
            else:
                print("Image not displayed.")
                assert image_present, "image is not displayed for oped section for article " + temp_var
            temp_category = driver.find_element(
              By.XPATH,
              "(//div[@class='home-op-ed-card d-flex flex-column']//div[2]//div[1])["+temp_string+"]")
            print("category :", temp_category.text)
            assert temp_category.text is not None and \
                   temp_category.text != "", "Category is not present for : " + temp_var + \
                                             " article in 'op ed' section."
            temp_author = driver.find_element(
              By.XPATH,
              "(//div[@class='home-op-ed-card__author d-flex align-items-center']/a)["+temp_string+"]")
            print("author :", temp_author.text)
            assert temp_author.text is not None and \
                   temp_author.text != "", "author is not present for : " + temp_var + " article in 'op ed' section."
            actions = ActionChains(driver)
            actions.move_to_element(b).perform()
            print("loaded link of op ed : ", b.get_attribute('href'))
            op_ed_original_link_url = b.get_attribute('href')
            assert (op_ed_original_link_url is not None) and (op_ed_original_link_url != ""),\
                "opinion ed article url is not present"
            if (op_ed_original_link_url is None) or (op_ed_original_link_url == ""):
                print("particular op ed link is not there")
            b.click()
            WebDriverWait(driver, 40).until(ec.title_is(temp_var+" - Blavity News"))
            print("Current window title for opinion ed is : " + driver.title)
            temp_str = driver.title
            temp = temp_str.split(' -')
            compare_1 = str(temp[0])
            compare_2 = temp_var
            assert compare_1 == compare_2, "for a particular story of opinon ed's sections"\
                                           + temp_var + ", title text does not match"
            print("deduced string is :", compare_1)
            print("text string is :", compare_2)
            driver.back()
            WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
            count += 1
        print("all the links in op ed are working as expected")
        from_other_sites = driver.find_element(By.XPATH, "//h2[normalize-space()='From Our Other Sites']")
        actions = ActionChains(driver)
        actions.move_to_element(from_other_sites).perform()
        more_op_ed_button = driver.find_element(By.XPATH, "//button[contains(text(),'Read more op-eds')]")
        driver.execute_script("arguments[0].click();", more_op_ed_button)
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH,
          "//button[contains(text(),'Read more op-eds')]")))
        temp_number_after_click = driver.find_elements(
          By.XPATH,
          "//div[@class='page-home__op-ed__articles d-grid']/div")
        print("number of articles after click ", len(temp_number_after_click))
        print("Read more op-eds button is working as expected")


def verify_from_our_other_sites():
    print("in function from our other sites")
    from_other_sites = driver.find_element(By.XPATH, "//h2[normalize-space()='From Our Other Sites']")
    assert from_other_sites.is_displayed(), "from our other sites section is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(from_other_sites).perform()
    number_of_ele = driver.find_elements(By.CLASS_NAME, "home-oo-card__site-name")
    assert len(number_of_ele) > 0, "articles are not there in from our other sites section."
    count = 0
    while count < len(number_of_ele):
        temp_string = "(//div[@class='home-oo-card__title-container flex-full']/a)["+str(count+1)+"]"
        temp_ele = driver.find_element(By.XPATH, temp_string)
        actions = ActionChains(driver)
        actions.move_to_element(temp_ele).perform()
        assert temp_ele.is_displayed(), "particular article is not displayed of from our other sites section"
        compare_var = str(temp_ele.text)
        parent_site = driver.find_element(By.XPATH, "(//div[@class='home-oo-card__site-name']/a)["+str(count+1)+"]")
        assert parent_site.text is not None and \
               parent_site.text != "", "parent site is not present for : "\
                                       + compare_var + " article in 'op ed' section."
        print("site is :", parent_site.text)
        header_str = compare_var
        print("made title :", header_str)
        print("loaded link of other sites : ", temp_ele.get_attribute('href'))
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH,
          "(//div[@class='home-oo-card d-flex flex-column']//div[1]/img)["+str(count+1)+"]")))
        img = driver.find_element(
          By.XPATH,
          "(//div[@class='home-oo-card d-flex flex-column']//div[1]/img)["+str(count+1)+"]")
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          img)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for from our other sites for article " + header_str
        blavity_other_link_url = temp_ele.get_attribute('href')
        assert blavity_other_link_url is not None and blavity_other_link_url != "", \
            "article link is not there for particular blavity other link url"
        if (blavity_other_link_url is None) or (blavity_other_link_url == ""):
            print("particular other site link is not there")
        driver.execute_script("arguments[0].click();", temp_ele)
        print("clicked on article heading")
        # switch to the new tab being opened.
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 40).until(ec.title_contains(header_str))
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        print("Current window title for from our other links: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = compare_var
        assert compare_1 == compare_2, "for a particular story from our other sites, title text does not match"
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        count += 1


def verify_blavity_news_at_top():
    print("function called to verify_blavity_news_at_top")
    blavity_logo = driver.find_element(By.XPATH, "(//img[@class='img img-fluid'])[1]")
    assert blavity_logo.is_displayed(), "Blavity:News image is not present"
    blavity_logo.click()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_blavity_footer():
    print("function called to check blavity footer")
    blavity_img = driver.find_element(By.XPATH, "//img[@class='app-footer__logo']")
    assert blavity_img.is_displayed(), "Blavity:News image is not displayed within footer"
    image_present = driver.execute_script(
      "return arguments[0].complete && typeof arguments[0].naturalWidth "
      "!= \"undefined\" && arguments[0].naturalWidth > 0",
      blavity_img)
    if image_present:
        print("Image displayed.")
    else:
        print("Image not displayed.")
        assert image_present, "image is not displayed of BLAVITY:NEWS in footer"
    all_rights_reserved = driver.find_element(
        By.XPATH, "//p[contains(text(),'© 2021 Blavity, Inc. All rights reserved.')]")
    assert all_rights_reserved.is_displayed(), "under footer all rights reserved text is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(all_rights_reserved).perform()
    # image = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/footer[1]/div[1]/img[1]")
    if all_rights_reserved.is_displayed():
        print("footer blavity image is present")
        fb_blavity = driver.find_element(By.XPATH, "//a[@href='https://www.facebook.com/Blavity']")
        assert fb_blavity.is_displayed(), "facebook link is not displayed under footer"
        actions.move_to_element(all_rights_reserved).perform()
        if fb_blavity.is_displayed():
            print("footer facebook image is present")
            fb_blavity = driver.find_element(By.XPATH, "//a[@href='https://www.facebook.com/Blavity']")
            fb_blavity.click()
            verify_blavity_footer_facebook()
        twitter_blavity = driver.find_element(
          By.XPATH,
          "(//*[name()='svg'][@class='icon icon--twitter'])[3]")
        assert twitter_blavity.is_displayed(), "twitter link is not displayed under footer"
        if twitter_blavity.is_displayed():
            print("footer tweeter image is present")
            twitter_blavity.click()
            verify_blavity_footer_twitter()
        instag_blavity = driver.find_element(By.XPATH, "//a[@href='https://www.instagram.com/blavity']")
        assert instag_blavity.is_displayed(), "instagram link is not displayed under footer"
        if instag_blavity.is_displayed():
            print("footer instagram image is present")
            instag_blavity.click()
            verify_blavity_footer_instagram()
        if all_rights_reserved.is_displayed():
            print("All rights reserved condition is there")
        link_careers = driver.find_element(By.XPATH, "//a[@class='text-bold'][normalize-space()='Careers']")
        assert link_careers.is_displayed(), "careers link is not displayed under footer"
        if link_careers.is_displayed():
            print("Careers link is displayed")
            link_careers.click()
            open_new_tab_and_verify()
            print("footer career's link is active")
        link_terms = driver.find_element(By.XPATH, "//a[normalize-space()='Terms']")
        assert link_terms.is_displayed(), "terms link is not displayed under footer"
        if link_terms.is_displayed():
            print("terms link is displayed")
            link_terms.click()
            # switch to the new tab being opened.
            open_new_tab_and_verify()
            print("footer terms link is active")
        link_privacy = driver.find_element(By.XPATH, "//a[normalize-space()='Privacy']")
        assert link_privacy.is_displayed(), "privacy link is not displayed under footer"
        if link_privacy.is_displayed():
            print("privacy link is displayed")
            actions.move_to_element(all_rights_reserved).perform()
            link_privacy.click()
            # switch to the new tab being opened.
            open_new_tab_and_verify()
            print("footer privacy link is active")
        link_adv = driver.find_element(By.XPATH, "//a[normalize-space()='Advertise']")
        assert link_adv.is_displayed(), "Advertise link is not displayed under footer"
        if link_adv.is_displayed():
            print("Advertise link is displayed")
            actions.move_to_element(all_rights_reserved).perform()
            link_adv.click()
            # switch to the new tab being opened.
            open_new_tab_and_verify()
            print("footer advertise link is active")
        link_media = driver.find_element(By.XPATH, "//a[contains(text(),'Media Passes')]")
        assert link_media.is_displayed(), "Media link is not displayed under footer"
        if link_media.is_displayed():
            print("Media Passes link is displayed")
            actions.move_to_element(all_rights_reserved).perform()
            link_media.click()
            # switch to the new tab being opened.
            verify_blavity_footer_link_media()
        #   as "privacy preferences" link is removed , from footer, thus this code is commented.
        # link_prefer = driver.find_element(By.XPATH, "//a[contains(text(),'Privacy Preferences')]")
        # assert link_prefer.is_displayed(), "Preferences link is not displayed under footer"
        # if link_prefer.is_displayed():
        #     print("Privacy Preferences link is displayed")
        #     actions.move_to_element(all_rights_reserved).perform()
        #     link_prefer.click()
        #     # switch to the new tab being opened.
        #     verify_blavity_footer_preferences()


def verify_blavity_footer_facebook():
    print("inside function footer facebook link")
    # time.sleep(2)
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert driver.current_url == 'https://www.facebook.com/Blavity', "facebook link in footer is not active"
    if driver.current_url == 'https://www.facebook.com/Blavity':
        print("face book link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_blavity_footer_twitter():
    time.sleep(2)
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert driver.current_url == 'https://twitter.com/blavity', "twitter link in footer is not active"
    if driver.current_url == 'https://twitter.com/blavity':
        print("twitter link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_blavity_footer_instagram():
    time.sleep(2)
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    WebDriverWait(driver, 40).until(ec.title_contains("blavity"))
    assert driver.current_url == 'https://www.instagram.com/blavity/', "instagram link in footer is not active"
    if driver.current_url == 'https://www.instagram.com/blavity/':
        print("instagram link is active")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def open_new_tab_and_verify():
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    assert "Blavity" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def verify_blavity_footer_preferences():
    time.sleep(5)
    driver.switch_to.frame("sp_message_iframe_410351")
    # manage_pre = driver.find_element_by_xpath("//p[normalize-space()='Manage your preferences']")
    WebDriverWait(driver, 40).until(ec.presence_of_element_located(
        (By.XPATH, "//p[normalize-space()='Manage your preferences']")))
    close_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']")
    actions = ActionChains(driver)
    actions.move_to_element(close_btn).perform()
    assert close_btn.is_displayed(), "close button is not displayed for preferences under footer"
    close_btn.click()
    print("footer privacy preferences link is active")


def verify_blavity_footer_link_media():
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_is("Media Credentials Request Form"))
    assert "Media Credentials Request Form" in driver.title
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("footer media passes link is active")


# environment()
# page_load()
# post_page_load_pop_up()
# verify_presence_of_element_in_page()
# verify_if_ticker_exists()
# verify_ticker_count_and_links()
# verify_carousel_read_more_arrows()
# verify_side_bar_top_stories()
# verify_load_more_stories_home_page()
# verify_subscribe_banner_section()
# verify_lunchtable_section()
# verify_blavity_originals_section()
# verify_page_op_ed_section()
# verify_from_our_other_sites()
# verify_blavity_footer()
