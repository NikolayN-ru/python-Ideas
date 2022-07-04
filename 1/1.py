from icrawler.builtin import GoogleImageCrawler

def google_img_downloader():
	crawler = GoogleImageCrawler(storage={'root_dir': './img'})
	filters = dict(
		type='photo',
		# color='blackandwite'
		)
	crawler.crawl(keyword='florida Miami', max_num=5, min_size=(1000, 1000), overwrite=True, filters=filters)
	


def main():
	google_img_downloader()

if __name__ == '__main__':
	main()
