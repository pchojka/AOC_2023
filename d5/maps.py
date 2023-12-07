import operator
class RangeMap:

    def __init__(self, source_type: str, dst_type: str, dst_range_start: int=0, src_range_start : int=0, range_len: int =0):
        self.source_type = source_type
        self.dst_type = dst_type
        self.dst_start_range = dst_range_start
        self.src_start_range = src_range_start
        self.range_len = range_len
        self.result = []

    # def process(self):
    #     for i in range(0,self.range_len):
    #         self.result.append({
    #             'src': self.src_start_range+i,
    #             'dst': self.dst_start_range+i
    #         })
            
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
    
    def __repr__(self) -> str:
        res = ""
        res += f"{self.source_type} => {self.dst_type}\n"
        for range in self.result:
             res+= f"SRC : {range['src_min']} => {range['src_max']}\n"
             res+= f"DST : {range['src_min'] + range['op']} => {range['src_max'] + range['op']}\n\n"
        return res


