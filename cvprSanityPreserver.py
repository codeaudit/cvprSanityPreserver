
# coding: utf-8

# In[1]:


'''This python script downloads papers from the CVPR open access website and creates first
page montages of the papers by search term. This query term is searched in the titles of the papers,
and their first pages are used to make four-paper montages of all the papers that match your interest.

You can thus, at a glance check through pertinent papers for your topic of interest from the hundreds
of papers at CVPR.

Code modified from Anrej Karpathy's Arxiv Sanity preserver 
(https://github.com/karpathy/arxiv-sanity-preserver), 
and the name CVPR Sanity Preserver is a homage to his work.

Jay Chakravarty
(pchakra5@ford.com)
August 2017.

'''
############################################################################################
# PARAMETERS TO MODIFY:  
# search term and local directory to save  montage files in.
# Also include url of conference website, which needs to be modified, if you need to duplicate this for 
# other conferences.

string_search_title = 'Localization' # Topic to search for - capitalize first letter because this is how files are named on CVPR site
write_file_path = "/home/pchakra5/Documents/databases/CVPR17/topicwise/" #Local dir to write pdfs, texts and montage images to


base_url = "http://openaccess.thecvf.com/CVPR2017.py" # CVPR 2017 site
base_url1 = "http://openaccess.thecvf.com/" 
base_url2 = "http://openaccess.thecvf.com/content_cvpr_2017/papers/"

############################################################################################
import urllib
import os
import sys
import os
from bs4 import BeautifulSoup


#request = urlretrieve()   request(url, None, None)

with urllib.request.urlopen(base_url) as url:
  response = url.read()

soup = BeautifulSoup(response, "html5lib")

links = soup.findAll('a', href=True)


num_pdfs = 0

'''Example paper path:
           http://openaccess.thecvf.com/content_cvpr_2017/papers/Teney_Graph-Structured_Representations_for_CVPR_2017_paper.pdf'''




print('Downloading pdfs for topic ', string_search_title, '...')
for link in links:
    link1 = link['href']
    if link1.find('pdf', 0, len(link1)) != -1 & link1.find('supplemental', 0, len(link1)) == -1:
        paper_url = base_url1 + link['href']
        if paper_url.find(string_search_title, 0, len(paper_url)) != -1:
            #print (paper_url)
            print('\n')
            num_pdfs += 1
            
            file_name = (paper_url.split(base_url2))[1]
            print(file_name)
            
            write_directory_name = write_file_path + string_search_title + '/pdfs/'
            
            if not os.path.exists(write_directory_name):
                os.makedirs(write_directory_name)
                
            file = open(write_directory_name+file_name, 'wb')
            file.write(urllib.request.urlopen(paper_url).read())
            file.close()
                
            
     
print('\n')
print(num_pdfs, string_search_title, ' papers in all')

            


# In[82]:


# '''Write pdfs to text files'''

# import shutil

# search_pdf_dir_name = write_file_path + string_search_title + '/pdfs/'
# write_txt_dir_name  = write_file_path + string_search_title + '/txts/'




# if not shutil.which('pdftotext'): # needs Python 3.3+
#   print('ERROR: you don\'t have pdftotext installed. Install it first before calling this script')
#   sys.exit()
    
    



# for file in os.listdir(search_pdf_dir_name):
#     if file.endswith(".pdf"):
#         pdf_file_name = os.path.join(search_pdf_dir_name, file)
#         #print(pdf_file_name)
        
#         file_base_name = file.split('.pdf')[0] 
        
#         #print(file_base_name)
        
#         if not os.path.exists(write_txt_dir_name):
#             os.makedirs(write_txt_dir_name)
        
        
#         write_txt_file_name = write_txt_dir_name + file_base_name + '.txt'
#         pdf_path = pdf_file_name
#         txt_path = write_txt_file_name
        
        
                
                
#         cmd = "pdftotext %s %s" % (pdf_path, txt_path)
#         os.system(cmd)
        
# print('Done converting pdfs to text files.')


# In[2]:


'''Extract screenshots of 1st pages of each paper and combine them into a montage image'''
from subprocess import Popen
import time

search_pdf_dir_name = write_file_path + string_search_title + '/pdfs/'
write_montage_dir_name  = write_file_path + string_search_title + '/montage/'

write_montage_tmp_dir_name =  write_file_path + string_search_title + '/montage/tmp/'

file_idx = 0
montage_idx = 0
file_idx1 = 0


num_total_files = 0

for file in os.listdir(search_pdf_dir_name):
    if file.endswith(".pdf"):
        num_total_files += 1
        
        
for file in os.listdir(search_pdf_dir_name):
    if file.endswith(".pdf"):
        pdf_file_name = os.path.join(search_pdf_dir_name, file)
        #print(pdf_file_name)
        
        file_base_name = file.split('.pdf')[0] 
        
        #print(file_base_name)
        
        if not os.path.exists(write_montage_dir_name):
            os.makedirs(write_montage_dir_name)
            
    
        if not os.path.exists(write_montage_tmp_dir_name):
            os.makedirs(write_montage_tmp_dir_name)
        
        #Screenshots of all 7 pages
        #pp = Popen(['convert', '%s[0-7]' % (pdf_file_name, ), '-thumbnail', 'x1024', os.path.join(write_montage_tmp_dir_name, 'thumb.png')])
        #Screenshot of the 1st page
        
        
        
        write_montage_tmp_image_name = str(file_idx1) + '.png'
        #print(write_montage_tmp_image_name)
        pp = Popen(['convert', '%s[0]' % (pdf_file_name, ), '-thumbnail', 'x1824', 
                    os.path.join(write_montage_tmp_dir_name, write_montage_tmp_image_name)])
        
        
        
        file_idx += 1
        file_idx1 += 1
        
        
        if file_idx % 4 == 0:
            time.sleep(1.0)
            cmd = "montage -mode concatenate -quality 90 -tile 2 %s %s" % (os.path.join(write_montage_tmp_dir_name, '*.png'), 
                                                                           write_montage_dir_name + str(montage_idx) + '.png')
            
            print('Making montage ', montage_idx)
            #print(cmd)
            time.sleep(1.0)
            os.system(cmd)
            file_idx1 = 0
            montage_idx += 1
            # Delete (move) tmp files
            for buf_file_idx in range(0,4):
                f = os.path.join(write_montage_tmp_dir_name, '%d.png' % (buf_file_idx,))
                f2= os.path.join(write_montage_tmp_dir_name, 'buf-%d.jpg' % (buf_file_idx,))
                if os.path.isfile(f):
                    cmd = 'mv %s %s' % (f, f2)
                    os.system(cmd)
        elif file_idx  == num_total_files:
            time.sleep(1.0)
            cmd = "montage -mode concatenate -quality 90 -tile 2 %s %s" % (os.path.join(write_montage_tmp_dir_name, '*.png'), 
                                                                           write_montage_dir_name + str(montage_idx) + '.png')
            
            print('Making montage ', montage_idx)
            #print(cmd)
            time.sleep(1.0)
            os.system(cmd)
            
        
            
        

print('\n All done! \n')
            
        




        
            
            


# In[ ]:




