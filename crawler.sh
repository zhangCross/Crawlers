#!/bin/bash -x

get_detail()
{
    curl "http://www.website.com/search/getDetail.htm" -H "Cookie: hdflag=invalite; JSESSIONID=25E5E6A46456816E905024D504C7D1FC; Hm_lvt_accc94e05dd4516e89bc93ebd0d3938e=1479092037; Hm_lpvt_accc94e05dd4516e89bc93ebd0d3938e=1479092037; username=abc; password=b3918ccab7741b2f27bf755719c9dd3e; huodong=website; hdflag=active; resume_record=100026995963"%"2C100023693228"%"2C100009407392"%"2C100027002033; Hm_lvt_b9e62a948ba6b6274cc0fa7e61b1b38b=1479092037; Hm_lpvt_b9e62a948ba6b6274cc0fa7e61b1b38b=1479107997" -H "Origin: http://www.website.com" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Referer: http://www.website.com/search/detail.htm?ids=MTAwMDI3MDAyMDMz" -H "X-Requested-With: XMLHttpRequest" -H "Connection: keep-alive" --data "id=100027002033&_random=0.21856303022306323" --compressed
}

#get_detail


by_form_data()
{
curl "http://www.website.com/search/getDetail.htm" -H "Cookie:JSESSIONID=25E5E6A46456816E905024D504C7D1FC; username=15601257869; password=b3918ccab7741b2f27bf755719c9dd3e; Hm_lvt_b9e62a948ba6b6274cc0fa7e61b1b38b=1479092037; Hm_lpvt_b9e62a948ba6b6274cc0fa7e61b1b38b=1479107997" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36" -H "Referer: http://www.website.com/search/detail.htm?ids=abc" --data "id=100009407392&_random=0.21856303022306323" --compressed


}


agent()
{
    timeout 100 curl "http://website.com/search/search.htm" -x 172.16.2.25:8080 -H "Cookie: JSESSIONID=D1B04F6023E3CF24CB93AC8D5F608B0D; username=abc; password=b3918ccab7741b2f27bf755719c9dd3e; Hm_lvt_b9e62a948ba6b6274cc0fa7e61b1b38b=1479092037,1479180100; Hm_lpvt_b9e62a948ba6b6274cc0fa7e61b1b38b=1479181894" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36" --data "workYear=0-15&updateDate=3&rows=60&sortBy=1&sortType=1&offset=0&_random=0.2361808842667248" --compressed

}

no_agent()
{
    timeout 100 curl "http://website.com/search/search.htm" -H "Cookie: JSESSIONID=04C1A160D6D6DA0125B885A2A2A22C48; username=abc; password=b3918ccab7741b2f27bf755719c9dd3e; Hm_lvt_553e06d0322a2c6ff45a820e1b26c315=1442980934; Hm_lpvt_553e06d0322a2c6ff45a820e1b26c315=1442995284" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36" --data "workYear=0-15&updateDate=3&rows=60&sortBy=1&sortType=1&offset=0&_random=0.3515498156193644" --compressed

}

host=$1
port=$2
my_agent()
{
    echo $host
    timeout 100 curl "http://website.com/search/search.htm" -x "$host":"$port" -H "Cookie: JSESSIONID=04C1A160D6D6DA0125B885A2A2A22C48; username=abc; password=b3918ccab7741b2f27bf755719c9dd3e; Hm_lvt_553e06d0322a2c6ff45a820e1b26c315=1442980934; Hm_lpvt_553e06d0322a2c6ff45a820e1b26c315=1442995284" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36" --data "workYear=0-15&updateDate=3&rows=60&sortBy=1&sortType=1&offset=0&_random=0.3515498156193644" 

}

#my_agent
#by_form_data

help() {
    perl -lne 'print if (/\(\)\s*$/)' < $0
}

if [ "$1" != "" ]; then
    $*
fi

