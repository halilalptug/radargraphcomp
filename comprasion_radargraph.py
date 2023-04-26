import requests
from PIL import Image
from io import BytesIO

class Footballer():
    def __init__(self, name, pace, shoot, passing, dribling, defend, pyshic):
        self.name = name
        self.pace = pace
        self.shoot = shoot
        self.passing = passing
        self.dribling = dribling
        self.defend = defend
        self.pyschic = pyshic
    
    def prepskill(self):
        return ','.join([
            str(self.pace),
            str(self.shoot),
            str(self.passing),
            str(self.dribling),
            str(self.defend),
            str(self.pyschic),
            str(self.pace)
            
        ])
    
    def skill_vis(self):
        
        chart_URL = 'https://image-charts.com/chart'
        
        payload = {
            'chco' : '3092de',
            'chd' : 't:' + self.prepskill(),
            'chdl' : self.name,
            'dhdlp' : 'b',
            'chs' : '480x480',
            'cht' : 'r',
            'chtt' : 'Footballer Skills',
            'chl' : 'Pace|Shoot|Passing|Dribling|Defending|Pyshics',
            'chxl': '0:|0|20|40|60|80|100',
            'chxt': 'x',
            'chxr': '0,0.0,100.0',
            'chm': 'B,AAAAAABB,0,0,0'          
        }
        
        response = requests.post(grafik_URL, data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()
        
    def skill_compare(self, targetfootballer):
        
        chart_URL = 'https://image-charts.com/chart'
        
        payload = {
            'chco' : '3092de,027182',
            'chd' : 't:' + self.prepskill() + '|' + targetfootballer.prepskill(),
            'chdl' : self.name + '|' + targetfootballer.name,
            'dhdlp' : 'b',
            'chs' : '480x480',
            'cht' : 'r',
            'chtt' : 'Footballer Skills',
            'chl' : 'Pace|Shoot|Passing|Dribling|Defending|Pyshics',
            'chxl': '0:|0|20|40|60|80|100',
            'chxt': 'x',
            'chxr': '0,0.0,100.0',
            'chm': 'B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0'          
        }
        
        response = requests.post(grafik_URL, data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()

messi = Footballer('Messi', 85, 92, 91, 95, 38, 65)
ronaldo = Footballer('Ronaldo', 89, 93, 81, 89, 35, 77)

ronaldo.skill_compare(messi)
