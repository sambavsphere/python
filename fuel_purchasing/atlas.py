import math
class currency():
    def __init__(self,country):
        f_country=open('countrycurrency.csv')
        self.curency_code=''
        for i in f_country.readlines():
            if i[0]==country:
                self.curency_code=i[14]
                break
        f_rate=open('currencyrates.csv')
        self.rate=1
        for i in f_rate.readlines():
            if i[1]==self.curency_code:
                self.rate=i[3]
                break

class airportatlas():
    def __init__(self,csvfile):
        self.csvfile=csvfile
        self.keys=['AirportID','AirportName','CityName','Country','code','ICAOcode','Latitude','Longitude',
        'Altitude','TimeOffset','DST','Tz']
        self.loadData()
    def loadData(self):
        f=open(self.csvfile)
        self.airports_data={}
        for airport in f.readlines():
            airport_list=airport.split(',')
            self.airports_data.update({airport_list[4]:dict(zip(self.keys,[str(i).strip() for i in airport_list]))})
    def getAirport(self,code):
        self.present_airport=self.airports_data.get(code,False)
        return self.present_airport
    def greatcirledist(self,source,airports_4):
        source_actual=source
        #source_details=self.getAirport(source)
        
        short_path=source
        source_airport=source
        total_distance=0
        k=0
        while k<4:
            distance_airports={}
            for airport in airports_4:
                source_details=self.getAirport(source)
                airport_details=self.getAirport(airport)
                dis=self.getDistanceBetweenAirports(
                    source_details['Latitude'],
                    source_details['Longitude'],
                    airport_details['Latitude'],
                    airport_details['Longitude'])
                currency_o=currency(source_details['Country'])
                cost_in_eur=float(currency_o.rate)
                dis=dis*cost_in_eur
                distance_airports.update({source+airport_details['code']:dis})

            distances=[j for (i,j) in distance_airports.iteritems()]
            distances.sort()
            source=[i for (i,j) in  distance_airports.iteritems() if j==distances[0]][0][3:]
            airports_4.remove(source)
            total_distance=total_distance+distances[0]
            short_path=short_path+source
            k=k+1
        airport_details=self.getAirport(source)
        source_actual_details=self.getAirport(source_actual)
        dis=self.getDistanceBetweenAirports(source_details['Latitude'],source_details['Longitude'],source_actual_details['Latitude'],source_actual_details['Longitude'])
        total_distance=total_distance+dis
        short_path=short_path+source_actual
        return short_path,total_distance
    def getDistanceBetweenAirports(self,lat1, long1, lat2, long2):
        # Convert latitude and longitude to
        # spherical coordinates in radians.
        degrees_to_radians = math.pi/180.0
             
        # phi = 90 - latitude
        lat1=float(lat1)
        lat2=float(lat2)
        long1=float(long1)
        long2=float(long2)
        phi1 = (90.0 - lat1)*degrees_to_radians
        phi2 = (90.0 - lat2)*degrees_to_radians
             
        # theta = longitude
        theta1 = long1*degrees_to_radians
        theta2 = long2*degrees_to_radians
             
        # Compute spherical distance from spherical coordinates.
             
        # For two locations in spherical coordinates
        # (1, theta, phi) and (1, theta', phi')
        # cosine( arc length ) =
        #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
        # distance = rho * arc length
         
        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
               math.cos(phi1)*math.cos(phi2))
        arc = math.acos( cos )
     
        # Remember to multiply arc by the radius of the earth
        # in your favorite set of units to get length.
        return arc*6373
        
    def __str__(self):
        return self.present_airport


            
    

    
    
