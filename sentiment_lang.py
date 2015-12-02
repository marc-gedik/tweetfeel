
def enum(**named_values):
    return type('Enum', (), named_values)
	
Lang = enum(FR='francais', EN='english')