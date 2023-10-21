# -*- coding: utf-8 -*-
"""Web_scrapping, data extraction and LLM classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EFE3jm_eqK0Kfp4pyA1Oge-TnW9nLP3S
"""

pip install praw

pip install spacy

import praw
import pandas as pd

# Reddit App Credentials (replace with your own)
CLIENT_ID = my_client_id
CLIENT_SECRET = my_client_sercet
USER_AGENT = my_user_agent

# Authenticate with PRAW
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

pip install indian-cities

# get the list of india cities

from indian_cities.dj_city import cities
import spacy
nlp = spacy.load("en_core_web_sm")

print(cities)
keywords1 = []
for i in cities:
  for j in i:
    try:
      keywords1.append(j)
      for k in j:
        try:
          keywords1.append(k)
          for m in k:
            try:
              keywords1.append(m)
            except:
              continue
        except:
          continue
    except:
      continue
  try:
    keywords1.append(i)
  except:
    continue

keywords = []
for i in keywords1:
  if len(i) == 1:
    continue
  elif (i == '(' or i == ')'):
    continue
  elif (type(i) == tuple):
    continue
  else:
    keywords.append(i)
keywords = list(set(keywords))
keywords.append('India')
keywords.append('Indian')
keywords2 = []
for i in range(len(keywords)):
  keywords[i] = keywords[i].lower()

print(keywords)
len(keywords)

# get the keyword list of disease

symptoms = ['discomfort', 'Anuria' , 'oliguria', 'cough', 'Bloody diarrhea', 'Bone pain', 'muscle pain', 'joint pain', 'Bubo-lymphadenitis', 'Chills', 'Common cold', 'Conjunctivitis', 'Cough', 'Cutaneous bleeding', 'Dark urine', 'Dehydration', 'Diarrhea', 'Difficult breathing', 'Fever', 'Headache', 'Hematemesis', 'melena', 'Jaundice', 'Malaise', 'Mental status disturbances', 'Nausea', 'Paralysis', 'Rash', 'Seizures', 'Sore throat', 'Stiff neck', 'Vesicle', 'bullae', 'Vomiting']
disease = ['chicken box', 'mumps', 'thrombocytopenia', 'synodrome', 'cancer', 'hiv', 'aids', 'Tuberculosis', 'diabetes', 'stroke', 'Influenza', 'flu', 'asthma', 'Chronic Obstructive Pulmonary Disease', 'copd', 'heart disease', 'arthritis', 'scabies', 'Chlamydia', 'kidney disease', 'Gonorrhea', 'headaches', 'Diarrhoea', 'allergies', 'common cold', 'Conjunctivitis', 'sick', 'infection', 'salmonella', 'Epilepsy', 'Gonorrhea', 'Attention deficit hyperactivity disorde', 'adhd', 'ebola', 'Mononucleosis', 'Sexually transmitted infection']
for i in range(len(symptoms)):
  symptoms[i] = symptoms[i].lower()
for i in range(len(disease)):
  disease[i] = disease[i].lower()

# scrap data from reddit using praw and spacy nlp. Using spacy is to make sure that the matching is done correctly. Otherwise, 'indiagggy' will be classified as 'india' content

import spacy
import praw
nlp = spacy.load("en_core_web_sm")

# Fetch posts from specific subreddits
#subreddit_name = 'news+worldnews'
#for i in List:
  #subreddit_name = subreddit_name + '+' + i

posts = []
start_time = '2019-08-10'
end_time = '2021-09-10'

List = ["india", "indianews", "DoesAnybodyElse", "Advice", "needadvice", "medizzy", "medicine", "Health", "medicine", "Coronavirus", "COVID19", "PeopleFuckingDying", "flu"]
#List = ["Malaria", "Tuberculosis", "HIV", "hivaids", "hepatitis", "flu"]
for i in List:
  subreddit_name = i
  subreddit = reddit.subreddit(subreddit_name)
  for post in subreddit.top(limit=1000):
      Revalance = False
      if (i == 'india' or i == 'indianews'):
        Revalance = True
      date_created = post.created_utc
      location = 'india'
      title_location = []
      content_location = []
      location_1 = nlp(post.title)
      for entity in location_1.ents:
          if entity.label_ == "GPE":
              title_location.append(entity.text)
      location_2 = nlp(post.selftext)
      for entity in location_2.ents:
          if entity.label_ == "GPE":
              content_location.append(entity.text)
      for m in range(len(title_location)):
          title_location[m] = title_location[m].lower()
      for n in range(len(content_location)):
          content_location[n] = content_location[n].lower()
      for keyword in keywords:
          if (keyword in content_location or keyword in title_location):
              Revalance = True
              if (keyword != 'india' and keyword != 'indian'):
                location = keyword
      content = post.selftext
      if (Revalance == True):
        posts.append({
            'title': post.title,
            'content': post.selftext,
            'url': post.url,
            'date': date_created,
            'location': location
        })

