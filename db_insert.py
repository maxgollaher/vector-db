import glob
import json
import pandas as pd

from datasets import load_dataset
from utils import fast_pg_insert
from config import TIMESCALE_DB


def read_directory(path):
    files = glob.glob(f'{path}/*.jsonl')
    data = []
    for file in files:
        with open(file, 'r') as f:
            data.extend([json.loads(line) for line in f])

    return data


def load_podcast_data():
    print("Loading dataset...")
    ds = load_dataset("Whispering-GPT/lex-fridman-podcast")
    print("Dataset loaded.")

    print("Preparing podcast data...")
    podcast_data = []
    for i, record in enumerate(ds['train']):
        podcast_data.append({
            'id': record['id'],
            'title': record['title'],
        })
    podcast_df = pd.DataFrame(podcast_data)
    print("Podcast data prepared.")

    try:
        fast_pg_insert(podcast_df, TIMESCALE_DB, 'podcast', ['id', 'title'])
    except Exception as e:
        print(f"Failed to insert podcast data: {e}")


def extract_embeddings(embeddings):
    extracted_data = []
    for item in embeddings:
        id = item['custom_id']
        embedding = item['response']['body']['data'][0]['embedding']
        embedding_str = "[" + ",".join(map(str, embedding)) + "]"
        extracted_data.append({'id': id, 'embedding': embedding_str})
    return extracted_data


def extract_documents(documents):
    extracted_data = []
    for item in documents:
        id = item['custom_id']
        start_time = item['body']['metadata']['start_time']
        end_time = item['body']['metadata']['stop_time']
        content = item['body']['input']
        podcast_id = item['body']['metadata']['podcast_id']
        extracted_data.append(
            {'id': id, 'start_time': start_time, 'end_time': end_time, 'content': content,
             'podcast_id': podcast_id})
    return extracted_data


def load_podcast_segment_data():
    print("Reading embeddings...")
    embeddings = read_directory('embedding')
    embeddings_data = extract_embeddings(embeddings)
    embeddings_df = pd.DataFrame(embeddings_data)
    print("Embeddings loaded.")

    print("Reading documents...")
    documents = read_directory('documents')
    documents_data = extract_documents(documents)
    documents_df = pd.DataFrame(documents_data)
    print("Documents loaded.")

    # Merge DataFrames
    print("Preparing podcast segments data...")
    podcast_segments_df = pd.merge(documents_df, embeddings_df, left_on='id', right_on='id')
    podcast_segments_df = podcast_segments_df[['id', 'start_time', 'end_time', 'content', 'embedding', 'podcast_id']]
    print("Podcast segments data prepared.")

    print("Inserting podcast segments data...")
    try:
        fast_pg_insert(podcast_segments_df, TIMESCALE_DB, 'podcast_segment',
                       ['id', 'start_time', 'end_time', 'content', 'embedding', 'podcast_id'])
        print("Podcast segments data inserted.")
    except Exception as e:
        print(f"Failed to insert podcast segment data: {e}")

if __name__ == '__main__':
    # load_podcast_data()
    load_podcast_segment_data()
