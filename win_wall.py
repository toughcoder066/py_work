import os
'''
==windows wallpaper saver==

1. set the source path
2. set the destination path
2. grab every file from the step 1 path and send a copy to destination path
3. rename the files to a four-lettered file
4. append .jpg to the files
5. check the file size and delete files less than 900kb
'''

class MakeACopy:
	def __init__(self,dest):
		self.dest = os.path.join('Desktop',dest)
		self.img_path = os.environ.get('LOCALAPPDATA')
		self.appendage = "Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
		self.file_source = os.path.join(self.img_path,self.appendage)
		self.dest_path = os.path.join(os.environ.get('USERPROFILE'), self.dest)
	
	def make_process(self):	
		try:
			os.mkdir(r''.join(self.dest_path))
		except FileExistsError:
			print('copying to already existing directory ...')
		
	
	def copy_to_dest(self):
		self.make_process()
		for s_files in os.listdir(self.file_source):
			import shutil
			sf = os.path.join(self.file_source,s_files)
			sf_slice = ''.join(list(os.path.split(sf)[1]))[:4]
			
			if sf_slice+'.jpg' in [s for s in os.listdir(self.dest_path)]:
				continue
				#raise FileExistsError('the file already exists in the destination directory')
			else:
				shutil.copy(sf,self.dest_path)
				
			for n_files in os.listdir(self.dest_path):
				if os.stat(self.dest_path+'\\'+ n_files).st_size > 900000:
					try:
						os.rename(self.dest_path+'\\'+ n_files,self.dest_path+'\\'+n_files[:4]+'.jpg')
					except FileExistsError:
						pass
				else:
					os.remove(self.dest_path+'\\'+ n_files)
				
		print('copy done')

def my_copy(dest):
	var = MakeACopy(dest)
	var.copy_to_dest()
	

if __name__ == '__main__':
	my_copy('picfolder')
	
