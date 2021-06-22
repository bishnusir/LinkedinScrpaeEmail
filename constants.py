import pathlib, os

BASE_PATH = pathlib.Path(__file__).parent.absolute()
allowed_methods = ("xpath", "name" , "link_text", "partial_link_text", "id", "tag_name", "class_name", "css_selector")
MEDIA_PATH = f"{BASE_PATH}/media"
STATIC_PATH = f"{BASE_PATH}/static"
EXPORT_PATH = f"{BASE_PATH}/export"
DRIVER_PATH = f"{STATIC_PATH}/chromedriver.exe"


MAX_WAIT = 5 #maximum wait time for an element load

CSV_FileName='Connections.csv' #file name of linked connections details csv file
User_MIN_WAIT =50 #minimum number users email scrapped per day
User_MAX_WAIT =70 #maximum number users email scrapped per day



if not os.path.exists(STATIC_PATH):
    os.mkdir(STATIC_PATH)

