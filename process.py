import csv
import os


os.system("tap-adwords -c config.json -p catalog.json > shopping.csv")


readfile = open('shopping.csv', 'rt', newline='')
writefile = open('final_shopping.csv', 'wt', newline='')
reader = csv.reader(readfile, delimiter=',', quotechar='"')
writer = csv.writer(writefile, quoting=csv.QUOTE_ALL, escapechar='\\', delimiter=',')



for row in reader:
    if row[0] == "{\"type\": \"RECORD\"":
        newrow = []
        for n in range(len(row)):
            if (row[n].find("_sdc_report_datetime") > 0) | (row[n].find("time_extracted") > 0):
                col_len = len(row[n]) - 1
                position_data = row[n].find(": ") + 2
            elif row[n].find("{\"account") > 0:
                col_len = len(row[n])
                position_data = row[n].find("account\": ") + 10
            else:
                col_len = len(row[n])
                position_data = row[n].find(": ") + 2
            fixed = row[n][position_data:col_len]
            newrow.append(fixed.strip('\"'))
        # print(newrow)
        writer.writerow(newrow)

# 'AccountDescriptiveName', 'AdGroupId', 'AdGroupName', 'AdGroupStatus', 'AdNetworkType1', 'AggregatorId', 'AverageCpc', 'Brand', 'CampaignId', 'CampaignName', 'Channel', 'ChannelExclusivity', 'Clicks', 'ClickType', 'Cost', 'Ctr', 'Date', 'Device', 'ExternalCustomerId', 'Impressions', 'OfferId', 'ProductTitle'
