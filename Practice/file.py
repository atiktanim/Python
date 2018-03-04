from urllib import request

url='http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv'
def download_stock_data(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n")

    fx=open('CSV_File.csv','w')
    for line in lines:
           fx.write(line+"\n")
    fx.close()

download_stock_data(url)


