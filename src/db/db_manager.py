from db.gdrive_models import engine, File, Session
from google_api.drive import service
from google_api.drive_manager import upload_file_to_drive


def upload_file(file_id, default_name, mime_type, file_size):
    '''Загрузка и сохрание файла'''
    session = Session()
    gdrive_id = upload_file_to_drive(service, file_id, default_name, mime_type)
    file = File(default_name=default_name,
                gdrive_id=gdrive_id,
                file_size=file_size,
                mime_type=mime_type,)
    session.add(file)
    session.commit()



def show_current_dir_elem():
    session = Session()
    files = session.query(File).all()
    
    messages = []

    for file in files:
        messages.append(str(file))

    return messages
    