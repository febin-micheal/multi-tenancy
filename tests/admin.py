# Add view
from starlette_admin import DropDown
from starlette_admin.contrib.sqla import ModelView

# from main import admin
from tests.models import Company, Employee

# admin.add_view(
#     DropDown(
#         "Tests",
#         icon="fa fa-list",
#         views=[
#             ModelView(Company),
#             ModelView(Employee),
#         ],
#     )
# )