df = pd.DataFrame(posts)
df['date'] = pd.to_datetime(df['date'], unit='s')
#df = pd.DataFrame(list(filter(lambda l: end_time > l["date"] > start_time , df)))

# the scraped data

df2 = df.loc[ (df['date'] < end_time) & (df['date'] > start_time)]
df2.to_csv('dataset_location.csv', index = False, encoding = 'UTF-8')
df4 = df2.loc[ (df2['location'] != 'india') & (df2['location'] != 'indian')]
df4.to_csv('dataset_city_specified.csv', index = False, encoding = 'UTF-8')
df2

city = ['indian', 'kerala',
 'roorkee',
 'nalgonda',
 'harihar',
 'makrana',
 'shantipur',
 'dhuburi',
 'karauli',
 'hindupur',
 'amravati',
 'mainpuri',
 'jalna',
 'jalpaiguri',
 'dhar',
 'jalgaon',
 'odisha',
 'najibabad',
 'telangana',
 'hassan',
 'gujarat',
 'fatehpur',
 'muzaffarnagar',
 'sahaswan',
 'hardoi',
 'rourkela',
 'delhi',
 'india']

for i in range(len(city)):
  city.append(city[i].capitalize())
  city.append(city[i].upper())
city

pip install zstandard

# web scraping using dump files and filter based on india location

import zstandard
import os
import json
import sys
import csv
from datetime import datetime
import logging.handlers


def write_line_zst(handle, line):
	handle.write(line.encode('utf-8'))
	handle.write("\n".encode('utf-8'))


def write_line_json(handle, obj):
	handle.write(json.dumps(obj))
	handle.write("\n")


def write_line_single(handle, obj, field):
	if field in obj:
		handle.write(obj[field])
	else:
		log.info(f"{field} not in object {obj['id']}")
	handle.write("\n")


def write_line_csv(writer, obj, is_submission):
	output_list = []
	output_list.append(str(obj['score']))
	output_list.append(datetime.fromtimestamp(int(obj['created_utc'])).strftime("%Y-%m-%d"))
	if is_submission:
		output_list.append(obj['title'])
	output_list.append(f"u/{obj['author']}")
	output_list.append(f"https://www.reddit.com{obj['permalink']}")
	if is_submission:
		if obj['is_self']:
			if 'selftext' in obj:
				output_list.append(obj['selftext'])
			else:
				output_list.append("")
		else:
			output_list.append(obj['url'])
	else:
		output_list.append(obj['body'])
	writer.writerow(output_list)


def read_and_decode(reader, chunk_size, max_window_size, previous_chunk=None, bytes_read=0):
	chunk = reader.read(chunk_size)
	bytes_read += chunk_size
	if previous_chunk is not None:
		chunk = previous_chunk + chunk
	try:
		return chunk.decode()
	except UnicodeDecodeError:
		if bytes_read > max_window_size:
			raise UnicodeError(f"Unable to decode frame after reading {bytes_read:,} bytes")
		log.info(f"Decoding error with {bytes_read:,} bytes, reading another chunk")
		return read_and_decode(reader, chunk_size, max_window_size, chunk, bytes_read)


def read_lines_zst(file_name):
	with open(file_name, 'rb') as file_handle:
		buffer = ''
		reader = zstandard.ZstdDecompressor(max_window_size=2**31).stream_reader(file_handle)
		while True:
			chunk = read_and_decode(reader, 2**27, (2**29) * 2)

			if not chunk:
				break
			lines = (buffer + chunk).split("\n")

			for line in lines[:-1]:
				yield line.strip(), file_handle.tell()

			buffer = lines[-1]

		reader.close()


