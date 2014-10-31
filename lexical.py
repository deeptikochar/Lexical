import sqlite3

def lexical_analysis(url):
    temp = url.find('//')
    if temp != -1:
        url = url[temp+2:]

    print(url)
    url_length = len(url)		# URL length
    print(url_length)

    # Getting the domain and path tokens
    domain_tokens = get_domain_tokens(url)
    path_tokens = get_path_tokens(url)

    domain_characteristics = token_characteristics(domain_tokens)
    print(domain_characteristics)
    path_characteristics = token_characteristics(path_tokens)
    print(path_characteristics)


def get_domain_tokens(url):
    temp = url.find('/')
    domain_length = temp
    if temp == -1:
        domain_length = len(url)

    print(domain_length)	# Domain Length

    temp2 = url[0:domain_length]
    domains = temp2.split('.')
    print(domains)
    return domains

def get_path_tokens(url):
    temp = url.find('/')
    path = url[temp+1:]

    path_tokens = path.split('/')
    print(path_tokens)
    return path_tokens

def token_characteristics(tokens):
    print(tokens)
    token_chars = []
    token_count = len(tokens)	# Domain token count

    total_length = 0
    avg_length = 0
    max_length = 0

    for token in tokens:
        length = len(token)
        total_length += length
        if max_length < length:
            max_length = length

    avg_length = total_length/token_count
    total_length = total_length + token_count - 1

    token_chars.append(token_count)
    token_chars.append(total_length)
    token_chars.append(avg_length)
    token_chars.append(max_length)
    return token_chars



input_url = "https://www.jetbrains.com/pycharm/webhelp/configuring-python-interpreter-for-a-project.html"
lexical_analysis(input_url)


def main():
    import csv
    f=open('verified_online.csv')
    csv_f=csv.reader(f)

    for row in csv_f:
        url = row[1]
        target = row[7]
        lexical_analysis(url)
