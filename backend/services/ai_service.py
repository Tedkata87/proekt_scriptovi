import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)
def generate_bike_recommendation(data):

    prompt = f"""
You are an MTB expert.

Recommend mountain bikes.

Rider height:
{data.get("height")}

Rider weight:
{data.get("weight")}

Terrain:
{data.get("terrain")}

Budget:
{data.get("budget")}

Preferences:
{data.get("preferences")}

Rules:

1. Recommend MTB bikes only.

2. If budget is low,
recommend second hand bikes.

3. Return:
Brand
Model
Reason

4. Maximum 5 bikes.
"""

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )

    return {
        "recommendation":
        response.choices[0]
        .message.content
    }

def generate_setup(data):

    prompt = f"""
You are a professional MTB suspension tuner.

Rider height:
{data.get("rider_height")}

Rider weight:
{data.get("rider_weight")}

Terrain:
{data.get("terrain")}

Bike type:
{data.get("bike_type")}

Brand:
{data.get("brand")}

Model:
{data.get("model")}

Fork:
{data.get("fork")}

Shock:
{data.get("shock")}

Frame size:
{data.get("frame_size")}

Wheel size:
{data.get("wheel_size")}

Drivetrain:
{data.get("drivetrain")}

Brakes:
{data.get("brakes")}

Handlebars:
{data.get("handlebars")}

Give:

Fork pressure

Shock pressure

Sag

Rebound

Compression

Tire pressure

Brake lever angle

Handlebar position

Additional setup tips
"""

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5
    )

    return {
        "setup":
        response.choices[0]
        .message.content
    }