def process_file(input_file, output_file, output_format, field, values, from_date, to_date, single_field, exact_match):
	output_path = f"{output_file}.{output_format}"
	is_submission = "submission" in input_file
	log.info(f"Input: {input_file} : Output: {output_path} : Is submission {is_submission}")
	writer = None
	if output_format == "zst":
		handle = zstandard.ZstdCompressor().stream_writer(open(output_path, 'wb'))
	elif output_format == "txt":
		handle = open(output_path, 'w', encoding='UTF-8')
	elif output_format == "csv":
		handle = open(output_path, 'w', encoding='UTF-8', newline='')
		writer = csv.writer(handle)
	else:
		log.error(f"Unsupported output format {output_format}")
		sys.exit()

	file_size = os.stat(input_file).st_size
	created = None
	matched_lines = 0
	bad_lines = 0
	total_lines = 0
	for line, file_bytes_processed in read_lines_zst(input_file):
		total_lines += 1
		if total_lines % 100000 == 0:
			log.info(f"{created.strftime('%Y-%m-%d %H:%M:%S')} : {total_lines:,} : {matched_lines:,} : {bad_lines:,} : {file_bytes_processed:,}:{(file_bytes_processed / file_size) * 100:.0f}%")

		try:
			obj = json.loads(line)
			created = datetime.utcfromtimestamp(int(obj['created_utc']))

			if created < from_date:
				continue
			if created > to_date:
				continue

			if field is not None:
				field_value = obj[field].lower()
				matched = False
				for value in values:
					if exact_match:
						if value == field_value:
							matched = True
							break
					else:
						if value in field_value:
							matched = True
							break
				if not matched:
					continue

			matched_lines += 1
			if output_format == "zst":
				write_line_zst(handle, line)
			elif output_format == "csv":
				write_line_csv(writer, obj, is_submission)
			elif output_format == "txt":
				if single_field is not None:
					write_line_single(handle, obj, single_field)
				else:
					write_line_json(handle, obj)
			else:
				log.info(f"Something went wrong, invalid output format {output_format}")
		except (KeyError, json.JSONDecodeError) as err:
			bad_lines += 1
			if write_bad_lines:
				if isinstance(err, KeyError):
					log.warning(f"Key {field} is not in the object: {err}")
				elif isinstance(err, json.JSONDecodeError):
					log.warning(f"Line decoding failed: {err}")
				log.warning(line)

	handle.close()
	log.info(f"Complete : {total_lines:,} : {matched_lines:,} : {bad_lines:,}")


for i in ['Coronavirus', 'COVID', 'Health', 'india', 'medicine', 'publichealth', 'worldnews']:
		input_file = i + "_submissions.zst"
		i =i.lower()
		output_file = i + "_submissions_1"

		output_format = "csv"

		single_field = None

		write_bad_lines = True


		from_date = datetime.strptime("2015-01-01", "%Y-%m-%d")
		to_date = datetime.strptime("2023-12-31", "%Y-%m-%d")


		field = 'title'
		values = city

		values_file = None
		exact_match = False



		log = logging.getLogger("bot")
		log.setLevel(logging.INFO)
		log_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
		log_str_handler = logging.StreamHandler()
		log_str_handler.setFormatter(log_formatter)
		log.addHandler(log_str_handler)

		if __name__ == "__main__":
			if single_field is not None:
				log.info("Single field output mode, changing output file format to txt")
				output_format = "txt"

			if values_file is not None:
				values = []
				with open(values_file, 'r') as values_handle:
					for value in values_handle:
						values.append(value.strip().lower())
				log.info(f"Loaded {len(values)} from values file {values_file}")
			else:
				values = [value.lower() for value in values]  # convert to lowercase

			log.info(f"Filtering field: {field}")
			if len(values) <= 20:
				log.info(f"On values: {','.join(values)}")
			else:
				log.info(f"On values:")
				for value in values:
					log.info(value)
			log.info(f"Exact match {('on' if exact_match else 'off')}. Single field {single_field}.")
			log.info(f"From date {from_date.strftime('%Y-%m-%d')} to date {to_date.strftime('%Y-%m-%d')}")
			log.info(f"Output format set to {output_format}")

			input_files = []
			if os.path.isdir(input_file):
				if not os.path.exists(output_file):
					os.makedirs(output_file)
				for file in os.listdir(input_file):
					if not os.path.isdir(file) and file.endswith(".zst"):
						input_name = os.path.splitext(os.path.splitext(os.path.basename(file))[0])[0]
						input_files.append((os.path.join(input_file, file), os.path.join(output_file, input_name)))
			else:
				input_files.append((input_file, output_file))
			log.info(f"Processing {len(input_files)} files")
			for file_in, file_out in input_files:
				process_file(file_in, file_out, output_format, field, values, from_date, to_date, single_field, exact_match)

