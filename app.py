from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from examples import custom_style_2
from console.utils import wait_key
from logic.dt_helper import endDate, list_date
from logic.tw_helper import scrape_topic, sentiment_analysis
from ui.splash import splash, clear, close
from ui.loading import animation
from logic.db_helper import init, get_records_date, get_sentiment, \
    insert_tweet, get_null_sentiment, update_sentiment, \
    get_date
from logic.visualization import fig_ensemble
import ui.menu as menu
import time
import threading

#################################
# Riyad Febrian
# riyadfebrian@gmail.com
# Python Advance Sanbercode
#################################


def ensemble_thread(function, args=0):
    loading_process = threading.Thread(target=function,
                                       kwargs={'data': args})
    loading_process.start()
    animation(loading_process)
    loading_process.join()
    clear()
    time.sleep(.1)


def date_range_menu():
    init_date = list_date(get_date())
    start_date = prompt(menu.pickStartDate(init_date), style=custom_style_2)
    submenu_date = endDate(init_date, start_date['start_dt'])

    end_date = prompt(menu.pickEndDate(submenu_date), style=custom_style_2)
    return start_date, end_date


if __name__ == '__main__':
    clear()
    time.sleep(.1)
    splash()
    init()

    while 1:
        answers = prompt(menu.__menu, style=custom_style_2)

        if answers['menu'] == 'Update Data':
            sub_answer = prompt(menu.__updateData, style=custom_style_2)
            result = scrape_topic(count=int(sub_answer['range']),
                                  max_tweet=int(sub_answer['max_tweet']))

            insert_tweet(result.values.tolist())
            print('Update Data Success')

        elif answers['menu'] == 'Update Sentiment Value':
            unlabeled = get_null_sentiment()
            if len(unlabeled) == 0:
                print("All tweets has been analyzed")
            else:
                result = sentiment_analysis(unlabeled)  # Added Value

                result = result.loc[:, ['value', 'tweet_id']]
                update_sentiment(result.values.tolist())

                print('Update Sentiment Success')

        elif answers['menu'] == 'Show Data':
            st_dt, ed_dt = date_range_menu()
            data = get_records_date(st_dt['start_dt'], ed_dt['end_dt'])
            print(data)

        elif answers['menu'] == 'Visualization':
            st_dt, ed_dt = date_range_menu()
            data = get_sentiment(st_dt['start_dt'], ed_dt['end_dt'])
            ensemble_thread(fig_ensemble, data)

            print(f'Mean = {data.value.mean()}')
            print(f'Median = {data.value.median()}')
            print(f'Std Deviation = {data.value.std()}')

        elif answers['menu'] == 'Quit':
            clear()
            close()
            break

        wait_key()
        clear()
