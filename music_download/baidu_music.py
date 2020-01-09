import requests, sys, getopt


def download_music(songid):
    response = requests.get('http://musicapi.taihe.com/v1/restserver/'
                            'ting?method=baidu.ting.song.playAAC&'
                            'format=jsonp&songid={songid}&from=web'.format(songid=songid))
    # 乱码
    # response.encoding = response.apparent_encoding
    data_json = response.json()
    # pprint.pprint(data_json)

    music_url = data_json['bitrate']['file_link']
    music_name = data_json['songinfo']['title']
    print(''.join([music_name, ':', music_url]))
    music_response = requests.get(music_url)
    with open(music_name + '.mp4', 'wb') as f:
        f.write(music_response.content)
        print(music_name, '下载完成')


if __name__ == '__main__':
    current_script_name = 'baidu_music.py'
    args_ = sys.argv[1:]
    if args_:
        try:
            opts, args = getopt.getopt(args_, 'hd:', ["download="])
        except:
            print('Error:%s -d <download song id>' % current_script_name)
            print('or:%s --dowmload=<download song id>' % current_script_name)
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('%s -d <dowmload song id>' % current_script_name)
                print('  or: %s --download=<download song id>' % current_script_name)
            elif opt in ('-d', '--download'):
                download_id = arg
        # download_id = input('Enter the song id ：')
        try:
            download_music(download_id)
        except:
            print('No song found!')
    else:
        print('Error:%s -d <download song id>' % current_script_name)
        print('or:%s --download=<download song id>' % current_script_name)
# response = requests.get('https://music.taihe.com/artist/177787?pst=sug')
# response.encoding = response.apparent_encoding
# songids = re.findall('"/song/(\d+)"', response.text)
# for songid in songids:
#     download_music(songid)
