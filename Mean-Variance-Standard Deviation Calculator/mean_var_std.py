def calculate(nine_digit_list):
    try:
        import numpy as np
        
        dictionary = {}
        mean = []
        variance = []
        std = []
        max_ = []
        min_ = []
        sum_ = []
        
        
        a = np.array(nine_digit_list)
        a = a.reshape(3,3)
        
        mean_axis_1 = list(a.mean(axis=0))
        mean_axis_2 = list(a.mean(axis=1))
        mean_flattened = a.mean()
        mean.append(mean_axis_1)
        mean.append(mean_axis_2)
        mean.append(mean_flattened)
    
    
        variance_axis_1 = list(a.var(axis=0))
        variance_axis_2 = list(a.var(axis=1))
        variance_flattened = a.var()
        variance.append(variance_axis_1)
        variance.append(variance_axis_2)
        variance.append(variance_flattened)
    
    
        std_axis_1 = list(a.std(axis=0))
        std_axis_2 = list(a.std(axis=1))
        std_flattened = a.std()
        std.append(std_axis_1)
        std.append(std_axis_2)
        std.append(std_flattened)
    
    
        max_axis_1 = list(a.max(axis=0))
        max_axis_2 = list(a.max(axis=1))
        max_flattened = a.max()
        max_.append(max_axis_1)
        max_.append(max_axis_2)
        max_.append(max_flattened)
    
    
        min_axis_1 = list(a.min(axis=0))
        min_axis_2 = list(a.min(axis=1))
        min_flattened = a.min()
        min_.append(min_axis_1)
        min_.append(min_axis_2)
        min_.append(min_flattened)
    
    
        sum_axis_1 = list(a.sum(axis=0))
        sum_axis_2 = list(a.sum(axis=1))
        sum_flattened = a.sum()
        sum_.append(sum_axis_1)
        sum_.append(sum_axis_2)
        sum_.append(sum_flattened)
    
    
        dictionary['mean'] = mean
        dictionary['variance'] = variance
        dictionary['standard deviation'] = std
        dictionary['max'] = max_
        dictionary['min'] = min_
        dictionary['sum'] = sum_
        return dictionary
    
    except:
        return "List must contain nine numbers."