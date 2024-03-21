class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self,name):
        if hasattr(self, 'name') == False:
            if isinstance(name, str) and len(name)>=3:
                self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        visitors = [trip.visitor for trip in Trip.all if trip.national_park == self]
        set_of_visitors = set(visitors)
        list_of_visitors = list(set_of_visitors)
        return list_of_visitors

    def total_visits(self):
        visitors = [trip.visitor for trip in Trip.all if trip.national_park == self]
        return len(visitors)
    
    def best_visitor(self):
        all_visits = [trip.visitor for trip in Trip.all if trip.national_park == self]
        visitors = self.visitors() 
        if len(visitors) > 0:
            best_visitor = visitors[0]
            visits = 0
            for visitor in visitors:
                if all_visits.count(visitor) > visits:
                    best_visitor = visitor
                    visits = all_visits.count(visitor)
            
            return best_visitor
        else: 
            return None


class Trip:
    all =[]

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date,str) and len(start_date)>=7 and check_date_format(start_date):
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self,end_date):
        if isinstance(end_date,str) and len(end_date)>=7 and check_date_format(end_date):
            self._end_date = end_date

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self,visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self,national_park):
        if isinstance(national_park,NationalPark):
            self._national_park = national_park


def check_date_format(date):
    split_date = date.split()
    correct_format = False
    if split_date[0][0].isupper():
        num_of_date = split_date[1][0]
        try:
            if int(num_of_date):
                correct_format = True
        except:
            return correct_format

    return correct_format


class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and len(name)>0 and len(name)<=15:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        visited_parks = [trip.national_park for trip in Trip.all if trip.visitor == self]
        set_of_parks = set(visited_parks)
        unique_parks = list(set_of_parks)
        return unique_parks
    
    def total_visits_at_park(self, park):
        times_visited = 0
        all_trips = [trip for trip in Trip.all if trip.visitor == self]
        for trip in all_trip:
            if trip.national_park == park:
                times_visited+=1

        return times_visited