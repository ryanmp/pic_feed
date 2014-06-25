import os, jinja2, time, datetime, math

def main():
	out = get_imgs()
	render_template(out[0], out[1], out[2])

def get_imgs():
	print 'get image list'
	path = os.getcwd()
	ret_name = []
	ret_ext = []
	fdates = []
	datetimes = []
	all_files = os.listdir(path+'/img')
	for f in all_files:
		if f.endswith(('.png', '.jpg','.jpeg','.gif')):

			creation_time = os.stat(path+'/img/'+f).st_mtime
			as_datetime = datetime.datetime.strptime(time.ctime(creation_time), "%a %b %d %H:%M:%S %Y")
			datetimes.append(as_datetime)
			fdate = as_datetime.strftime("%B %e, %Y")
			fdates.append(fdate)
			
			tmp = f.split('.')
			ret_name.append(tmp[0])
			ret_ext.append(tmp[1])
	return [ret_name, ret_ext, fdates, datetimes]


def render_template(_names, _exts, _dates):

	total_images = len(_names)
	images_per_page = 5
	num_pages = int(math.ceil(float(total_images)/images_per_page))

	# generate list of html pages to be rendered
	pages = []
	for i in xrange(num_pages):
		if (i == 0):
			this_page = 'index.html'
		else: 
			this_page = str(i+1)+'.html'
		pages.append(this_page)

	# render all pages
	for i in xrange(num_pages):

		# calculate start and index index for picture range to be used on a given template
		if i < (num_pages-1):
			start_idx = i*images_per_page
			end_idx = i*images_per_page + images_per_page
		else:
			start_idx = i*images_per_page
			end_idx = None

		print 'render template:', i
		templateEnv = jinja2.Environment( loader= jinja2.FileSystemLoader( os.getcwd() ) )
		template = templateEnv.get_template( "index.jinja" )

		templateVars = { "title" : "miscellaneous images",
		                 "names" : _names[start_idx:end_idx],
		                 "exts" : _exts[start_idx:end_idx],
		                 "dates" : _dates[start_idx:end_idx],
		                 "num_pages": num_pages,
		                 "pages" : pages,
		                 "which_page": i+1
		               }

		index = open(pages[i], 'w+')
		index.write( template.render( templateVars ) )


main()