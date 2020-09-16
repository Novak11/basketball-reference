'''
Python script that scrapes website-https://www.basketball-reference.com and collects NBA and ABA players data:
-Name
-Career start year
-Career ending year
-Position
-Height
-Weight
-Date of birth
-College
'''


from bs4 import BeautifulSoup
import requests
import concurrent.futures
import time


start = time.perf_counter()

alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
link_list = [f'https://www.basketball-reference.com/players/{x}/' for x in alphabet]
player_count = 0

def download_player_data(link):
    global player_count
    response = requests.get(link)


    #Get HTML structure
    soup = BeautifulSoup(response.content, 'lxml')

    #Find a table with players
    table = soup.find(class_="sortable stats_table")


    #Extract data from table
    # Get body
    tbody = table.find('tbody')
    tr_body = tbody.find_all('tr')

    for trb in tr_body:
        # Get th data
        th = trb.find('th')
        print('\n')
        print(th.get_text())
        player_count += 1

        for td in trb.find_all('td'):
            # Get case value
            print(td.get_text())



#ThreadPool extracting data for players with last name from A-Z
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_player_data, link_list)



print("")
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')

input("Click enter to see the number of players")
print(f'Number of players: {player_count}')
input("Click enter to exit.")