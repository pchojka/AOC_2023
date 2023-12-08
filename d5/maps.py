import operator
class RangeMap:

    def __init__(self, source_type: str, dst_type: str, dst_range_start: int=0, src_range_start : int=0, range_len: int =0):
        self.source_type = source_type
        self.dst_type = dst_type
        self.dst_start_range = dst_range_start
        self.src_start_range = src_range_start
        self.range_len = range_len
        self.result = []
        self.min_op_range = {}
        self.is_complete = True

    def process(self):
        self.min_op_range = min(self.result, key=operator.itemgetter('op'))
        if self.result[0]['src_min'] != 0:
            self.is_complete = False
            return
        for i in range(0, len(self.result) - 1):
            if self.result[i]['src_max'] != self.result[i+1]['src_min'] -1:
                self.is_complete = False
                return
        
            
    def add_sub_range(self, range):
        self.result.append({
            'src_min': int(range[1]),
            'src_max': int(range[1]) + int(range[2]) -1,
            'op': int(range[0]) - int(range[1])
        })
        self.result.sort(key=operator.itemgetter('src_min'))
 
    def process_input(self,input_type: str, input_value: int):
        if input_type != self.source_type:
            raise TypeError('Input type is not expected')
        for range in self.result:
            if input_value >= range['src_min'] and input_value <= range['src_max']:
                return {
                    'type': self.dst_type,
                    'value': input_value + range['op']
                }
        return {
            'type': self.dst_type,
            'value': input_value
        }
    def process_app_ranges(self, input_min, input_max):
        ranges = []
        for range in self.result:
            if input_min >= range['src_min'] and input_max <= range['src_max']:
                return [range]
            if input_max < range['min_src'] or input_min > range['max_src']:
                continue
            if input_min >= range['src_min'] and input_max >= range['src_max']:
                ranges.append(range)
            if input_min < range['src_min'] and input_max < range['src_max']:
                ranges.append({
                    'src_min': range['src_min'],
                    'src_max': input_max,
                    'op': range['op']
                })
        return ranges
    

    def process_input_range(self, input_type:str, input_min_value:int, input_max_value:int):
            result = []  
            if input_type != self.source_type:
                raise TypeError('Input type is not expected')
            applicable_ranges = self.process_app_ranges(input_min_value, input_max_value)
            match (len(applicable_ranges)):
                case 0:
                    result.append({
                        'type': self.dst_type,
                        'min_value': input_min_value,
                        'max_value': input_max_value
                    })
                case 1:
                    result.append({
                        'type': self.dst_type,
                        'min_value': input_min_value+ applicable_ranges[0]['op'],
                        'max_value': input_max_value + applicable_ranges[0]['op']
                    })
            return result
            
    def __repr__(self) -> str:
        res = ""
        res += f"{self.source_type} => {self.dst_type}\n"
        for range in self.result:
             res+= f"SRC : {range['src_min']} => {range['src_max']} ; Op : {range['op']}\n"
        res+= f"Min_ops_range: {self.min_op_range['src_min']} => {self.min_op_range['src_max']} ; Op : {self.min_op_range['op']}\n"

        return res


