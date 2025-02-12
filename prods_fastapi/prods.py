from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# Define skin tone to color category mappings
SKIN_TONE_RECOMMENDATIONS = {
    "fair": {
        "best": ["Cool", "Neutral"],
        "avoid": ["Warm"]
    },
    "medium": {
        "best": ["Neutral", "Warm"],
        "avoid": ["Cool"]
    },
    "dark": {
        "best": ["Warm", "Neutral"],
        "avoid": ["Cool"]
    }
}

# Load the cleaned CSV file into a pandas DataFrame
df = pd.read_csv("hm_products_with_color_categories.csv")

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Add your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the CSV API!"}

# Define an endpoint for skin tone-based recommendations
@app.get("/recommendations/skin-tone/{skin_tone}")
def get_skin_tone_recommendations(
    skin_tone: str,
    page: int = Query(1, description="Page number", ge=1),
    limit: int = Query(20, description="Items per page", le=20),
):
    # Validate skin tone
    if skin_tone.lower() not in SKIN_TONE_RECOMMENDATIONS:
        return {"error": "Invalid skin tone. Please choose 'fair', 'medium', or 'dark'"}
    
    # Get recommended colors for the skin tone
    recommended_colors = SKIN_TONE_RECOMMENDATIONS[skin_tone.lower()]["best"]
    
    # Filter products by recommended color categories
    filtered_df = df[df["color_category"].isin(recommended_colors)]
    
    # Calculate pagination
    total_items = len(filtered_df)
    total_pages = (total_items + limit - 1) // limit
    start = (page - 1) * limit
    end = start + limit
    
    # Get paginated data
    paginated_data = filtered_df.iloc[start:end].to_dict(orient="records")
    
    return {
        "skin_tone": skin_tone,
        "recommended_colors": recommended_colors,
        "data": paginated_data,
        "page": page,
        "limit": limit,
        "total_items": total_items,
        "total_pages": total_pages,
    }

# Define an endpoint to get paginated and filtered data
@app.get("/data/")
def get_data(
    mst: str = Query(None, description="Filter by 'mst' column"),
    page: int = Query(1, description="Page number", ge=1),
    limit: int = Query(20, description="Items per page", le=20),
):
    # Filter data by 'mst' column if provided
    filtered_df = df
    if mst:
        filtered_df = df[df["mst"] == mst]

    # Calculate pagination
    
    total_items = len(filtered_df)
    total_pages = (total_items + limit - 1) // limit
    start = (page - 1) * limit
    end = start + limit

    # Get paginated data
    paginated_data = filtered_df.iloc[start:end].to_dict(orient="records")

    return {
        "data": paginated_data,
        "page": page,
        "limit": limit,
        "total_items": total_items,
        "total_pages": total_pages,
    }