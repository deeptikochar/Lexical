import csv

def lexical_analysis(url):
    temp = url.find('//')
    if temp != -1:
        url = url[temp+2:]

    print(url)
    url_length = len(url)		# URL length
    print(url_length)
    domains = domain_characteristics(url)
    path_tokens = path_characteristics(url)
    print(domains)


# Domain characteristics
def domain_characteristics(url):
    temp = url.find('/')
    domain_length = temp
    if temp == -1:
        domain_length = len(url)

    print(domain_length)	# Domain Length

    temp2 = url[0:domain_length]
    domains = temp2.split('.')
    print(domains)

    domain_count = len(domains)	# Domain token count

    avg_length = 0
    max_length = 0

    for token in domains:
        length = len(token)
        avg_length += length
        if max_length < length:
            max_length = length
    avg_length /= domain_count

    print(avg_length)		# Average domain token length
    print(max_length)		# Longest domain token length
    return domains

# Path characteristics

def path_characteristics(url):
    temp = url.find('/')
    path = url[temp+1:]

    path_tokens = path.split('/')
    print(path_tokens)

    token_count = len(path_tokens)	# Path token count

    avg_length = 0
    max_length = 0

    for token in path_tokens:
        length = len(token)
        avg_length += length
        if max_length < length:
            max_length = length
    avg_length /= token_count

    print(avg_length)		# Average path token length
    print(max_length)		# Longest path token length
    return path_tokens


input_url = "https://www.jetbrains.com/pycharm/webhelp/configuring-python-interpreter-for-a-project.html"
lexical_analysis(input_url)