# group all the data from different subreddits into one dataframe

import pandas as pd
covid_1 = pd.read_csv('covid_submissions_1.csv')
health = pd.read_csv('health_submissions_1.csv')
india = pd.read_csv('india_submissions_1.csv')
medicine = pd.read_csv('medicine_submissions_1.csv')
health_2 = pd.read_csv('publichealth_submissions_1.csv')
news = pd.read_csv('worldnews_submissions_1.csv')
covid_2 = pd.read_csv('coronavirus_submissions_1.csv')

data = data.append(news, ignore_index = True)
data = data.append(covid_2, ignore_data = covid_1)
data = data.append(health, ignore_index = True)
data = data.append(india, ignore_index = True)
data = data.append(medicine, ignore_index = True)
data = data.append(health_2, ignore_index = Trueindex = True)

# rename columns of dump file scrapped data

covid_1_rename = covid_1.rename(columns = {'1': 'upvotes', '2020-03-28': 'date', 'Coronavirus की पहली तस्वीर सामने आई,India के पहले patient से लिया गया था नमूना': 'title', 'u/snehaagg': 'poster', 'https://www.reddit.com/r/COVID/comments/fqmqsp/coronavirus_क_पहल_तसवर_समन_आईindia_क_पहल_patient/': 'url', 'https://www.youtube.com/watch?v=PgfkyAGvOb0': 'other links'})
health_rename = health.rename(columns = {'1': 'upvotes', '2015-01-01': 'date', 'IVF Hospitals In Kerala': 'title', 'u/armcivf': 'poster', 'https://www.reddit.com/r/Health/comments/2qzlob/ivf_hospitals_in_kerala/': 'url', 'http://armcivf.net/blog/causes-infertility-india-among-males/': 'other links'})
india_rename = india.rename(columns = {'1': 'upvotes', '2015-01-01': 'date', 'A Sampling of Indian English Accents': 'title', 'u/[deleted]': 'poster', 'https://www.reddit.com/r/india/comments/2qz0n9/a_sampling_of_indian_english_accents/': 'url', 'https://www.youtube.com/watch?v=v9arM_agKFA': 'other links'})
medicine_rename = medicine.rename(columns = {'11': 'upvotes', '2015-01-14': 'date', 'Does anyone have any experience practicing/working with the Indian Health Service?': 'title', 'u/sojo92': 'poster', 'https://www.reddit.com/r/medicine/comments/2sepkd/does_anyone_have_any_experience_practicingworking/': 'url', 'Looking to get some insight on what your experience was like. Was it rewarding? Did you find the financial incentives (i.e. loan repayment) compelling based on your duties? Would you do it again?': 'other links'})
health_2_rename = health_2.rename(columns = {'19': 'upvotes', '2015-02-20': 'date', 'Drug-resistant malaria is on the verge of entering India (X-post from /r/globalhealth)': 'title', 'u/genericaccount1234': 'poster', 'https://www.reddit.com/r/publichealth/comments/2wjm83/drugresistant_malaria_is_on_the_verge_of_entering/': 'url', 'http://www.bbc.com/news/health-31533559': 'other links'})
news_rename = news.rename(columns = {'1': 'upvotes', '2015-01-01': 'date', "Russia's Strategic Shift To East Continues: Now India": 'title', 'u/AriRusila': 'poster', 'https://www.reddit.com/r/worldnews/comments/2qyydq/russias_strategic_shift_to_east_continues_now/': 'url', 'https://arirusila.wordpress.com/2014/12/17/russias-strategic-shift-to-east-continues-now-india/': 'other links'})
covid_2_rename = covid_2.rename(columns = {'5': 'upvotes', '2020-01-25': 'date', "I'm content that there\'s nothing for Indiana ...yet...": 'title', 'u/BigWhails': 'poster', 'https://www.reddit.com/r/Coronavirus/comments/etmmna/im_content_that_theres_nothing_for_indiana_yet/': 'url', "To be honest, I'm just happy I didn't hear about my state yet...I'm I just by myself here? \n\nI realized how paranoid I'm sounding, but cant blame me, I have family I care about.": 'other links'})

