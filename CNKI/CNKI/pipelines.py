from scrapy.exceptions import DropItem


class CnkiPipeline(object):
    '''
    #filter_str = "/Article/"
    filter_str = "http://"

    def process_item(self, item, spider):
        if self.filter_str in item['href']:
            print(item['title'], item['href'])
            with open('./tmp.csv', 'a') as f:
                f.write(item['title']+','+item['href']+'\n')
            return item
        else:
            raise DropItem("this's not a normal paper")
    '''
    def process_item(self, item, spider):
        with open('./data/temp.txt', 'a') as f:
            f.write(item['title'] + '\t'+item['href'] + '\t'+item['abstract'] + '\n')
        with open('./data/urls.txt', 'a') as f:
            f.write(item['href']+'\n')
        return item

