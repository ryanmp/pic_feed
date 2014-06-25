import os, jinja2, time, datetime

def main():
	print "running main"
	out = get_imgs()
	render_template(out[0], out[1], out[2])

def get_imgs():
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
	templateEnv = jinja2.Environment( loader= jinja2.FileSystemLoader( os.getcwd() ) )
	template = templateEnv.get_template( "index.jinja" )

	templateVars = { "title" : "miscellaneous images",
	                 "names" : _names,
	                 "exts" : _exts,
	                 "dates" : _dates
	               }
	index = open('index.html', 'w+')
	index.write( template.render( templateVars ) ) 

main()