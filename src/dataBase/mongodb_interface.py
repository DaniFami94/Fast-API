from motor.motor_asyncio import AsyncIOMotorClient
from bson import json_util
import json

class MongoDBInterface:

    def __init__(self): # Inicializamos la clase MongoDBInterface
        # Inicializamos las variables de la clase
        self.client = None
        self.db = None
        self.movies_collection = None
        self.users_collections = None

    async def connect(self):
        # with open('secrets.json') as f:
        #     secrets = json.load(f)
        #     mongo_user = secrets['mongoDB']['user']
        #     mongo_pwd = secrets['mongoDB']['pwd']

        uri = "mongodb://localhost:27017"


        try:
            self.client = AsyncIOMotorClient(uri)
            # 🔍 Verificar que realmente conecta
            await self.client.admin.command('ping')

            self.db = self.client["ecommerce_db"]
            self.movies_collection = self.db["movies"]
            self.users_collection = self.db["users"]

            print("✅ Conexión real con MongoDB establecida.")

        except Exception as e:
            print(f"❌ Error conectando a MongoDB: {e}")
    
    async def close(self):
        self.client.close()
    print("🔌 MongoDB connection closed.")
            
    # Métodos CRUD para películas
    async def get_all_movies(self):
        try:
            cursor = self.movies_collection.find({})
            movies = await cursor.to_list(length=None)
            return movies
        except Exception as e:
            print(f"Error getting movies: {e}")
            return []

    async def get_movie_by_id(self, id: int):
        try:
            movie = await self.movies_collection.find_one({"id": id})
            return movie
        except Exception as e:
            print(f"Error getting movie: {e}")
            return None
        
    async def get_movies_by_category(self, category: str):
        try:
            cursor = self.collection.find({"category": category})
            movies = await cursor.to_list(length=None)
            return movies
        except Exception as e:
            print(f"Error getting movies by category: {e}")
        return []

    async def create_movie(self, movie_data: dict):
        try:
            result = await self.movies_collection.insert_one(movie_data)
            return result.inserted_id
        except Exception as e:
            print(f"Error creating movie: {e}")
            return None
    
    async def update_movie(self, movie_id: int, movie_data: dict):
        try:
            result = await self.movies_collection.update_one({"id": movie_id}, {"$set": movie_data})
            return result.modified_count
        except Exception as e:
            print(f"Error updating movie: {e}")
            return None
    
    async def delete_movie(self, movie_id: int):
       try:
            result = await self.movies_collection.delete_one({"id": movie_id})
            return result.deleted_count
       except Exception as e:
            print(f"Error deleting movie: {e}")
            return None

# Métodos CRUD para usuarios

    async def get_all_users(self):
        try:
            cursor = self.users_collection.find({})
            users = await cursor.to_list(length=None)
            return json.loads(json_util.dumps(users)) # convierte a JSON para evitar problemas de serialización
        except Exception as e:
            print(f"Error getting users: {e}")
            return []

    async def get_user_by_id(self, id: int):
        try:
            user = await self.users_collection.find_one({"id": id})
            return user
        except Exception as e:
            print(f"Error getting User: {e}")
            return None

    async def create_user(self, user_data: dict):
        try:
            result = await self.users_collection.insert_one(user_data)
            return result.inserted_id
        except Exception as e:
            print(f"Error creating User: {e}")
            return None
        
    async def update_user(self, user_id: int, user_data: dict):
        try:
            result = await self.users_collection.update_one(
                {"id": user_id}, 
                {"$set": user_data}
            )
            return result.modified_count
        except Exception as e:
            print(f"Error updating User: {e}")
            return None

    async def delete_user(self, user_id: int):
        try:
            result = await self.users_collection.delete_one({"id": user_id})
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting User: {e}")
            return None
        
# CRUD para autenticación

    async def get_user_by_credentials(self, username: str, password: str):
        try:
            user = await self.users_collection.find_one({
                "username": {"$regex": f"^{username}$", "$options": "i"},
                "password": password
            })
            print(f"MongoDB query result: {user}")  # Debug print
            return user
        except Exception as e:
            print(f"Error in get_user_by_credentials: {e}")
            return None