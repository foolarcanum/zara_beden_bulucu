from playwright.sync_api import sync_playwright
from win10toast import ToastNotifier
import time
import msvcrt
toaster = ToastNotifier()
link=input('Linki yapıştır:')
beden=input('Beden gir:')
def size_check():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto(f"{link}")
        size_list=page.locator('[class=size-selector-list]').inner_text()
        size_list=list(size_list.split('\n'))
        print(size_list)
        try:    
            count=size_list.index(beden)
        except ValueError:
            print(f'{beden} seçeneği sitede yok')
            toaster.show_toast(f'{beden} seçeneği sitede yok',' ',
            icon_path=None,
            duration=None,
            threaded=True)
            browser.close()
            return 0        
        check=page.locator('[class=size-selector-list__item-button]').locator(f'nth={count}')
        gel=check.get_attribute('data-qa-action')
        if gel.find('size-out-of-stock')!=-1:
            print('Bedenin yok')
            toaster.show_toast('Bedenin yok',' ',
            icon_path=None,
            duration=None,
            threaded=True)
        else:
            print('Bedenin var')
            toaster.show_toast('Bedenin var',' ',
            icon_path=None,
            duration=None,
            threaded=True)
        browser.close()
def start():
    while True:
        size_check()
        for n in range(600):
            time.sleep(0.1)  
            if msvcrt.kbhit():      #kills the process with a keystroke on terminal
                return 0          
start()            

    
