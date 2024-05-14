from googleapiclient.http import MediaFileUpload
from bot import bot
import os
from db.db_manager import Session, File
# from drive import service


def upload_file_to_drive(service, file_id, default_name, mime_type):
    file_info = file_id
    downloaded_file = bot.download_file(file_info.file_path)
    with open(default_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    file_metadata = {'name': default_name}
    media = MediaFileUpload(filename=default_name, mimetype=mime_type)
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()

    os.remove(default_name)  # Удаление файла после его загрузки на диск    
    return file.get('id')


def load_files_from_gdrive(service):
    session = Session()
    results = service.files().list(pageSize=1000, fields="nextPageToken, files(id, name, mimeType, size)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        for item in items:
            gdrive_id = item['id']
            default_name = item['name']
            mime_type = item['mimeType']
            file_size = item.get('size')  # size might not be available for all files

            existing_file = session.query(File).filter(File.gdrive_id == gdrive_id).first()
            if existing_file is None:
                file = File(gdrive_id=gdrive_id, default_name=default_name, mime_type=mime_type, file_size=file_size)
                session.add(file)

        session.commit()

