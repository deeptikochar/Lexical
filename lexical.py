#!/usr/bin/env python
import sqlite3

def lexical_analysis(url):
    return_values = []
    return_values.append(url)
    temp = url.find('//')
    if temp != -1:
        url = url[temp+2:]


    url_length = len(url)		# URL length

    # Getting the domain and path tokens
    domain_tokens = get_domain_tokens(url)
    path_tokens = get_path_tokens(url)

    # Get token count, total length, average length and max length
    domain_characteristics = token_characteristics(domain_tokens)
    path_characteristics = token_characteristics(path_tokens)

    # Get percentage of special characters and all alphabets
    char_freq = character_frequencies(url, url_length - domain_characteristics[0] - path_characteristics[0] + 2)

    return_values.append(url_length)
    return_values.extend(domain_characteristics)
    return_values.extend(path_characteristics)
    return_values.extend(char_freq)
    return return_values

def get_domain_tokens(url):
    temp = url.find('/')
    domain_length = temp
    if temp == -1:
        domain_length = len(url)

    temp2 = url[0:domain_length]
    domains = temp2.split('.')
    return domains

def get_path_tokens(url):
    temp = url.find('/')
    path = url[temp+1:]

    path_tokens = path.split('/')
    return path_tokens

def token_characteristics(tokens):
    token_chars = []
    token_count = len(tokens)	                # Domain token count

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

def character_frequencies(input_str, total_length):
    char_freq = []
    char_freq.extend([0] * 26)
    digit_count = 0
    special_char_count = 0

    for char in input_str:
        ascii_value = ord(char)
        if(ascii_value >= 97 and ascii_value <= 122):       # To find occurrences of [a-z]
            char_freq[ascii_value - 97] += 1
        elif(ascii_value >= 65 and ascii_value <= 90):      # To find occurrences of [A-Z]
            char_freq[ascii_value - 65] += 1
        elif(ascii_value >= 48 and ascii_value <= 57):
            digit_count += 1
        elif(char in "!@#$%^&*()-_=+{}[]|\':;><,?"):        # To find occurrences of special characters
            special_char_count += 1

    char_freq.insert(0, digit_count)
    char_freq.insert(0,special_char_count)
    for i in range(0, len(char_freq)):
        char_freq[i] = char_freq[i] * 100 / total_length

    return char_freq

