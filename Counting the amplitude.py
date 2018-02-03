class CountingAmplitude:

    data_list = []
    while True:
        date = input(f'Enter the temperature measurement date(DD-MM-YY) or enter "end": ')
        if date == 'end':
            print(f'\nYou entered the temperatures for {len(data_list)} days.')
            break
            for x in data_list:
                print(f'Day: {x[0]}, minimum temperature: {x[1]}℃, maximum temperature: {x[2]}℃.')
    
            amplituda_max = ()
            amplituda_min = ()
            first_cycle = True
            
            for x in data_list:
                amplitude_for_day_x = x[2] - x[1]
                if first_cycle == True:
                    amplitude_min = (x[0], amplitude_for_day_x)
                    amplitude_max = (x[0], amplitude_for_day_x)
                    first_cycle = False
                elif amplitude_for_day_x > amplitude_max[1]:
                    amplitude_max = (x[0], amplitude_for_day_x)
                elif amplitude_for_day_x < amplitude_min[1]:
                    amplitude_min = (x[0], amplitude_for_day_x)
                    
            print(f'\nThe minimu temperature was on {amplitude_min[0]} day: {amplitude_min[1]}℃.')
            print(f'The maximum temperature was on {amplitude_max[0]} day: {amplitude_max[1]}℃.')
            break
    
        minimal = int(input(f'Enter the minimum temperature: '))
        maximal = int(input(f'Enter the maximum temperature: '))
        data = (date, minimal, maximal)
    
        data_list.append(data)