data2 = covid_1_rename
data2 = data2.append(news_rename, ignore_index = True)
data2 = data2.append(covid_2_rename, ignore_data = covid_1)
data2 = data2.append(health_rename, ignore_index = True)
data2 = data2.append(india_rename, ignore_index = True)
data2 = data2.append(medicine_rename, ignore_index = True)
data2 = data2.append(health_2_rename, ignore_index = Trueindex = True)
data2.to_csv('dataset_india.csv', index = False, encoding = True)

# open tweets data on kaggle

import json
import pandas as pd
List = []
fin = open('tweets.json')
for i in fin:
  List.append(i)
List

# filter the dataset based on illness keywords and store in seperate dataframe

keywords = []
Likes = []
Tweets = []

for j in List:
  Len = len(j)
  j = j[0:len(j)-1]
  j = json.loads(j)


  keywords.append(j['keyword'])
  Likes.append(j['likes'])
  Tweets.append(j['tweet'])

  data = {
      "keywords": keywords,
      "likes": Likes,
      "tweets": Tweets
  }

df = pd.DataFrame(data)
df = df.loc[(df['keywords'] == 'COVID-19')]
df.to_csv('COVID-19_tweets.csv', index = False, encoding = 'UTF-8')
df = df.loc[(df['keywords'] == 'Vaccine')]
df.to_csv('Vaccine_tweets.csv', index = False, encoding = 'UTF-8')

import pandas as pd
df = pd.read_csv('COVID-19_tweets.csv')
df

"""# Classification using LLM

"""

pip install kor

!pip install -q openai

pip install deep-translator

data = pd.read_csv('dataset_location.csv')

# use LLM to classify reddit posts based on the degree of illness: severe illness, light illness and no illness

import openai

# Authenticate your API key
openai.api_key = "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"

labeled_examples = {
    "no illness": ["Thousands thronged a religious festival in Sanand without masks and social distancing even as the Gujarat government has imposed a Mini Lockdown till May 12", "Just went for a run and feeling energized.", "Her tongue was cut, spine broken. What about you?", "TIL of Ghulam Dastagir, a Stationmaster who refused to leave his post during the Bhopal Gas Tragedy & saved thousands of lives by not letting any trains stop at the station. He spent the next 2 decades in & out of hospital due to long exposure to the gas before passing in 2003"],
    "light illness": ["India Is Making It Nearly Impossible for Homeless People to Get Vaccinated. India’s vaccination program requires a mobile phone and a home address. Many people have neither.", "Slight headache and fatigue.", "Pizza delivery boy tests positive, 72 families in South Delhi ordered to quarantine themselves."],
    "severe illness": ["I'm in a lot of pain today.", "We've only been here a few hours and have seen half a dozen people die while they wait for treatment.", "My grandmother fought and beat COVID after battling it for a month, and turned 94 today.", "Corona Donors"]
}

i = 0
j = 10
Illness = []

