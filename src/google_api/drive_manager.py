from googleapiclient.http import MediaFileUpload
from bot import bot
# from drive import service


def upload_file_to_drive(service, tg_file_id, default_name,
                        mime_type):
    file_info = bot.get_file(tg_file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(default_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    file_metadata = {'name': default_name}
    media = MediaFileUpload(filename=default_name, mimetype=mime_type)
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    return file.get('id')

