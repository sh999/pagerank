import json
from pprint import pprint
line = json.loads('{"url": "http://www.engr.uky.edu/", "linkedurls": ["http://www.engr.uky.edu/paducah/", "http://www.engr.uky.edu/internal/", "http://www.engr.uky.edu/directory/", "http://www.engr.uky.edu/paducah/", "http://www.engr.uky.edu/internal/", "http://www.engr.uky.edu/directory/", "http://www.engr.uky.edu/", "http://www.engr.uky.edu/academics/", "http://www.engr.uky.edu/academics/engineering-departments/", "http://www.engr.uky.edu/academics/undergraduate-engineering-degrees/", "http://www.engr.uky.edu/academics/fyp/", "http://www.engr.uky.edu/academics/graduate-students/", "http://www.engr.uky.edu/academics/certificates/", "http://www.engr.uky.edu/academics/international/", "http://www.engr.uky.edu/academics/engineering-mba/", "http://www.engr.uky.edu/academics/seam/", "http://leadership.engr.uky.edu/", "http://www.engr.uky.edu/academics/university-scholars/", "http://www.engr.uky.edu/admissions/", "http://www.engr.uky.edu/visit/", "http://www.engr.uky.edu/admissions/undergraduate/", "http://www.engr.uky.edu/admissions/graduate-admissions/", "http://www.engr.uky.edu/admissions/international/", "http://www.engr.uky.edu/admissions/transfer/", "http://www.engr.uky.edu/admissions/contact/", "http://www.engr.uky.edu/ambassadors/", "http://www.engr.uky.edu/students/", "http://www.engr.uky.edu/students/advising/", "http://www.engr.uky.edu/coop/", "http://www.engr.uky.edu/careers/", "http://www.engr.uky.edu/scholarships/", "http://www.engr.uky.edu/students/student-organizations/", "http://www.engr.uky.edu/estudio/", "http://www.engr.uky.edu/ecs/recommendations/", "http://www.engr.uky.edu/wie-mentoring-program/", "http://www.engr.uky.edu/alumni-mentoring-program/", "http://www.engr.uky.edu/alumni-mentoring-program/student-mentoring-application/", "http://www.engr.uky.edu/alumni-mentoring-program/alumni-mentor-application/", "http://www.engr.uky.edu/research/", "http://www.engr.uky.edu/research/", "http://www.engr.uky.edu/centers-consortia/", "http://www.engr.uky.edu/kej/research2015/", "http://www.engr.uky.edu/about/welcome-from-dean/", "http://www.engr.uky.edu/visit/", "http://www.engr.uky.edu/about/administration/", "http://www.engr.uky.edu/advancement/", "http://www.engr.uky.edu/about/facilities/", "http://www.engr.uky.edu/about/history/", "http://www.engr.uky.edu/about/welcome-from-dean/", "http://www.engr.uky.edu/top50/", "http://www.engr.uky.edu/about/mission/", "http://www.engr.uky.edu/accreditation/", "http://www.engr.uky.edu/academics/", "http://www.engr.uky.edu/academics/engineering-departments/", "http://www.engr.uky.edu/academics/undergraduate-engineering-degrees/", "http://www.engr.uky.edu/academics/fyp/", "http://www.engr.uky.edu/academics/graduate-students/", "http://www.engr.uky.edu/academics/certificates/", "http://www.engr.uky.edu/academics/international/", "http://www.engr.uky.edu/academics/engineering-mba/", "http://www.engr.uky.edu/academics/seam/", "http://leadership.engr.uky.edu/", "http://www.engr.uky.edu/academics/university-scholars/", "http://www.engr.uky.edu/admissions/", "http://www.engr.uky.edu/visit/", "http://www.engr.uky.edu/admissions/undergraduate/", "http://www.engr.uky.edu/admissions/graduate-admissions/", "http://www.engr.uky.edu/admissions/international/", "http://www.engr.uky.edu/admissions/transfer/", "http://www.engr.uky.edu/admissions/contact/", "http://www.engr.uky.edu/ambassadors/", "http://www.engr.uky.edu/students/", "http://www.engr.uky.edu/students/advising/", "http://www.engr.uky.edu/coop/", "http://www.engr.uky.edu/careers/", "http://www.engr.uky.edu/scholarships/", "http://www.engr.uky.edu/students/student-organizations/", "http://www.engr.uky.edu/estudio/", "http://www.engr.uky.edu/ecs/recommendations/", "http://www.engr.uky.edu/wie-mentoring-program/", "http://www.engr.uky.edu/alumni-mentoring-program/", "http://www.engr.uky.edu/alumni-mentoring-program/student-mentoring-application/", "http://www.engr.uky.edu/alumni-mentoring-program/alumni-mentor-application/", "http://www.engr.uky.edu/research/", "http://www.engr.uky.edu/research/", "http://www.engr.uky.edu/centers-consortia/", "http://www.engr.uky.edu/kej/research2015/", "http://www.engr.uky.edu/about/welcome-from-dean/", "http://www.engr.uky.edu/visit/", "http://www.engr.uky.edu/about/administration/", "http://www.engr.uky.edu/advancement/", "http://www.engr.uky.edu/about/facilities/", "http://www.engr.uky.edu/about/history/", "http://www.engr.uky.edu/about/welcome-from-dean/", "http://www.engr.uky.edu/top50/", "http://www.engr.uky.edu/about/mission/", "http://www.engr.uky.edu/accreditation/", "http://www.engr.uky.edu/visit/", "http://www.engr.uky.edu/academics/undergraduate-engineering-degrees/", "http://www.engr.uky.edu/visit/", "http://www.engr.uky.edu/academics/undergraduate-engineering-degrees/", "http://www.engr.uky.edu/cme/", "http://www.engr.uky.edu/ce/", "http://www.engr.uky.edu/ece/", "http://www.engr.uky.edu/me/", "http://www.engr.uky.edu/mng/", "http://www.engr.uky.edu/event/family-engineering-breakfast/", "http://www.engr.uky.edu/event/james-forbes-ph-d-seminar/", "http://www.engr.uky.edu/event/marco-panesi-ph-d-seminar/", "http://www.engr.uky.edu/events/", "http://www.engr.uky.edu/admissions/", "http://www.engr.uky.edu/students/", "http://www.engr.uky.edu/alumni", "http://www.engr.uky.edu/Internal", "http://www.engr.uky.edu/visit/", "http://www.engr.uky.edu/scholarships/", "http://www.engr.uky.edu/academics/", "http://www.engr.uky.edu/directory/", "http://www.engr.uky.edu/top50/", "http://www.engr.uky.edu/accreditation/", "http://www.engr.uky.edu/kej/", "http://www.engr.uky.edu/news/2016/09/22/en-gedi-scroll-high-tech-recovery/", "http://www.engr.uky.edu/news/2016/09/22/en-gedi-scroll-high-tech-recovery/", "http://www.engr.uky.edu/news/2016/09/16/onr-grant-award-young-adams/", "http://www.engr.uky.edu/news/2016/09/16/onr-grant-award-young-adams/", "http://www.engr.uky.edu/news/2016/09/13/doe-award-hastings/", "http://www.engr.uky.edu/news/2016/09/13/doe-award-hastings/", "http://www.engr.uky.edu/accreditation/", "http://www.engr.uky.edu/ecs/contacts/"]}')
site = line['url']
links = line['linkedurls']
d = {}
for l in links:
	to_insert = {}
	to_insert[l] = 0
	d.update(to_insert)
pprint(d)