while (j < 1087):
  data2 = data.iloc[i:j]
  content_list = data2['tweet'].values.tolist()
  content_list2 = data2['hashtags'].values.tolist()
  for k in range(len(content_list)):
    if str(content_list2[k]) != '[]':
        batch_text = content_list[k] + '. The hashtags of the post is enclosed in the following list: ' + str(content_list2[k])
    else:
        batch_text = content_list[k]
    try:
      response = openai.ChatCompletion.create(
          model="gpt-3.5_turbo",
          messages=[
                {"role": "system", "content": "Classify each of the following social media posts as indicating no illness, light illness, or severe illness. Only output 'no illness', 'light illness', or 'severe illness'. Do not output any word other than those three. Also, we define illness as 'infectious, causing harm to individual's health or the functioning of community. Remember that violence, natural accidents do not count"},
                {"role": "system", "content": f"Here are some examples: {labeled_examples}"},
                {"role": "user", "content": batch_text}
            ],
           max_tokens=50,
           n=1,
           stop=None,temperature=0.3,
          )
    except:
      response = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[
                {"role": "system", "content": "Classify each of the following social media posts as indicating no illness, light illness, or severe illness. Only output 'no illness', 'light illness', or 'severe illness'. Do not output any word other than those three. Also, we define illness as 'infectious, causing harm to individual's health or the functioning of community. Remember that violence, natural accidents do not count"},
                {"role": "system", "content": f"Here are some examples: {labeled_examples}"},
                {"role": "user", "content": batch_text}
            ],
           max_tokens=50,
           n=1,
           stop=None,
           temperature=0.3,
          )
    re = response.choices[0].message.content
    re = re.lower()
    Illness.append(re)
    i = len(Illness)
    j = len(Illness) + 10
  print(len(Illness))


    # Process the response as needed
    #return response.choices[0].message.content

data2 = data.iloc[i: 1087]
content_list = data2['tweet'].values.tolist()
content_list2 = data2['hashtags'].values.tolist()
  for k in range(len(content_list)):
    if str(content_list2[k]) != '[]':
        batch_text = content_list[k] + '. The hashtags of the post is enclosed in the following list: ' + str(content_list2[k])
    else:
        batch_text = content_list[k]
    try:
      response = openai.ChatCompletion.create(
          model="gpt-3.5_turbo",
          messages=[
                {"role": "system", "content": "Classify each of the following social media posts as indicating no illness, light illness, or severe illness. Only output 'no illness', 'light illness', or 'severe illness'. Do not output any word other than those three. Also, we define illness as 'infectious, causing harm to individual's health or the functioning of community. Remember that violence, natural accidents do not count"},
                {"role": "system", "content": f"Here are some examples: {labeled_examples}"},
                {"role": "user", "content": batch_text}
            ],
           max_tokens=50,
           n=1,
           stop=None,temperature=0.3,
          )
    except:
      response = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[
                {"role": "system", "content": "Classify each of the following social media posts as indicating no illness, light illness, or severe illness. Only output 'no illness', 'light illness', or 'severe illness'. Do not output any word other than those three. Also, we define illness as 'infectious, causing harm to individual's health or the functioning of community. Remember that violence, natural accidents do not count"},
                {"role": "system", "content": f"Here are some examples: {labeled_examples}"},
                {"role": "user", "content": batch_text}
            ],
           max_tokens=50,
           n=1,
           stop=None,
           temperature=0.3,
          )
    re = response.choices[0].message.content
    re = re.lower()
    Illness.append(re)
    i = len(Illness)
    j = len(Illness) + 10
print(len(Illness))

data['illness'] = Illness
# show the rows where chatgpt gives outputs that do not match the previous pattern

data2 = data.loc[(data["illness"] != "no illness") & (data["illness"] != "severe illness") & (data["illness"] != "light illness") ]
data2

# change the rows that contains inapprorpiate output accordingly

data["illness"] = data["illness"].replace(["no context", "inappropriate content"], ["no illness", "no illness"])
data.at[726, "illness"] = "no illness"
data.at[605, "illness"] = "no illness"
data.at[402, "illness"] = "no illness"
data100 = data.loc[(data["illness"] != "no illness") & (data["illness"] != "severe illness") & (data["illness"] != "light illness")]
data.to_csv("dataset_with_illness_2.csv", index = False, encoding = "UTF-8")
data

data = pd.read_csv('tweets_9000.csv')

# use LLM to classify twitter posts based on the degree of illness: severe illness, light illness and no illness


import openai
from deep_translator import GoogleTranslator

# Authenticate your API key
openai.api_key = "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"

