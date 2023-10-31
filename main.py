from fastapi import FastAPI
from starlette_admin.contrib.sqla import Admin

from database import DatabaseSelector
# from database import engine
from tests.routers import router as tests_router

from utils.models import Base


# Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create admin
# admin = Admin(engine, title="Multi Tenancy")

# # Add view
from tests.admin import *

# Mount admin to your app
# admin.mount_to(app)

# Include app-wise routers below
app.include_router(router=tests_router)

app.add_middleware(DatabaseSelector)
