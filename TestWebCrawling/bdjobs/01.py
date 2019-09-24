import requests
import re


# Golobal Variable
url = "http://jobs.bdjobs.com/m/jobsearch.aspx?fcatid=8"


html = requests.get(url)
htmlRead = html.text
with open("aBdJobs.html","w") as f:
    f.write(htmlRead)

regex = r'<div class="blog".*?onclick="(.*?)">.*?<div class=\'comp_name_text\'>(.*?)</div><d.*?\'job_title_text\'>(.*?)</div>.*?\'job_title_hb\'>(.*?)</div>.*?\'edu_text_s\'\s*>(.*?)</div>.*?\'edu_text_d\'.*?>(.*?)</div><table.*?\'exp_text\'.*?\'>(.*?)</td>.*?\'dead_text\'.*?\'>(.*?)</td>.*?<li>(.*?)</li>'


bdjobsRE = re.compile(regex,re.S|re.M)
print(bdjobsRE)

jobs = re.findall(bdjobsRE,htmlRead)

print(jobs)
