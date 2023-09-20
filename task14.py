months = ['березень', 'квітень', 'травень',
          'червень', 'липень', 'серпень',
          'вересень', 'жовтень', 'листопад',
          'грудень', 'січень', 'лютий']

spring_months = tuple(months[0:3])
summer_months = tuple(months[3:6])
autumn_months = tuple(months[6:9])
winter_months = tuple(months[9:12])

tuple_months = (winter_months, spring_months, summer_months, autumn_months)
print(tuple_months)