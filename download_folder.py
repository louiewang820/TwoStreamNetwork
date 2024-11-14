import gdown
url_models = "https://drive.google.com/drive/folders/1jNkO4NMsukSRTtiaPeB5xU42Q7tr1mD3?usp=drive_link"
gdown.download_folder(url_models, quiet=True, use_cookies=False)
print('installed pretrained_models folder')
results = "https://drive.google.com/drive/folders/1SMPdVvZ5T5t2rORfgsGuw6j_bx_QElBh?usp=drive_link"
gdown.download_folder(results, quiet=True, use_cookies=False)
print('installed results folder')