def main():
    import csv
    f=open('verified_online.csv',"r")
    csv_f=csv.reader(f)

    no_urls = 0
    no_tiny_urls = 0
    tiny_url=['0rz.tw','1link.in','1url.com','2.gp','2big.at','2tu.us','3.ly','307.to','4ms.me','4sq.com','4url.cc','6url.com','7.ly','a.gg','a.nf','aa.cx','abcurl.net','ad.vu','adf.ly','adjix.com','afx.cc','all.fuseurl.com','alturl.com','amzn.to','ar.gy','arst.ch','atu.ca','azc.cc','b23.ru','b2l.me','bacn.me','bcool.bz','binged.it','bit.ly','bizj.us','bloat.me','bravo.ly','bsa.ly','budurl.com','canurl.com','chilp.it','chzb.gr','cl.lk','cl.ly','clck.ru','cli.gs','cliccami.info','clickthru.ca','clop.in','conta.cc','cort.as','cot.ag','crks.me','ctvr.us','cutt.us','dai.ly','decenturl.com','dfl8.me','digbig.com','digg.com','disq.us','dld.bz','dlvr.it','do.my','doiop.com','dopen.us','easyuri.com','easyurl.net','eepurl.com','eweri.com','fa.by','fav.me','fb.me','fbshare.me','ff.im','fff.to','fire.to','firsturl.de','firsturl.net','flic.kr','flq.us','fly2.ws','fon.gs','freak.to','fuseurl.com','fuzzy.to','fwd4.me','fwib.net','g.ro.lt','gizmo.do','gl.am','go.9nl.com','go.ign.com','go.usa.gov','goo.gl','goshrink.com','gu     rl.es','hex.i','hiderefer.com','hmm.ph','href.in','hsblinks.com','htxt.it','huff.to','hulu.com','hurl.me','hurl.ws','icanhaz.com','idek.net','ilix.in','is.gd','its.my','ix.lt','j.mp','jijr.com','kl.am','klck.me','korta.nu','krunchd.com','l9k.net','lat.ms','liip.to','liltext.com','linkbee.com','linkbun.ch','liurl.cn','ln-s.net','ln-s.ru','lnk.gd','lnk.ms','lnkd.in','lnkurl.com','lru.jp','lt.tl','lurl.no','macte.ch','mash.to','merky.de','migre.me','miniurl.com','minurl.fr','mke.me','moby.to','moourl.com','mrte.ch','myloc.me','myurl.in','n.pr','nbc.co','nblo.gs','nn.nf','not.my','notlong.com','nsfw.in','nutshellurl.com','nxy.in','nyti.ms','o-x.fr','oc1.us','om.ly','omf.gd','omoikane.net','on.cnn.com','on.mktw.net','onforb.es','orz.se','ow.ly','ping.fm','pli.gs','pnt.me','politi.co','post.ly','pp.gg','profile.to','ptiturl.com','pub.vitrue.com','qlnk.net','qte.me','qu.tc','qy.fi','r.im','rb6.me','read.bi','readthis.ca','reallytinyurl.com','redir.ec','redirects.ca','redirx.com','retwt.me','ri.ms','rickroll.it',    'riz.gd','rt.nu','ru.ly','rubyurl.com','rurl.org','rww.tw','s4c.in','s7y.us','safe.mn','sameurl.com','sdut.us','shar.es','shink.de','shorl.com','short.ie','short.to','shortlinks.co.uk','shorturl.com','shout.to','show.my','shrinkify.com','shrinkr.com','shrt.fr','shrt.st','shrten.com','shrunkin.com','simurl.com','slate.me','smallr.com','smsh.me','smurl.name','sn.im','snipr.com','snipurl.com','snurl.com','sp2.ro','spedr.com','srnk.net','srs.li','starturl.com','su.pr','surl.co.uk','surl.hu','t.cn','t.co','t.lh.com','ta.gd','tbd.ly','tcrn.ch','tgr.me','tgr.ph','tighturl.com','tiniuri.com','tiny.cc','tiny.ly','tiny.pl','tinylink.in','tinyuri.ca','tinyurl.com','tk.','tl.gd','tmi.me','tnij.org','tnw.to','tny.com','to.','to.ly','togoto.us','totc.us','toysr.us','tpm.ly','tr.im','tra.kz','trunc.it','twhub.com','twirl.at','twitclicks.com','twitterurl.net','twitterurl.org','twiturl.de','twurl.cc','twurl.nl','u.mavrev.com','u.nu','u76.org','ub0.cc','ulu.lu','updating.me','ur1.ca','url.az','url.co.uk','url.ie','url360.me    ','url4.eu','urlborg.com','urlbrief.com','urlcover.com','urlcut.com','urlenco.de','urli.nl','urls.im','urlshorteningservicefortwitter.com','urlx.ie','urlzen.com','usat.ly','use.my','vb.ly','vgn.am','vl.am','vm.lc','w55.de','wapo.st','wapurl.co.uk','wipi.es','wp.me','x.vu','xr.com','xrl.in','xrl.us','xurl.es','xurl.jp','y.ahoo.it','yatuc.com','ye.pe','yep.it','yfrog.com','yhoo.it','yiyd.com','youtu.be','yuarel.com','z0p.de','zi.ma','zi.mu','zipmyurl.com','zud.me','zurl.ws','zz.gd','zzang.kr']

    values = []
    con = sqlite3.connect('lex.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS lexical")
        cur.execute("CREATE TABLE lexical(url TEXT, url_length INT, domain_token_count INT, domain_length INT, domain_avg_length REAL, domain_max_length INT, path_token_count INT, path_length INT, path_average_length REAL, path_max_length INT, special_chars REAL, digits REAL, a REAL, b REAL, c REAL, d REAL, e REAL, f REAL, g REAL, h REAL, i REAL, j REAL, k REAL, l REAL, m REAL, n REAL, o REAL, p REAL, q REAL, r REAL, s REAL, t REAL, u REAL, v REAL, w REAL, x REAL, y REAL, z REAL)")
        for row in csv_f:
            no_urls += 1
            url = row[1]
            target = row[7]
            for i in tiny_url:    # check if the url is a tiny url. If not , analyze the url.
                if(i in url):
                    no_tiny_urls += 1
                    continue
            values = lexical_analysis(url)
            cur.execute("INSERT INTO lexical VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", values)

        cur.execute("SELECT * FROM lexical")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("Number of urls analyzed:")
        print(no_urls)
        print("Number of tiny urls:")
        print(no_tiny_urls)


main()
con = sqlite3.connect('lex.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM lexical")
    count = cur.fetchone()
    print(count)
    cur.execute("SELECT AVG(url_length), AVG(domain_token_count), AVG(domain_length),AVG(domain_avg_length),AVG(domain_max_length),AVG(path_token_count),AVG(path_length),AVG(path_average_length),AVG(path_max_length),AVG(special_chars) from lexical")
    average = cur.fetchone()
    print(average)
