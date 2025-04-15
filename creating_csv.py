import pandas as pd
import numpy as np
import csv

all_data_info = pd.read_csv("./all_data_info.csv")
train_info = pd.read_csv("./train_info.csv")

artists = train_info['artist']

train_only_images = []
test_only_images = []

image_name_Train = []
artists_names_Train = []
labels_Train = []
date_Train = []
genre_Train = []
style_Train = []
title_Train = []

image_name_Test = []
artists_names_Test = []
date_Test = []
genre_Test = []
style_Test = []
title_Test = []


image_name_New = []
artists_names_New = []
date_New = []
genre_New = []
style_New = []
title_New = []
with open('all_data_info.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        image_name = row['new_filename']
        artist_group = row['artist_group']
        artist_name = row['artist']
        date = row['date']
        genre = row['genre']
        style = row['style']
        title = row['title']
        in_train = row['in_train']
        if artist_group == 'train_only':
            df = train_info[train_info['filename'] == image_name]
            label = df.iloc[0]['artist']
            image_name_Train.append(image_name)
            artists_names_Train.append(artist_name)
            labels_Train.append(label)
            date_Train.append(date)
            genre_Train.append(genre)
            style_Train.append(style)
            title_Train.append(title)
        if artist_group == 'test_only':
            image_name_Test.append(image_name)
            artists_names_Test.append(artist_name)
            date_Test.append(date)
            genre_Test.append(genre)
            style_Test.append(style)
            title_Test.append(title)
        if artist_group == 'train_and_test':
            if artist_name == 'II' or artist_name == 'Hadis-i Şerîf' or artist_name == 'Hadis-i Şerîfler' or artist_name == '1':
                continue
            else:
                if in_train == "True":
                    image_name_New.append(image_name)
                    artists_names_New.append(artist_name)
                    date_New.append(date)
                    genre_New.append(genre)
                    style_New.append(style)
                    title_New.append(title)

train_data = pd.DataFrame({
    'image_name': image_name_Train,
    'artist_name': artists_names_Train,
    'label': labels_Train,
    'date': date_Train,
    'genre': genre_Train,
    'style': style_Train,
    'title': title_Train
})

test_data = pd.DataFrame({
    'image_name': image_name_Test,
    'artist_name': artists_names_Test,
    'date': date_Test,
    'genre': genre_Test,
    'style': style_Test,
    'title': title_Test
})

train_data.to_csv("./new_Train.csv", index=False)
test_data.to_csv("./new_Test.csv", index=False)


data = pd.DataFrame({
    'title': title_New,
    'style': style_New,
    'genre': genre_New,
    'date': date_New,
    'artist_name': artists_names_New,
    'image_name': image_name_New,
})


selected_artists = np.random.choice(data['artist_name'].unique(), 500, replace=False)
selected_images = []

for artist_name in selected_artists:
    artist_data = data[data['artist_name'] == artist_name]
    if len(artist_data) <= 10:
        selected_images.extend(artist_data.to_dict('records'))
    else:
        selected_images.extend(artist_data.sample(10).to_dict('records'))

selected_images_df = pd.DataFrame(selected_images)

artists_names_New = [a for a in artists_names_New if a not in artists_names_Train]
artists_names_New = [a for a in artists_names_New if a not in artists_names_Test]


filename = 'temp.csv'
selected_images_df.to_csv(filename, index=False)

train_data = pd.read_csv("./new_Train.csv")
train_11_4 = pd.read_csv("./temp.csv")
common_columns = [col for col in train_data.columns if col in train_11_4.columns and col != 'label']

combined_data = pd.concat([train_data[common_columns], train_11_4[common_columns]])

combined_data.to_csv("./train_validation_data.csv", index=False)

