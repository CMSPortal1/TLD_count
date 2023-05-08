import urllib.request  # the lib that handles the url stuff
import tldextract


if __name__ == '__main__':


    target_url = 'https://intel.slashnext.cloud/api/intel/domains?authkey=5710bb344b5efc0fd12d1589176bf34b'
    url_target = urllib.request.urlopen(target_url)
    tmp_copy_string = url_target.read().decode("utf8").split('\n')
    print('got URLs')
    tld_freq = dict()

    for x in tmp_copy_string:
        domain = tldextract.extract(x).domain
        suffix = tldextract.extract(x).suffix
        tld = domain + '.' + suffix
        print(tld)
        if tld in tld_freq:
            tld_freq[tld] = tld_freq[tld] + 1
        else:
            tld_freq[tld] = 1
    print('file processing started')
    with open('tld_frequency.txt', 'w') as f:
        for k,v in tld_freq.items():
            if v >= 3000:
                f.write(str(k)+','+str(v)+'\n')
    print('completed!')