labeled_examples = {
    "no illness": ["Thousands thronged a religious festival in Sanand without masks and social distancing even as the Gujarat government has imposed a Mini Lockdown till May 12", "Just went for a run and feeling energized.", "Her tongue was cut, spine broken. What about you?", "TIL of Ghulam Dastagir, a Stationmaster who refused to leave his post during the Bhopal Gas Tragedy & saved thousands of lives by not letting any trains stop at the station. He spent the next 2 decades in & out of hospital due to long exposure to the gas before passing in 2003"],
    "light illness": ["India Is Making It Nearly Impossible for Homeless People to Get Vaccinated. India’s vaccination program requires a mobile phone and a home address. Many people have neither.", "Slight headache and fatigue.", "Pizza delivery boy tests positive, 72 families in South Delhi ordered to quarantine themselves."],
    "severe illness": ["I'm in a lot of pain today.", "We've only been here a few hours and have seen half a dozen people die while they wait for treatment.", "My grandmother fought and beat COVID after battling it for a month, and turned 94 today.", "Corona Donors"]
}

i = 0
j = 10
Illness = []

while (j < 9655):
  data2 = data.iloc[i:j]
  content_list = data2['tweet'].values.tolist()
  content_list2 = data2['hashtags'].values.tolist()
  for k in range(len(content_list)):
    if str(content_list2[k]) != '[]':
        context_1 = GoogleTranslator(source='auto').translate(content_list[k])
        context_2 = GoogleTranslator(source = 'auto').translate(content_list2[k])
        batch_text = str(content_list[k]) + '. The hashtags of the post is enclosed in the following list: ' + str(content_list2[k])
    else:
        context_1 = GoogleTranslator(source='auto').translate(content_list[k])
        context_2 = GoogleTranslator(source = 'auto').translate(content_list2[k])
        batch_text = str(content_list[k])
    try:
      response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "Classify each of the following social media posts as indicating no illness, light illness, or severe illness. Only output 'no illness', 'light illness', or 'severe illness'. Do not output any word other than those three. Also, we define illness as 'infectious, causing harm to individual's health or the functioning of community. Remember that violence, natural accidents do not count"},
                {"role": "system", "content": f"Here are some examples: {labeled_examples}"},
                {"role": "user", "content": batch_text}
            ],
           max_tokens=50,
           n=1,
           stop=None,
          temperature=0.3,
          )
    except:
      response = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[
                {"role": "system", "content": "Classify each of the following social media posts as indicating no illness, light illness, or severe illness. Only output 'no illness', 'light illness', or 'severe illness'. Do not output any word other than those three. Also, we define illness as 'infectious, causing harm to individual's health or the functioning of community. Remember that violence, natural accidents do not count"},
                {"role": "system", "content": f"Here are some examples: {labeled_examples}"},
                {"role": "user", "content": batch_text}
            ],
           max_tokens=50,
           n=1,
           stop=None,
           temperature=0.3,
          )
    re = response.choices[0].message.content
    re = re.lower()
    Illness.append(re)
    i = len(Illness)
    j = len(Illness) + 10
  print(len(Illness))

data2 = data.iloc[i: 9655]
content_list = data2['tweet'].values.tolist()
content_list2 = data2['hashtags'].values.tolist()
  for k in range(len(content_list)):
    if str(content_list2[k]) != '[]':
        batch_text = content_list[k] + '. The hashtags of the post is enclosed in the following list: ' + str(content_list2[k])
    else:
        batch_text = content_list[k]
    try:
      response = openai.ChatCompletion.create(
          model="gpt-3.5_turbo",
          messages=[
                {"role": "system", "content": "Classify each of the following social media posts as indicating no illness, light illness, or severe illness. Only output 'no illness', 'light illness', or 'severe illness'. Do not output any word other than those three. Also, we define illness as 'infectious, causing harm to individual's health or the functioning of community. Remember that violence, natural accidents do not count"},
                {"role": "system", "content": f"Here are some examples: {labeled_examples}"},
                {"role": "user", "content": batch_text}
            ],
           max_tokens=50,
           n=1,
           stop=None,temperature=0.3,
          )
    except:
      response = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[
                {"role": "system", "content": "Classify each of the following social media posts as indicating no illness, light illness, or severe illness. Only output 'no illness', 'light illness', or 'severe illness'. Do not output any word other than those three. Also, we define illness as 'infectious, causing harm to individual's health or the functioning of community. Remember that violence, natural accidents do not count"},
                {"role": "system", "content": f"Here are some examples: {labeled_examples}"},
                {"role": "user", "content": batch_text}
            ],
           max_tokens=50,
           n=1,
           stop=None,
           temperature=0.3,
          )
    re = response.choices[0].message.content
    re = re.lower()
    Illness.append(re)
    i = len(Illness)
    j = len(Illness) + 10
