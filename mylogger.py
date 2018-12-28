import logging

def getLogger(loggerName):
	mylogger = logging.getLogger(loggerName)
	mylogger.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	
	stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(formatter)
	mylogger.addHandler(stream_handler)

	#file_handler = logging.FileHandler(loggerName+".log")
	#file_handler.setFormatter(formatter)
	#mylogger.addHandler(file_handler)

	return mylogger

if __name__ == "__main__":
	mylogger = getLogger()
	mylogger.info("server start!!!")

