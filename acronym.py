#function to create abbriviation acronym
def abbr(string):
    oupt = string[0]
    for i in range(1, len(string)):
        if string[i - 1] == ' ':
            oupt += string[i]
    oupt = oupt.upper()
    return oupt

a = "Lovely Professional Univercity"

print(abbr(a))
