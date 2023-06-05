#############
# FUNCTIONS #
#############

en_dictionary = {}
def build_dictionary():
    en_dictionary['water'] = "wet"
    en_dictionary['fire'] = "hot"
    en_dictionary['earth'] = "hard"
    en_dictionary['frost'] = "cold"

def find_in_dictonary(d: dict, s: str) -> str:
    return d.get(s, "Nous ne connaissons pas ce mot")

    



#######
# RUN #
#######

build_dictionary()
print("find_in_dictonary('water')")
print("> " + find_in_dictonary(en_dictionary, "water"))


print("find_in_dictonary('script')")
print("> " + find_in_dictonary(en_dictionary, "script"))
