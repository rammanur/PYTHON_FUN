import urllib

vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK:;;100 Raisin Dr;Fresno;CA;96000;United States of America
EMAIL;PREF;INTERNET:%s
REV:201308219T195243Z
END:VCARD
'''

def make_vcard_and_qr(line):
    fields = line.split(',')

    fname, lname, title, email, phone = fields

    vcard = vcard_template % (lname, fname, fname, lname, title, phone, email)

    filename = '%s_%s.vcard' % (fname, lname)
    with open(filename, 'w') as f:
        f.write(vcard)

    link = 'http://example.com/vcard/%s_%s.vcard' % (fname, lname)
    quoted_link = urllib.urlencode({'chl': link})
    qr_url = 'https://chart.googleapis.com/chart?chs=300x300&cht=qr&' + quoted_link

    f = urllib.urlopen(qr_url)
    image = f.read()

    filename = '%s_%s.png' % (fname, lname)
    with open(filename, 'wb') as f:
        f.write(image)

with open('notes/raisin_team.csv') as f:
    for line in f:
        make_vcard_and_qr(line)