print(len(Illness))

data['illness'] = Illness
data.to_csv('9000_rows_dataset_with_illness_classification.csv', index = False, encoding = 'UTF-8')

# show the rows where chatgpt gives outputs that do not match the previous pattern

data2 = data.loc[(data["illness"] != "no illness") & (data["illness"] != "severe illness") & (data["illness"] != "light illness") ]
data2

# change the rows that contains inapprorpiate output accordingly

data["illness"] = data["illness"].replace(["no context", "inappropriate content"], ["no illness", "no illness"])
data.at[478, "illness"] = "no illness"
data100 = data.loc[(data["illness"] != "no illness") & (data["illness"] != "severe illness") & (data["illness"] != "light illness")]
data.to_csv("dataset_with_illness_2.csv", index = False, encoding = "UTF-8")

len(Illness)

data1000 = data.iloc[0: 1474]
data1000['illness'] = Illness
data1000
data1000.to_csv('data_get_percentage.csv', index = False, encoding = 'UTF-8')

data1001 = data

# get the percentage of illness related posts in different dates

import pandas as pd
data4 = pd.read_csv('Dataset_with_illness_3.csv')
data5 = data4.sort_values(by = 'date')
col3 = data5['date'].values.tolist()
for i in col3:
  data5.replace(i, i[0:10], inplace = True)
col = data5['date'].values.tolist()
col2 = data5['illness'].values.tolist()
Dict = {}
Dict2 = {}
for i in col:
  if i not in Dict:
    Dict[i] = 1
  else:
    Dict[i] = Dict[i] + 1
for i in Dict:
  if i not in Dict2:
    data100 = data5.loc[(data5['date'] == i) & (data5['illness'] != 'no illness')]
    x = len(data100.index)
    Dict2[i] = str(x) + '/' + str(int(Dict[i])) + ' = ' + str(x/int(Dict[i]))
Dict2

# get the dataframe of percentage of posts that contain illness keyword on different days

import pandas as pd
col = data1001['created_at'].values.tolist()
for i in col:
  data1001.replace(i, i[0:10], inplace = True)
data1002 = data1001.sort_values(by = 'created_at')
col2 = data1002['created_at'].values.tolist()
Dict = dict(data1002['created_at'].value_counts())
List2 = []
List3 = []
List4 = []
for i in Dict:
  if i not in List2:
    x = 0
    data1003 = data1002.loc[(data1002['created_at'] == i)]
    data_tweet = data1003['tweet'].values.tolist()
    data_tweet2 = data1003['hashtags'].values.tolist()
    for j in disease:
      for k in range(len(data_tweet)):
        if (j in data_tweet[k] or j in data_tweet2[k]):
          if (x == 0):
            x = 1
            continue
          else:
            x += 1
    List2.append(str(x))
for i in Dict:
  if i not in List3:
    x = 0
    data1003 = data1002.loc[(data1002['created_at'] == i)]
    data_tweet = data1003['tweet'].values.tolist()
    data_tweet2 = data1003['hashtags'].values.tolist()
    for j in disease:
      for k in range(len(data_tweet)):
        if (j in data_tweet[k] or j in data_tweet2[k]):
          if (x == 0):
            x = 1
            continue
          else:
            x += 1
    List3.append(str(Dict[i]))
for i in Dict:
  if i not in List4:
    x = 0
    data1003 = data1002.loc[(data1002['created_at'] == i)]
    data_tweet = data1003['tweet'].values.tolist()
    data_tweet2 = data1003['hashtags'].values.tolist()
    for j in disease:
      for k in range(len(data_tweet)):
        if (j in data_tweet[k] or j in data_tweet2[k]):
          if (x == 0):
            x = 1
            continue
          else:
            x += 1
    List4.append(str(x/Dict[i]))
Fun = {'date': List, 'illness keywords matched': List2, 'number of posts': List3, 'precentage of keyword occurrence': List4}
S = pd.DataFrame.from_dict(Fun)
S.to_csv('relative_frequency_of_disease_keywords_on_posts_in_different_days.csv', index = False, encoding = 'UTF-8')