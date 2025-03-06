import facebook
from pymongo import MongoClient
import pandas as pd

# Set up the Facebook Graph API client
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCOUNT_ID = 'act_YOUR_ACCOUNT_ID'

graph = facebook.GraphAPI(ACCESS_TOKEN)

# Function to retrieve data from Facebook API
def get_facebook_data(endpoint, fields):
    try:
        data = graph.get_object(id=endpoint, fields=fields)
        return data.get('data', [])
    except facebook.GraphAPIError as e:
        print(f"Error fetching {endpoint}: {e}")
        return []

# Retrieve campaign data
campaigns = get_facebook_data(f'{ACCOUNT_ID}/campaigns', 'name,id,status,objective,spend')

# Retrieve ad set data
ad_sets = get_facebook_data(
    f'{ACCOUNT_ID}/adsets',
    'name,id,budget,start_time,end_time,targeting,optimization_goal,billing_event,bid_amount,daily_budget,lifetime_budget,insights.metric(reach,impressions,frequency,cpm).period(lifetime)'
)

# Retrieve ad data
ads = get_facebook_data(
    f'{ACCOUNT_ID}/ads',
    'name,id,creative{id,object_story_spec},insights.metric(clicks,ctr,cpc,conversions).period(lifetime)'
)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['facebook_data']

# Insert data into MongoDB (Avoid duplicates)
def insert_data(collection_name, data):
    if data:
        collection = db[collection_name]
        for record in data:
            if not collection.find_one({'id': record['id']}):  # Avoid duplicates
                collection.insert_one(record)
        print(f"Inserted {len(data)} records into {collection_name}")
    else:
        print(f"No data to insert for {collection_name}")

insert_data('campaigns', campaigns)
insert_data('ad_sets', ad_sets)
insert_data('ads', ads)

# Convert MongoDB collections to Pandas DataFrames
def fetch_dataframe(collection_name):
    collection = db[collection_name]
    return pd.DataFrame(list(collection.find({}, {'_id': 0})))  # Exclude MongoDB ID field

campaigns_df = fetch_dataframe('campaigns')
ad_sets_df = fetch_dataframe('ad_sets')
ads_df = fetch_dataframe('ads')

# Print DataFrames (optional)
print("Campaigns:\n", campaigns_df.head())
print("Ad Sets:\n", ad_sets_df.head())
print("Ads:\n", ads_df.head())
