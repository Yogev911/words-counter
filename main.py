from multiprocessing import Process
import api
import dal_service

if __name__ == '__main__':
    try:
        app_dal = Process(target=dal_service.serve)
        app_dal.start()
        app_words = Process(target=api.serve)
        app_words.start()

    except Exception as e:
        print(e.__str__())
