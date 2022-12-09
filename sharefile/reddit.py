import time

import pyautogui

while True:
    print("menu ,01.screenshot 0.cv 1.print position 2.auto reddit-upvotes x.break 3.Traffic Exchange 4.vk j 5. lootv")

    menu = input()
    if menu == "01":
        pyautogui.screenshot('/home/pungon/Documents/sharefile/images/everve/test.png')
        print('screens')
    if menu == "0":

        # start = pyautogui.locateCenterOnScreen('images/pakapon55@gmail.com.png')
        #54Ac
        for x in range(10):
            print(x)
            joingroup = pyautogui.locateCenterOnScreen('images/everve/vk/join-group.png')  # If the file is not a png file it will not work
            pyautogui.moveTo(joingroup)# Moves the mouse to the coordinates of the image
            pyautogui.click(joingroup)
            time.sleep(2)
            joingroup2 = pyautogui.locateCenterOnScreen(
                'images/everve/vk/join-group2.png')  # If the file is not a png file it will not work
            pyautogui.moveTo(joingroup2)  # Moves the mouse to the coordinates of the image
            pyautogui.click(joingroup2)
            time.sleep(10)
            follo = pyautogui.locateCenterOnScreen(
                'images/everve/vk/follo.png')
            pyautogui.moveTo(follo)
            pyautogui.click()
            time.sleep(5)
            joincommunity = pyautogui.locateCenterOnScreen(
                'images/everve/vk/join-community.png')
            pyautogui.moveTo(joincommunity)
            pyautogui.click()
            time.sleep(20)
            pyautogui.click(398, 25)
            time.sleep(7)
            next = pyautogui.locateCenterOnScreen('images/everve/vk/next.png')
            pyautogui.moveTo(next)
            pyautogui.click()
            time.sleep(3)
            report = pyautogui.locateCenterOnScreen('images/everve/vk/report.png')
            pyautogui.moveTo(report)
            pyautogui.click()
            time.sleep(3)


    if menu == "1" :

        time.sleep(2)
        print('position: ',pyautogui.position())

    if menu == "2" :
        time.sleep(5)
        for x in range(100):
            check = 0
            print(x)

            UpvotePost = pyautogui.locateCenterOnScreen(
                'images/everve/reddit/UpvotePost.png',confidence = 0.7)  # If the file is not a png file it will not work
            time.sleep(1)
            print(UpvotePost)
            pyautogui.moveTo(UpvotePost)  # Moves the mouse to the coordinates of the image
            time.sleep(1)
            pyautogui.click(UpvotePost)

            time.sleep(1)

            UpvotePost3 = pyautogui.locateCenterOnScreen(
                'images/everve/reddit/UpvotePost3.png')  # If the file is not a png file it will not work
            pyautogui.moveTo(UpvotePost3)  # Moves the mouse to the coordinates of the image
            pyautogui.click(UpvotePost3)
            print(UpvotePost3)
            time.sleep(1)

            UpvotePost2 = pyautogui.locateCenterOnScreen(
                'images/everve/reddit/UpvotePost2.png')
            pyautogui.moveTo(UpvotePost2)
            pyautogui.click(UpvotePost2)
            print(UpvotePost2)
            time.sleep(1)

            time.sleep(20)

            try:
                a, b = pyautogui.locateCenterOnScreen('images/everve/reddit/checkpass.png',confidence = 0.7)

            except:
                print('checkpass ',pyautogui.locateCenterOnScreen('images/everve/reddit/checkpass.png',confidence = 0.7))
                ClickUp = pyautogui.locateCenterOnScreen(
                    'images/everve/reddit/ClickUp.png',confidence = 0.7)
                # pyautogui.moveTo(ClickUp)
                time.sleep(2)
                pyautogui.click(ClickUp)
                print('Up',ClickUp)
                time.sleep(5)
                # ClickUp3 = pyautogui.locateCenterOnScreen(
                #     'images/everve/reddit/ClickUp3.png', confidence=0.7)
                # # pyautogui.moveTo(ClickUp)
                # time.sleep(2)
                # pyautogui.click(ClickUp3)
                # print('Up', ClickUp3)
                # time.sleep(5)
                # ClickUp2 = pyautogui.locateCenterOnScreen(
                #     'images/everve/reddit/ClickUp2.png',confidence = 0.7)
                # pyautogui.moveTo(ClickUp2)
                # time.sleep(2)
                # pyautogui.click(ClickUp2)
                # print('Up',ClickUp2)

                time.sleep(5)

                pyautogui.click(406, 51)
                time.sleep(15)

                try:
                 a, b = pyautogui.locateCenterOnScreen('images/everve/reddit/report.png', confidence=0.7)
                except:
                 next = pyautogui.locateCenterOnScreen(
                     'images/everve/reddit/next.png',confidence = 0.8)
                 print(next)
                 pyautogui.moveTo(next)
                 time.sleep(2)
                 pyautogui.click(next)
                 time.sleep(5)
                else:
                 report = pyautogui.locateCenterOnScreen(
                    'images/everve/reddit/report.png', confidence=0.7)
                 print('report', report)
                 pyautogui.moveTo(report)
                 time.sleep(2)
                 pyautogui.click(report)
                 time.sleep(5)


                #next = pyautogui.locateCenterOnScreen(
                #    'images/everve/reddit/next.png',confidence = 0.8)
                #print(next)
                #pyautogui.moveTo(next)
                #time.sleep(2)
                #pyautogui.click(next)
                #time.sleep(5)

                #next2 = pyautogui.locateCenterOnScreen('images/everve/reddit/next2.png')
                #pyautogui.moveTo(next2)
                #time.sleep(2)
                #pyautogui.click(next2)
                #time.sleep(5)
                #time.sleep(10)

            else:
                print('ไม่ผ่าน')
                time.sleep(2)

                pyautogui.click(166, 91)
                time.sleep(10)


    if menu == "3" :
        #2tab
        for x in range(50):
            time.sleep(2)

            viewWebsit = pyautogui.locateCenterOnScreen(
                'images/everve/website/viewWebsit.png',confidence=0.7)
            pyautogui.moveTo(viewWebsit)
            time.sleep(2)
            pyautogui.click(viewWebsit)
            time.sleep(35)

            pyautogui.click(398, 25)
            time.sleep(10)
            report = pyautogui.locateCenterOnScreen(
                'images/everve/reddit/report.png', confidence=0.7)
            print('report', report)
            pyautogui.moveTo(report)
            time.sleep(2)
            pyautogui.click(report)
            time.sleep(5)

            next = pyautogui.locateCenterOnScreen(
                'images/everve/reddit/next.png', confidence=0.7)
            pyautogui.moveTo(next)
            time.sleep(2)
            pyautogui.click(next)
            time.sleep(5)

            next2 = pyautogui.locateCenterOnScreen(
                'images/everve/reddit/next2.png')
            pyautogui.moveTo(next2)
            time.sleep(2)
            pyautogui.click(next2)
            time.sleep(5)
            time.sleep(10)
            x+=1

            print(x)

    if menu == "4" :
        #2tab
        for x in range(20):
            time.sleep(2)
            pyautogui.click(-1280, -219)
            time.sleep(10)
            pyautogui.click(-832, 310)
            time.sleep(5)
            pyautogui.click(-743, 72)

            time.sleep(25)

            pyautogui.click(-969, -250)
            time.sleep(5)
            pyautogui.click(-1071, 225)

            time.sleep(3)
            x+=1

            print(x)

    if menu == "5":
        #80%
        print('run auto skip Ad')
        while True:
            try:
                a, b = pyautogui.locateCenterOnScreen('images/lootv/skipad3.png', confidence=0.9)

            except:
                time.sleep(10)
                print('--')
                pass

            else:
                skipad = pyautogui.locateCenterOnScreen('images/lootv/skipad3.png', confidence=0.9)
                print('skip Ad ', skipad)
                pyautogui.moveTo(skipad)
                time.sleep(2)
                pyautogui.click()



    if menu == "x" :
        break
