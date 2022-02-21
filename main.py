"""
modularization with function
"""


def data_extraction():
    """
    date : 20 February 2022
    time :  19:37:59 WIB
    magnitude : 4.6
    depth : 42 km
    location : 9.77 LS - 124.80 BT
    epicenter : The epicenter of the earthquake was on land 29 km southwest of Malacca
    MMI scale :  II Kefamenanu
    :return:
    """

    data = dict()
    data['date'] = '20 February 2022'
    data['time'] = '19:37:59 WIB'
    data['magnitude'] = '4.6'
    data['depth'] = '42 km'
    data['location'] = {'ls' : '9.77' , 'bt' : '124.80' }
    data['epicenter'] = 'The epicenter of the earthquake was on land 29 km southwest of Malacca'
    data['mmi scale'] = 'II Kefamenanu'

    return data


def show_data(param):
    print('Latest Earthquake')
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Magnitude : {result['magnitude']}")
    print(f"location : LS = {result['location']['ls']} , BT = {result['location']['bt']}")
    print(f"Epicenter : {result['epicenter']}")
    print(f"MMI scale : {result['mmi scale']}")


if __name__ == '__main__':
    print('main app')
    result = data_extraction()
    show_data(result)
